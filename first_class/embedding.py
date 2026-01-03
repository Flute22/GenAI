import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]
from google import genai
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = input("Enter your prompt: ")

response = client.models.generate_content(
    model = 'gemini-3-flash-preview',
    contents = {prompt}
)

print("Response:", response.text)
