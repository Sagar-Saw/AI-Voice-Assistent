# main.py — Entry point for the terminal-based Voice Assistant

from stt import take_voice_input as listen
from llm import generate_response, clear_history
from tts import speak_text as speak


def main():
    print("=" * 50)
    print(" Voice Assistant Started!")
    print(" Say 'exit' or 'bye' to stop")
    print("=" * 50)

    speak("Hello! I am your voice assistant. You can speak in English or Hindi!")

    while True:
        print("\n--- Ready. Speak now ---")
        user_input = listen()

        # Handle case where no speech was detected
        if user_input is None:
            speak("I could not understand. Please try again.")
            continue

        stop_words = ["exit", "bye", "quit", "band karo", "alvida"]
        if any(word in user_input.lower() for word in stop_words):
            speak("Goodbye! Have a great day!")
            break

        # Get AI response and speak it out
        ai_response = generate_response(user_input)
        speak(ai_response)


if __name__ == "__main__":
    main()