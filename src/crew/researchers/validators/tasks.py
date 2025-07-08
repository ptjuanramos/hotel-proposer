from crewai import Task
from textwrap import dedent

class HotelResearchValidatorsTasks:

	def validate_hotel_list(self, agent):
		return Task(
			description=dedent("""\
				Validate the completeness and quality of hotel data:
                  1. Check all required fields are present
                  2. Ensure data formats are correct
                  3. Identify any missing critical information
                  4. Rate data quality for each hotel (1-10)
                  5. Flag hotels with insufficient data
				"""),
			agent=agent,
            expected_output=dedent("""
            JSON FORMAT:
            [{{
            	"hotel_id": "hotel list element id",
            	"is_insufficient_data": false,
            	"is_data_format_correct": false,
            	"are_all_fields_present": false,
            	"data_quality": 3,
            	"remarks": [
            		"(string to represent a remark regarding any missing info)"
            	]
            }}]
            """)
		)
