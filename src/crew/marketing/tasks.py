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
                    1. Demographic information
                    2. Customer needs
                    3. Season patterns
                    4. Pricing strategy 
                    5. Market Gaps
                    6. Highlight treats
                    7. Social media engagement
                
				"""),
			agent=agent,
            expected_output=dedent(f"""
            JSON FORMAT:
            [
            	{{
            		"hotel_id": "",
            		"hotel_name": "",
            		"demographic_information": "",
            		"customer_needs": "",
            		"season_patterns": "",
            		"pricing_strategy": "",
            		"market_gaps": "",
            		"highlight_treats": "",
            		"social_media_engagement": ""
            	}}
            ]
			""")
		)