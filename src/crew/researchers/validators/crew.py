from crewai import Crew

from .agents import HotelResearchValidatorsAgents
from .tasks import HotelResearchValidatorsTasks

class HotelResearchValidatorsCrew:
	def __init__(self):
		agents = HotelResearchValidatorsAgents()
		self.senior_researcher = agents.senior_hospitality_researcher()

	def kickoff(self, state):
		tasks = HotelResearchValidatorsTasks()
		crew = Crew(
			agents=[self.senior_researcher],
			tasks=[
				tasks.validate_hotel_list(self.senior_researcher),
			],
			verbose=True
		)

		result = crew.kickoff()
		return {**state, "validations": result}