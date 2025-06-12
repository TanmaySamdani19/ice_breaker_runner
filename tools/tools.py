import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twitter Profile Page."""

    # Check if API key exists
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return [
            {
                "url": "",
                "content": f"Error: TAVILY_API_KEY not found in environment variables. Please add it to your .env file.",
            }
        ]
    search = TavilySearchResults(api_key=api_key)
    res = search.run(f"{name} linkedin")
    return res
