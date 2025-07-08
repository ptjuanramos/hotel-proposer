from textwrap import dedent
from crewai import Agent

class HotelResearchingAgents:

    def hospitality_researcher(self):
        return Agent(
            role='Hospitality Researcher',
            goal='Find and compile comprehensive lists of hotels based on Switzerland and criteria',
            backstory=dedent("""\
                You are an expert in hospitality industry research with years of 
                experience in identifying hotels that match specific business criteria. You know 
                how to find hotels that would benefit from partnership opportunities."""),
            verbose=True,
            allow_delegation=False
        )
