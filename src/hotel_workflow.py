from dotenv import load_dotenv
from langgraph.graph import StateGraph

from .crew.business.crew import BusinessCrew
from .crew.marketing.crew import MarketingCrew
from .crew.researchers.validators.crew import HotelResearchValidatorsCrew
from .isolated_nodes.copy_writer_node import CopyWriterNode
from .states.hotel_research_state import HotelResearchState
from .crew.researchers.crew import HotelResearchingCrew
from .tools.google_drive import GoogleDrive

load_dotenv()


class HotelWorkflow:
	def __init__(self):
		workflow = StateGraph(HotelResearchState)
		google_drive = GoogleDrive()

		workflow.add_node("hotel_research_crew", HotelResearchingCrew().kickoff)
		workflow.add_node("hotel_research_validator_crew", HotelResearchValidatorsCrew().kickoff)
		workflow.add_node("hotel_marketing_crew", MarketingCrew().kickoff)
		workflow.add_node("business_manager", BusinessCrew().kickoff)
		workflow.add_node("doc_creator", CopyWriterNode(google_drive).create_proposal_doc)
		# workflow.add_node("proposal_email_validator", isolated_nodes.summarize_complaints)
		# workflow.add_node("manual_validator", isolated_nodes.save_summaries)
		# workflow.add_node("send_email", isolated_nodes.save_summaries)

		def check_validation(state):
			print(state)
			return state

		workflow.add_node("check_validation", check_validation)
		#
		workflow.set_entry_point("hotel_research_crew")
		# workflow.add_conditional_edges(
		# 		"hotel_list_researcher",
		# 		isolated_nodes.new_emails,
		# 		{
		# 			"continue": 'draft_responses',
		# 			"end": 'wait_next_run'
		# 		}
		# )

		workflow.add_edge('hotel_research_crew', 'hotel_research_validator_crew')
		workflow.add_edge('hotel_research_validator_crew', 'hotel_marketing_crew')
		#workflow.add_edge('hotel_marketing_crew', 'check_validation')
		workflow.add_edge('hotel_marketing_crew', 'business_manager')
		workflow.add_edge('business_manager', 'doc_creator')

		# workflow.add_edge('categorize_complaints', 'summarize_complaints')
		# workflow.add_edge('summarize_complaints', 'save_summaries')
		# workflow.add_edge('save_summaries', 'wait_next_run')
		# workflow.add_edge('wait_next_run', 'check_new_emails')

		self.app = workflow.compile()
