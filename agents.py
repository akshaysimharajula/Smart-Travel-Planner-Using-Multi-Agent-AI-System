import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment")

client = Groq(api_key=GROQ_API_KEY)

def call_llm(system_prompt, user_prompt, max_tokens=600):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content
