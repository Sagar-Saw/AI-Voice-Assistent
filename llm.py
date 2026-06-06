# llm.py — Sends user input to Groq AI and returns a response

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

# Validate API key before proceeding
if not API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please add it to your .env file.")

client = Groq(api_key=API_KEY)

SYSTEM_PROMPT = """
You are a helpful bilingual voice assistant.
- STRICTLY reply in the SAME language the user uses
- If user writes or speaks in English, reply in English ONLY
- If user writes or speaks in Hindi, reply in Hindi ONLY
- Never mix languages
- Keep answers short and clear (2-3 sentences)
"""

# Stores conversation so the assistant remembers context across turns
conversation_history = []


def generate_response(user_text):
    conversation_history.append({"role": "user", "content": user_text})

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *conversation_history  # Full history sent for contextual replies
            ]
        )
        answer = response.choices[0].message.content.strip()
        conversation_history.append({"role": "assistant", "content": answer})
        return answer

    except Exception as e:
        print(f"LLM Error: {e}")
        return "Sorry, something went wrong. Please try again."


def clear_history():
    # Resets memory for a fresh conversation session
    conversation_history.clear()