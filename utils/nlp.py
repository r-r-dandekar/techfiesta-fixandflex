import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

_API_KEY = os.getenv("GEMINI_API_KEY")
_CLIENT = genai.Client(api_key=_API_KEY, config={'system_instruction': 'You are a helpful but concside assistant made to help users find out about loan schemes.'})
_MODEL_ID = "gemini-2.5-flash"

def response(query: str) -> str:
    """
    Sends a query to Gemini and returns the text response.
    """
    try:
        res = _CLIENT.models.generate_content(
            model=_MODEL_ID,
            contents=query
        )
        return res.text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    answer = response(input("Enter query: "))
    print(answer)