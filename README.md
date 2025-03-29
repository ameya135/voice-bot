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
   pip install openai pyttsx3 SpeechRecognition flask python-dotenv
   ```

2. Make sure you have espeak-ng installed on your system (for text-to-speech):
   ```
   # On Arch Linux
   sudo pacman -S espeak-ng alsa-utils
   
   # On Ubuntu/Debian
   sudo apt-get install espeak-ng alsa-utils
   ```

3. Set up your environment variables in the `.env` file:
   ```
   # API Keys
   OPENAI_API_KEY=your_api_key_here
   
   # API URLs
   OPENAI_API_BASE_URL=https://openrouter.ai/api/v1
   
   # Models
   OPENAI_MODEL=openai/gpt-4o-mini-search-preview
   ```

4. Run the voice bot:
   ```
   python voice_bot.py
   ```

5. Open your browser and go to http://localhost:5000 to use the web interface.

## Customization

You can customize the voice modulation settings in the `.env` file:

```properties
# Voice Settings
VOICE_RATE=160
VOICE_VOLUME=0.9
VOICE_GENDER=male

# Espeak Settings
ESPEAK_PITCH=50
ESPEAK_SPEED=150
ESPEAK_VOICE=en
```

## Development Findings and Design Decisions

### Project Approach

The development of this voice bot focused on creating a modular, maintainable system with strong separation of concerns. Key design goals included:

1. **Modular Architecture**: Breaking functionality into logical modules (core, UI, config, utils) to make the code more maintainable and extendable.

2. **Multiple Voice Interfaces**: Supporting both text and speech interaction through a web interface with browser-based speech recognition and server-side text-to-speech capabilities.

3. **Environment-Based Configuration**: Moving sensitive data like API keys and configurable settings to environment variables to enhance security and flexibility.

4. **Robust Error Handling**: Implementing comprehensive error handling across the application, particularly in the text-to-speech module to handle failures gracefully.

### Technical Challenges and Solutions

#### Text-to-Speech Issues

The most significant challenge was creating a reliable text-to-speech system that works consistently across platforms. Several issues were encountered:

- **Reference Errors**: pyttsx3 encountered weakly-referenced object errors due to problems with garbage collection
- **Missing System Dependencies**: Required system packages like `espeak-ng` and `alsa-utils` needed to be installed
- **Inconsistent Voice Quality**: Different platforms had varying voice quality and capabilities

Solutions implemented:

- Added multiple fallback mechanisms for TTS (pyttsx3 → espeak/say command → platform-specific approaches)
- Implemented proper thread handling with timeouts to prevent hanging
- Added platform detection to use the best available TTS method on each operating system
- Introduced voice modulation settings (rate, volume, pitch, gender) with easy configuration

#### AI Integration

The integration with OpenAI's API required adaptation due to API changes:

- Updated from the deprecated `openai.ChatCompletion` interface to the new client-based model
- Added support for alternative providers via configurable base URLs
- Implemented a local database of personal information to provide consistent answers to personal questions

#### Web Interface Design

The web interface was chosen over a desktop UI due to platform compatibility issues:

- Created a responsive design that works across devices
- Implemented browser-based speech recognition using the Web Speech API
- Used Flask for server-side processing, allowing both speech and text interaction

### Future Improvements

Potential enhancements for future versions:

1. Add voice authentication to ensure only authorized users can access personal information
2. Implement more sophisticated natural language processing for better question understanding
3. Add conversation history and context awareness for more natural interactions
4. Support for additional languages and voice accents
5. Develop a responsive mobile interface for on-the-go interactions

### Final Thoughts

This voice bot demonstrates how modern AI capabilities can be combined with speech technologies to create personalized voice assistants. The modular design ensures that components can be improved or replaced individually as technology evolves, while the environment-based configuration makes deployment in different contexts straightforward.