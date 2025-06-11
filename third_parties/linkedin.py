import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape information from LinkedIn profile,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        # Use mock data URL for testing
        mock_url = "https://gist.githubusercontent.com/TanmaySamdani19/b202c7da85601e33425e4f9c10f49ee7/raw/1611cfe85ce11ee6969b2e037942808e4c10ad5c/tanmay-samdani-scrapin.json"
        response = requests.get(mock_url, timeout=20)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            # Filter out empty values and unwanted keys
            data = {
                k: v
                for k, v in data.items()
                if v not in ([], "", None)
                and k not in ["certifications"]
            }
            return data
        else:
            print(f"Error fetching mock data: {response.status_code}")
            return None
    else:
        # Real API call to scrapin.io
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        api_key = os.environ.get("SCRAPIN_API_KEY")  # Get API key from environment
        
        if not api_key:
            print("Error: SCRAPIN_API_KEY not found in environment variables")
            return None
            
        params = {
            "linkedInUrl": linkedin_profile_url,
            "apikey": os.environ.get("SCRAPIN_API_KEY")
        }
        
        try:
            response = requests.get(api_endpoint, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json().get("person")
                if data:
                    # Filter out empty values and unwanted keys
                    data = {
                        k: v
                        for k, v in data.items()
                        if v not in ([], "", None)
                        and k not in ["certifications"]
                    }
                    return data
                else:
                    print("No person data found in response")
                    return None
            else:
                print(f"API Error: {response.status_code} - {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None


if __name__ == "__main__":
    print("Testing LinkedIn Profile Scraper...")
    
    # Test with mock data
    result = scrape_linkedin_profile(
        linkedin_profile_url='https://www.linkedin.com/in/tanmay-samdani-96606b205/', 
        mock=True
    )
    
    if result:
        print("✅ Mock data retrieved successfully:")
        print("-" * 50)
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("❌ Failed to retrieve mock data")