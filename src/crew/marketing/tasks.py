from crewai import Task
from textwrap import dedent

class MarketingTasks:
	def obtain_marketing_info(self, agent) -> Task:
		return Task(
			description=dedent(f"""\
				Based on the obtained hotel list: 
				{{hotels}}
				
				Compile the most relevant information for a business proposal
                for digital detox events.
                    For each hotel, provide:

                    1 - Demographics
                    2 - Preferences
                    3 - Booking patterns
                    4 - psychographics (wellness, sustainability interest)
					5 - Market Trends: Wellness tourism growth, digital fatigue demand, seasonal opportunities (Google Trends).
					6 - Marketing Channels: Website/mobile optimization, social media engagement, email ROI, review management.
					7 - Brand Fit: Alignment with hotel’s mission, unique selling points.
					8 - Local Context: Nearby attractions, partnership opportunities (e.g., yoga studios).  
					
				The result should be truthful, we can use some assumptions, however it must have at least 60% of veracity.
				Minimize the number of tokens used as a response.              
				"""),
			agent=agent,
            expected_output=dedent(f"""
            JSON FORMAT:
            [
            	{{
            		"hotel_id": "",
            		"hotel_name": "",
            		"demographic_information": "",
            		"preferences": "",
            		"booking_patterns": "",
            		"psychographics": "",
            		"market_trends": "",
            		"brand_fit": "",
            		"local_context": "",
            	}}
            ]
			""")
		)