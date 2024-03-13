from textwrap import dedent
from crewai import Task

class MeetingPreparationTasks():
    def research_task(self, agent, participants, context):
        return Task(
            description=dedent(f"""\
                Conduct thorough research on the following meeting participants and the meeting context:

                Participants: {participants}
                Context: {context}

                Gather information about their background, interests, and potential questions or concerns.
                Summarize your findings in a concise report.
                """),
            expected_output=dedent("""\
                A report summarizing the research findings on the meeting participants and context.
                """),
            agent=agent
        )

    def industry_analysis_task(self, agent, participants, context):
        return Task(
            description=dedent(f"""\
                Analyze the industry relevant to the meeting participants and context:

                Participants: {participants}
                Context: {context}

                Identify key trends, challenges, and opportunities within the industry.
                Assess how these factors could impact the meeting and potential outcomes.
                Summarize your analysis in a report.
                """),
            expected_output=dedent("""\
                A report summarizing the industry analysis, including trends, challenges, and opportunities.
                """),
            agent=agent
        )

    def nvidia_solutions_recommendation_task(self, agent, research_report, industry_analysis):
        return Task(
            description=dedent(f"""\
                Based on the research report and industry analysis, identify gaps in the target company's AI implementation and recommend relevant NVIDIA solutions.

                Research Report:
                {research_report}

                Industry Analysis:
                {industry_analysis}

                Provide a list of recommended NVIDIA solutions tailored to the target company's needs and industry trends.
                """),
            expected_output=dedent("""\
                A list of recommended NVIDIA solutions with justifications based on the research and industry analysis.
                """),
            agent=agent
        )

    def meeting_strategy_task(self, agent, context, objective, nvidia_recommendations):
        return Task(
            description=dedent(f"""\
                Develop talking points, questions, and strategic angles for the meeting based on the provided context, objective, and NVIDIA solutions recommendations:

                Context: {context}
                Objective: {objective}
                NVIDIA Recommendations:
                {nvidia_recommendations}

                Create a document outlining a clear meeting strategy, including:
                * Compelling talking points that align with the objective and address the target company's needs.
                * Insightful questions to engage the participants and gather valuable information.
                * Strategic angles to position NVIDIA solutions effectively.
                """),
            expected_output=dedent("""\
                A document outlining a comprehensive meeting strategy, including talking points, questions, and strategic angles.
                """),
            agent=agent
        )

    def summary_and_briefing_task(self, agent, context, objective, research_report, industry_analysis, meeting_strategy):
        return Task(
            description=dedent(f"""\
                Compile all gathered information into a concise and informative briefing document for the EBC meeting:

                Context: {context}
                Objective: {objective}
                Research Report:
                {research_report}
                Industry Analysis:
                {industry_analysis}
                Meeting Strategy:
                {meeting_strategy}

                The briefing document should include:
                * A summary of the target company and its industry.
                * Key findings from the research and industry analysis.
                * Recommended NVIDIA solutions and their benefits.
                * Talking points, questions, and strategic angles for the meeting.
                * A list of potential questions that the executives from the target company may ask.
                """),
            expected_output=dedent("""\
                A comprehensive briefing document summarizing all findings and recommendations for the EBC meeting.
                """),
            agent=agent
        )