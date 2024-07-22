import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from tools.tools import get_profile_url_tavily


load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-4o")
    template = """given the full name {name_of_person} I want you to get me a link to their LinkedIn Profile. Your answer should only contain the URL."""

    prompt = PromptTemplate(template=template, input_variables=["name_of_person"])

    tools = [
        Tool(
            name="Crawl Google for Linkedin Profile Page",
            func=get_profile_url_tavily,
            description="Useful to search for user linkedin profile page URL.",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    result = agent_executor.invoke({"input": prompt.format_prompt(name_of_person=name)})

    linkedin_url = result["output"]
    print(linkedin_url)
    return linkedin_url


if __name__ == "__main__":
    linkedin_url = lookup("Pratik Patil Turtlemint")
