from crewai import Crew

from .agents import MarketingAgents
from .tasks import MarketingTasks

class MarketingCrew:
	def __init__(self):
		agents = MarketingAgents()
		self.researcher = agents.marketing_researcher()
		# self.senior_researcher = agents.senior_marketing_researcher()

	def kickoff(self, state):
		print("### Filtering emails")
		tasks = MarketingTasks()
		crew = Crew(
			agents=[self.researcher],
			tasks=[
				tasks.obtain_marketing_info(self.researcher),
			],
			verbose=True
		)
		result = crew.kickoff(inputs={
			"hotels": str(state["hotels"]),
		})
		return {**state, "marketing_insights": result}