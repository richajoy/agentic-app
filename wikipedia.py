from crewai import Agent, Task, Crew
from crewai_tools import tool
import wikipediaapi
import os 

os.environ["OPENAI_API_KEY"] = "xxxxx"
llm = "gpt-4o"

@tool("wikipedia_lookup")
def wikipedia_lookup(q: str) -> str:
    """Look up a query on Wikipedia and return the result"""
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(q)
    return page.summary if page.exists() else "Page not found"

# Define the agent 
researcher_agent = Agent(
                role="Researcher", 
                goal="You research topics using Wikipedia and report on the results", 
                backstory="You are an experienced writer and editor", 
                tools=[wikipedia_lookup], 
                llm=llm
    )
query = input("Enter a query: ")

task1 = Task(
    description=query,
    expected_output="A short text based on the tool output",
    agent=researcher_agent,
    tools=[wikipedia_lookup]
)

# Define the crew
crew = Crew(
    agents=[researcher_agent],
    tasks=[task1],
    verbose=True
)

result=crew.kickoff()

# Accessing the task output 
task_output = task1.output

print(f"Task Description: {task_output.description}")
print(f"Task Summary: {task_output.summary}")
print(f"Raw Output: {task_output.raw}")
