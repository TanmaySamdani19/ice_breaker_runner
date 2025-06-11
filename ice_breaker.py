import os
from dotenv import load_dotenv  # Add this import
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrape_linkedin_profile

# Load environment variables from .env file
load_dotenv()

information = """
"""

if __name__ == "__main__":
    print("Hello LangChain!")
    print(f"API Key: {os.environ.get('OPENAI_API_KEY', 'API key not found')}")
    summary_template = """
    Given the Linkedin information {information} about a person, I want you to create:
    1. A short summary of the person
    2. Two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )


    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url = "https://www.linkedin.com/in/tanmay-samdani-96606b205/",mock=True)
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
