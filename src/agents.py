from textwrap import dedent
from crewai import Agent

# Ensure this import path is correct based on your project structure
from tools import ExaSearchTool, NvidiaSolutionsTool

class MeetingPreparationAgents:
    def research_agent(self):
        # Utilizes ExaSearchTool's tools for research purposes
        return Agent(
            role='Research Specialist',
            goal='Conduct thorough research on people and companies involved in the meeting',
            tools=ExaSearchTool.tools(),  # Provides a list of methods for research
            backstory=dedent("""\
                As a Research Specialist, your mission is to uncover detailed information
                about the individuals and entities participating in the meeting. Your insights
                will lay the groundwork for strategic meeting preparation."""),
            verbose=True
        )

    def industry_analysis_agent(self):
        # Utilizes ExaSearchTool's tools for industry analysis
        return Agent(
            role='Industry Analyst',
            goal='Analyze the current industry trends, challenges, and opportunities',
            tools=ExaSearchTool.tools(),  # Provides a list of methods for analysis
            backstory=dedent("""\
                As an Industry Analyst, your analysis will identify key trends,
                challenges facing the industry, and potential opportunities that
                could be leveraged during the meeting for strategic advantage."""),
            verbose=True
        )

    def nvidia_expert_agent(self):
        # Utilizes NvidiaSolutionsTool for recommending NVIDIA solutions
        return Agent(
            role='NVIDIA Solutions Specialist',
            goal="Identify gaps in the target company's AI implementation and recommend relevant NVIDIA solutions",
            tools=[NvidiaSolutionsTool.recommend_solutions],  # Specific method for NVIDIA solutions
            backstory=dedent("""\
                As an NVIDIA Solutions Specialist, you possess deep knowledge of NVIDIA's AI offerings.
                You can analyze a company's AI needs and recommend the most suitable NVIDIA solutions
                to address those needs and enhance their AI capabilities."""),
            verbose=True
        )

    def meeting_strategy_agent(self):
        # Utilizes ExaSearchTool's tools for meeting strategy development
        return Agent(
            role='Meeting Strategy Advisor',
            goal='Develop talking points, questions, and strategic angles for the meeting',
            tools=ExaSearchTool.tools(),  # Provides a list of methods for strategy development
            backstory=dedent("""\
                As a Strategy Advisor, your expertise will guide the development of
                talking points, insightful questions, and strategic angles
                to ensure the meeting's objectives are achieved."""),
            verbose=True
        )

    def summary_and_briefing_agent(self):
        # Utilizes ExaSearchTool's tools for compiling briefing documents
        return Agent(
            role='Briefing Coordinator',
            goal='Compile all gathered information into a concise, informative briefing document',
            tools=ExaSearchTool.tools(),  # Provides a list of methods for document compilation
            backstory=dedent("""\
                As the Briefing Coordinator, your role is to consolidate the research,
                analysis, and strategic insights into a comprehensive briefing document."""),
            verbose=True
        )
