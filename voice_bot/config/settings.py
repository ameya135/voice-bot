import os
from dotenv import load_dotenv
import pathlib

# Get the project root directory (two levels up from this file)
ROOT_DIR = pathlib.Path(__file__).parent.parent.parent.absolute()

# Load environment variables from .env file
load_dotenv(os.path.join(ROOT_DIR, '.env'))

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'openai/gpt-4o-mini-search-preview')
OPENAI_API_BASE_URL = os.getenv('OPENAI_API_BASE_URL', 'https://openrouter.ai/api/v1')

# Text-to-Speech Configuration
TTS_DEFAULT_ENABLED = True

# Voice Modulation Settings
VOICE_RATE = int(os.getenv('VOICE_RATE', 160))       # Speed of speech (words per minute, normal=160-170)
VOICE_VOLUME = float(os.getenv('VOICE_VOLUME', 0.9))  # Volume (0.0 to 1.0)
VOICE_GENDER = os.getenv('VOICE_GENDER', 'male')     # Preferred voice gender ("male", "female", "neutral")

# For espeak specifically
ESPEAK_PITCH = int(os.getenv('ESPEAK_PITCH', 50))     # Pitch (0-99)
ESPEAK_SPEED = int(os.getenv('ESPEAK_SPEED', 150))    # Speed (words per minute)
ESPEAK_VOICE = os.getenv('ESPEAK_VOICE', 'en')        # Voice variant ("en", "en-us", "en-gb", etc.)

# Speech Recognition Configuration
SPEECH_RECOGNIZER = os.getenv('SPEECH_RECOGNIZER', 'google')  # Options: google, sphinx, etc.

# UI Configuration
UI_WINDOW_TITLE = "Voice Chat Bot"
UI_WINDOW_SIZE = "600x500"
UI_WINDOW_BG = "#f0f0f0"

# Server Configuration
SERVER_HOST = os.getenv('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.getenv('SERVER_PORT', 5000))