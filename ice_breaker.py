from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()

    print("Hello Langchain")

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/", mock=True
    )

    summary_prompt_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt = PromptTemplate(input_variables=["information"], template=summary_prompt_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-2024-05-13")
    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    parser = StrOutputParser()
    chain = summary_prompt | llm | parser

    res = chain.invoke({"information": linkedin_data})
    print(res)
