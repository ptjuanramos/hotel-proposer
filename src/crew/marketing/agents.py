from textwrap import dedent
from crewai import Agent

class MarketingAgents:

    def marketing_researcher(self):
        return Agent(
            role='Marketing Researcher',
            goal='Find and compile the most relevant information for a business proposal',
            backstory=dedent("""\
                You are an expert in marketing with years of 
                experience in identifying the most crucial information to create business proposals for events. You know 
                how and where to find the necessary information to transfer to business managers."""),
            verbose=True,
            allow_delegation=False
        )

    # def senior_marketing_researcher(self):
    #     return Agent(
    #         role='Hospitality Researcher',
    #         goal='Find and compile comprehensive lists of hotels based on Switzerland and criteria',
    #         backstory=dedent("""\
	# 				You are an expert in hospitality industry research with years of
	#                 experience in identifying hotels that match specific business criteria. You know
	#                 how to find hotels that would benefit from partnership opportunities."""),
    #         verbose=True,
    #         allow_delegation=False
    #     )