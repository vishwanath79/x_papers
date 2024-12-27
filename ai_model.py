import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_text(prompt, model="gpt-4o"):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content":  prompt
            }
        ]
    )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


