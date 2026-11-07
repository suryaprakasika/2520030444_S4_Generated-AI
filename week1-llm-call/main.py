
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini
client = genai.Client(api_key=api_key)

try:
    # Generate response
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="What is Artificial Intelligence? Explain in simple words."
    )

    print("\nLLM Response:")
    print(response.text)

except Exception as e:
    print("\nSomething went wrong:")
    print(e)
