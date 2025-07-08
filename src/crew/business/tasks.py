from crewai import Task
from textwrap import dedent

class BusinessManagerTasks:
	def create_email_proposal(self, agent) -> Task:
		return Task(
			description=dedent(f"""\
				Based on the marketing research:
				{{marketing_insights}}
				
				and based on the hotels list:
				{{hotels}}
				
				You are responsible to create a email business proposal for each hotel for the following event format:
				
				'A digital detox event where people put their phone away for a hours, in which the company that you are representing,
				Social Circle, is responsible to offer a kit that help them to achieve less dependency on their phone/social media/dumb scrolling.'
				
				Address the email to a specific individual (e.g., [Recipient Name], [Recipient Title], [Recipient Company]). 
				If no specific details are provided, use placeholders like "Dear [Recipient Name]" and customize based on context.
				
				Clearly state the purpose of the email: to propose a business collaboration, service, or solution.
				Provide a brief overview of the proposed idea, product, or service, focusing on how it addresses the recipient’s needs or challenges.
				
				Maintain a professional, confident, and courteous tone.
				Keep the email concise and easy to read with short paragraphs or bullet points where appropriate.
				
				"""),
			agent=agent,
            expected_output=dedent(f"""
            JSON FORMAT:
            [
            	{{
            		"hotel_id": "hotel list element id",
            		"hotel_name": "",
            		"hotel_email": "",
            		"email_proposal": ""
            	}}
            ]
			""")
		)