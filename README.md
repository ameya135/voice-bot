# Voice Bot

A voice-enabled chatbot that can answer questions about you through both text and speech interfaces.

## Features

- Text-to-speech capabilities with adjustable voice modulation
- Speech recognition for voice input
- Web-based user interface
- Personal information database for answering questions about you
- Integration with OpenAI API for general queries

## Questions the Bot Can Answer

- "What should we know about your life story in a few sentences?"
- "What's your #1 superpower?"
- "What are the top 3 areas you'd like to grow in?"
- "What misconception do your coworkers have about you?"
- "How do you push your boundaries and limits?"

## Project Structure

```
voice-bot/
  ├── voice_bot.py               # Main launcher
  └── voice_bot/                 # Main package
      ├── __init__.py            # Package initialization
      ├── __main__.py            # Entry point
      ├── config/                # Configuration
      │   ├── __init__.py
      │   └── settings.py        # Settings and API keys
      ├── core/                  # Core functionality
      │   ├── __init__.py
      │   ├── ai_service.py      # OpenAI integration
      │   ├── personal_database.py # Personal information
      │   ├── speech_recognition.py # Speech-to-text
      │   └── text_to_speech.py  # Text-to-speech with modulation
      ├── ui/                    # User interface
      │   ├── __init__.py
      │   ├── web_interface.py   # Flask web interface
      │   ├── static/            # Static assets
      │   └── templates/         # HTML templates
      │       └── index.html     # Main page
      └── utils/                 # Utility functions
          └── __init__.py        # Helpers and utilities
```

## Usage

1. Install the required dependencies:
   ```
   pip install openai pyttsx3 SpeechRecognition flask
   ```

2. Make sure you have espeak-ng installed on your system (for text-to-speech):
   ```
   # On Arch Linux
   sudo pacman -S espeak-ng
   
   # On Ubuntu/Debian
   sudo apt-get install espeak-ng
   ```

3. Run the voice bot:
   ```
   python voice_bot.py
   ```

4. Open your browser and go to http://localhost:5000 to use the web interface.

## Customization

You can customize the voice modulation settings in `voice_bot/config/settings.py`:

```python
# Voice Modulation Settings
VOICE_RATE = 160         # Speed of speech (words per minute)
VOICE_VOLUME = 0.9       # Volume (0.0 to 1.0)
VOICE_GENDER = "male"    # Preferred voice gender ("male", "female")

# For espeak specifically
ESPEAK_PITCH = 50        # Pitch (0-99)
ESPEAK_SPEED = 150       # Speed (words per minute)
ESPEAK_VOICE = "en"      # Voice variant ("en", "en-us", "en-gb", etc.)
```