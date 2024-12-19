import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_bot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the model
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Sorry, I couldn't process your message. Error: {e}"