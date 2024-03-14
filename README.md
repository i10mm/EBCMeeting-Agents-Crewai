
# Welcome to the EBC Meeting Preparation Report Toolkit!

This toolkit is designed to help you, as a Client Manager for Global System Integrators (GSI), prepare for Executive Briefing Center (EBC) meetings with your clients. Using the CrewAI framework, we can automate the process of gathering information, analyzing industry trends, and generating a comprehensive report that will help your clients understand how NVIDIA AI solutions can benefit their business.

## Agents

- Research Agent: Gather information about the target company and its industry.
- Industry Analysis Agent: Analyze the target company's industry, focusing on AI adoption and competition.
- NVIDIA Expert Agent: Identify gaps in the target company's AI implementation and recommend relevant NVIDIA solutions.
- Meeting Strategy Agent: Develop talking points, questions, and strategic angles for the meeting based on the gathered information.
- Summary and Briefing Agent: Compile all gathered information into a concise and informative briefing document.

## Tasks

- Research Task: Conduct thorough research on people and companies involved in the meeting.
- Industry Analysis Task: Analyze industry trends, challenges, and opportunities related to AI.
- NVIDIA Solutions Recommendation Task: Recommend relevant NVIDIA solutions based on the research and industry analysis.
- Meeting Strategy Task: Develop a document outlining talking points, questions, and strategic angles for the meeting.
- Summary and Briefing Task: Generate a comprehensive briefing document summarizing all findings and recommendations.

## Usage

To use this toolkit, simply provide the emails of the meeting participants (other than yourself), the context of the meeting, and your objective for the meeting. The CrewAI framework will orchestrate the agents and tasks to generate a comprehensive EBC meeting preparation report.

```python
from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from src.tasks import MeetingPreparationTasks
from src.agents import MeetingPreparationAgents

tasks = MeetingPreparationTasks()
agents = MeetingPreparationAgents()

print("## Welcome to the EBC Meeting Prep Crew")
print('-------------------------------')
participants = input("What are the emails for the participants (other than you) in the meeting?\n")
context = input("What is the context of the meeting?\n")
objective = input("What is your objective for this meeting?\n")

# Create Agents and Tasks...

report = crew.kickoff()

print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(report)
```

The output will be a comprehensive EBC meeting preparation report that will help your clients understand how NVIDIA AI solutions can benefit their business. The report will include a summary of the target company and its industry, key findings from the research and industry analysis, recommended NVIDIA solutions and their benefits, talking points, questions, and strategic angles for the meeting, and a list of potential questions that the executives from the target company may ask.

## Tools

The toolkit leverages the following tools:

- `ExaSearchTool`: A tool for conducting web searches and retrieving webpage content.
- `NvidiaSolutionsTool`: A tool for recommending relevant NVIDIA solutions based on the research report and industry analysis.

## Contributing

We welcome contributions to the EBC Meeting Preparation Report Toolkit! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

