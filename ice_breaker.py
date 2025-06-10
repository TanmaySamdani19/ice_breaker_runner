import os

if __name__ == "__main__":
    print("Hello LangChain!")
    print(os.environ.get('OPENAI_API_KEY', 'API key not found'))
