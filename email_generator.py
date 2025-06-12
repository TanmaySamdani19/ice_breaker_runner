import os
from typing import List
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from output_parsers import email_parser, Email

load_dotenv()


def generate_email(name: str, summary: str, facts: List[str], length: str = "medium", 
                  tone: str = "professional", purpose: str = "networking") -> Email:
    
    # Define length guidelines
    length_guidelines = {
        "short": "Keep the email concise and to the point, around 3-4 sentences.",
        "medium": "Write a moderate length email with 2-3 paragraphs.",
        "long": "Create a detailed email with multiple paragraphs and comprehensive content."
    }
    
    # Define tone guidelines
    tone_guidelines = {
        "professional": "Use formal, business-appropriate language and maintain a professional demeanor.",
        "friendly": "Use warm, approachable language while maintaining professionalism.",
        "casual": "Use relaxed, conversational language as if writing to a friend."
    }
    
    # Define purpose templates
    purpose_templates = {
        "networking": "The purpose is to connect and build a professional relationship.",
        "job_inquiry": "The purpose is to inquire about potential job opportunities.",
        "collaboration": "The purpose is to explore potential collaboration opportunities.",
        "introduction": "The purpose is to introduce yourself and establish initial contact."
    }
    
    facts_text = "\n".join([f"- {fact}" for fact in facts])
    
    email_template = """
    You are writing a personalized email to {name} based on their professional profile.
    
    Person's Summary: {summary}
    
    Interesting Facts about them:
    {facts}
    
    Email Requirements:
    - Length: {length_guideline}
    - Tone: {tone_guideline}
    - Purpose: {purpose_guideline}
    
    Create a personalized email that:
    1. Shows you've researched them (reference their background/achievements)
    2. Establishes credibility and common ground
    3. Has a clear purpose and call-to-action
    4. Incorporates relevant facts naturally
    5. Feels genuine and not templated
    
    Important: Do not use placeholder text like [Your Name] or [Your Company]. 
    Write from the perspective of someone reaching out professionally.
    
    \n{format_instructions}
    """
    
    email_prompt_template = PromptTemplate(
        input_variables=["name", "summary", "facts", "length_guideline", "tone_guideline", "purpose_guideline"],
        template=email_template,
        partial_variables={"format_instructions": email_parser.get_format_instructions()}
    )
    
    llm = ChatOpenAI(temperature=0.7, model_name="gpt-4o-mini")
    chain = email_prompt_template | llm | email_parser
    
    result = chain.invoke(input={
        "name": name,
        "summary": summary,
        "facts": facts_text,
        "length_guideline": length_guidelines[length],
        "tone_guideline": tone_guidelines[tone],
        "purpose_guideline": purpose_templates[purpose]
    })
    
    return result


if __name__ == "__main__":
    # Test the email generator
    test_summary = "Software engineer with expertise in AI and machine learning"
    test_facts = ["Graduated from Stanford", "Works at Google"]
    
    email = generate_email(
        name="John Doe",
        summary=test_summary,
        facts=test_facts,
        length="medium",
        tone="professional",
        purpose="networking"
    )
    
    print("Generated Email:")
    print("Subject:", email.subject)
    print("Body:", email.body)