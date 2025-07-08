from crewai import Crew

from .agents import BusinessManagerAgents
from .tasks import BusinessManagerTasks


class BusinessCrew:
	def __init__(self):
		agents = BusinessManagerAgents()
		self.researcher = agents.business_manager()

	def kickoff(self, state):

		tasks = BusinessManagerTasks()
		crew = Crew(
			agents=[self.researcher],
			tasks=[
				tasks.create_email_proposal(self.researcher),
			],
			verbose=True
		)

		result = crew.kickoff(inputs={
			"hotels": str(state["hotels"]),
			"marketing_insights": str(state["marketing_insights"]),
		})

		return {**state, "proposals": result.raw}