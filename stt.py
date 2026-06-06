# stt.py — Captures voice from microphone and converts it to text

import speech_recognition as sr


def take_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening... Please speak now.")
        # Reduce background noise before recording
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Recording complete.")
        except sr.WaitTimeoutError:
            print("No speech detected. Timed out.")
            return None

    try:
        # en-IN covers both Hindi and English spoken in India
        text = recognizer.recognize_google(audio, language="en-IN")
        print(f"Recognized: '{text}'")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return None
    except sr.RequestError as e:
        # Triggers when there is a network or API issue
        print(f"Google Speech API error: {e}")
        return None