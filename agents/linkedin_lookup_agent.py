import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool

from langchain.agents import create_react_agent, AgentExecutor

from langchain import hub

load_dotenv()

def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-4o")
    template = """given the full name {name_of_person} I want you to get me a link to their LinkedIn Profile. Your answer should only contain the URL."""

    prompt = PromptTemplate(template=template, input_variables=["name_of_person"])
    return "https://www.linkedin.com/in/pratikpatil24"


if __name__ == "__main__":
    linkedin_url = lookup("Pratik Patil")