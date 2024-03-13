from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process

from src.tasks import MeetingPreparationTasks
from src.agents import MeetingPreparationAgents

# Import and create the manager LLM
from langchain_openai import ChatOpenAI

manager_llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)  # Replace with your preferred LLM

tasks = MeetingPreparationTasks()
agents = MeetingPreparationAgents()

print("## Welcome to the EBC Meeting Prep Crew")
print('-------------------------------')
participants = input("What are the emails for the participants (other than you) in the meeting?\n")
context = input("What is the context of the meeting?\n")
objective = input("What is your objective for this meeting?\n")

# Create Agents
researcher_agent = agents.research_agent()
industry_analyst_agent = agents.industry_analysis_agent()
nvidia_expert_agent = agents.nvidia_expert_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()

# Create Tasks
research = tasks.research_task(researcher_agent, participants, context)
industry_analysis = tasks.industry_analysis_task(industry_analyst_agent, participants, context)
nvidia_recommendations = tasks.nvidia_solutions_recommendation_task(nvidia_expert_agent, research, industry_analysis)
meeting_strategy = tasks.meeting_strategy_task(meeting_strategy_agent, context, objective, nvidia_recommendations)
summary_and_briefing = tasks.summary_and_briefing_task(summary_and_briefing_agent, context, objective, research, industry_analysis, meeting_strategy)

# Set dependencies (optional)
meeting_strategy.context = [research, industry_analysis]
summary_and_briefing.context = [research, industry_analysis, meeting_strategy]

# Create Crew with hierarchical process
crew = Crew(
    agents=[
        researcher_agent,
        industry_analyst_agent,
        nvidia_expert_agent,
        meeting_strategy_agent,
        summary_and_briefing_agent
    ],
    tasks=[
        research,
        industry_analysis,
        nvidia_recommendations,
        meeting_strategy,
        summary_and_briefing
    ],
    verbose=True,
    process=Process.hierarchical,
    manager_llm=manager_llm
)

report = crew.kickoff()

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(report)

# Save the report to a file
with open("reports/ebc_meeting_prep_report.txt", "w") as f:
    f.write(report)