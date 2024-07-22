from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup


def ice_break_with(name: str) -> str:
    linkedin_url = lookup(name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    print(linkedin_data)
    summary_prompt_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt = PromptTemplate(
        input_variables=["information"], template=summary_prompt_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-2024-05-13")

    parser = StrOutputParser()
    chain = summary_prompt | llm | parser
    res = chain.invoke({"information": linkedin_data})
    print(res)
    return res


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_break_with("Pratik Patil Turtlemint")
