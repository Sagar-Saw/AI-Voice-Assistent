# tts.py — Converts text to speech and plays it as audio

import os
import tempfile
from gtts import gTTS
import pygame


def detect_language(text):
    # Returns 'hi' if Hindi characters found, otherwise 'en'
    for char in text:
        if '\u0900' <= char <= '\u097F':
            return 'hi'
    return 'en'


def speak_text(text, lang=None):
    # Initialize only when needed, not at import time
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    if lang is None:
        lang = detect_language(text)

    # Use system temp folder so no files appear in project directory
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    filename = tmp.name
    tmp.close()

    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

    except Exception as e:
        print(f"[TTS] Error: {e}")

    finally:
        # Always clean up temp file even if playback failed
        if os.path.exists(filename):
            os.remove(filename)