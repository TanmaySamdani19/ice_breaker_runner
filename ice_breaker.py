import os
from dotenv import load_dotenv  # Add this import
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
 
# Load environment variables from .env file
load_dotenv()
 
information = """
Levi has short, straight black hair styled in an undercut curtain, as well as narrow, intimidating dull gray eyes with dark circles under them and a deceptively youthful face. He is quite short, but his physique is well-developed in musculature from extensive vertical maneuvering equipment usage. He is usually either frowning or expressionless; that, plus his extremely calm demeanor, often makes it difficult for others to guess what he is thinking.
 
He is most often seen in his Survey Corps uniform, with a light gray button-up shirt underneath, along with his trademark white ascot. When embarking on expeditions outside the Walls, he also wears the Survey Corps' green hooded cloak. Once, when forced to take leave from his duties due to injury, Levi was seen in a black suit, plain white shirt, ascot, and dress shoes. However, since the beginning of the coup d'état, he has left the ascot off. For most of the time during which the Survey Corps was on the run from the military and monarchy, he simply wore his vertical maneuvering equipment harness over casual clothes.
 
After a close-encounter explosion from a Thunder Spear set off by Zeke Yeager, Levi now has several scars across his face including one across his right eye and is missing both the index and middle fingers on his right hand.
"""
 
if __name__ == "__main__":
    print("Hello LangChain!")
    print(f"API Key: {os.environ.get('OPENAI_API_KEY', 'API key not found')}")
    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A short summary of the person
    2. Two interesting facts about the person
    """
 
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
 
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})
 
    print(res)