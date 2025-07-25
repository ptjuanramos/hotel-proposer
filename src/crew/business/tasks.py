from crewai import Task
from textwrap import dedent

from src.models.proposal import HotelEmailProposalResponse


class BusinessManagerTasks:
	def create_email_proposal(self, agent) -> Task:
		return Task(
			description=dedent(f"""\
				Based on the marketing research:
				{{marketing_insights}}
				
				and based on the hotels list:
				{{hotels}}
				
				You are Nina Maurer, responsible to create a email business proposal for each hotel for the following product description:
				
				'Ready-to-use solution that enables hotels to easily offer a Digital Detox stay to their guests.

				It includes:
				
					• A physical kit (games, journal, candle, etc.)
					• A secure phone box for reception
					• A simple, staff-friendly process
					• No upfront cost, pay-as-you-go model, and currently in test phase — ideal for hotels looking to stand out with a meaningful, screen-free guest experience.'
				
				Address the email to a specific individual (e.g., [Recipient Name], [Recipient Title], [Recipient Company]).
				If no specific contact name is provided, use placeholders like "Dear [Hotel Name] Management" and customize based on context.
				
				Clearly state the purpose of the email: to propose a business collaboration, service, or solution.
				Provide a brief overview of the proposed idea, product, or service, focusing on how it addresses the recipient’s needs or challenges.
				Use the the marketing research as your advantage.
				
				Maintain a confident and friendly tone.
				Keep the email concise and easy to read with short paragraphs or bullet points where appropriate.
				"""),
			agent=agent,
			output_pydantic=HotelEmailProposalResponse,
            expected_output=dedent("Structured analysis following the HotelEmailProposalResponse schema")
		)