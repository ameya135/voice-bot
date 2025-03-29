# Settings and configuration for the Voice Bot

# OpenAI API Configuration
OPENAI_API_KEY = "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"
OPENAI_MODEL = "openai/gpt-4o-mini-search-preview"
OPENAI_API_BASE_URL="https://openrouter.ai/api/v1"

# Text-to-Speech Configuration
TTS_DEFAULT_ENABLED = True

# Voice Modulation Settings
VOICE_RATE = 160         # Speed of speech (words per minute, normal=160-170)
VOICE_VOLUME = 0.9       # Volume (0.0 to 1.0)
VOICE_GENDER = "male"    # Preferred voice gender ("male", "female", "neutral")

# For espeak specifically
ESPEAK_PITCH = 50        # Pitch (0-99)
ESPEAK_SPEED = 150       # Speed (words per minute)
ESPEAK_VOICE = "en"      # Voice variant ("en", "en-us", "en-gb", etc.)

# Speech Recognition Configuration
SPEECH_RECOGNIZER = "google"  # Options: google, sphinx, etc.

# UI Configuration
UI_WINDOW_TITLE = "Voice Chat Bot"
UI_WINDOW_SIZE = "600x500"
UI_WINDOW_BG = "#f0f0f0"