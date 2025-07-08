from crewai import Task
from textwrap import dedent

class HotelResearchingTasks:
	def research_hotels_list(self, agent) -> Task:
		return Task(
			description=dedent(f"""\
				Based on the location analysis and market research, compile a comprehensive 
                    list of hotels in Switzerland that match these criteria: Inclined to create digital detox events.
                
                    For each hotel, provide:
                    1. Hotel name
                    2. Exact location/address
                    3. Hotel category (luxury, business, boutique, etc.)
                    4. Contact information if available
                    5. Website
                    6. Brief description
                    7. Why they match our criteria
                
                    Get 15-25 hotels that best match our outreach criteria.
				"""),
			agent=agent,
            expected_output=dedent(f"""
            JSON FORMAT:
            [{{
            	"id": 1
            	"name": "",
            	"location": "",
            	"category": "",
            	"contact_information": "",
            	"website": "",
            	"brief_description": "",
            	"matching_criteria": ""
            }}]""")
		)