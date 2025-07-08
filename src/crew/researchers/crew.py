from crewai import Crew

from .agents import HotelResearchingAgents
from .tasks import HotelResearchingTasks

class HotelResearchingCrew:
	def __init__(self):
		agents = HotelResearchingAgents()
		self.researcher = agents.hospitality_researcher()

	def kickoff(self, state):
		tasks = HotelResearchingTasks()
		crew = Crew(
			agents=[self.researcher],
			tasks=[
				tasks.research_hotels_list(self.researcher),
			],
			verbose=True
		)

		result = crew.kickoff()
		return {**state, "hotels": result}