import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise SystemExit("GEMINI_API_KEY is missing. Check your .env file.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="In one sentence, what is a dataclass in Python?"
)

print(interaction.output_text)