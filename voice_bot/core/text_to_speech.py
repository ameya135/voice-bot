import pyttsx3
import logging
import subprocess
import tempfile
import os
import platform
import threading
from voice_bot.config import settings

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def text_to_speech(text):
    """
    Enhanced text-to-speech with multiple fallback options
    
    Args:
        text (str): The text to be converted to speech
    """
    if not text:
        return
    
    # Try primary method first (pyttsx3)
    try_pyttsx3(text)
    
def try_pyttsx3(text):
    """Try using pyttsx3 for text-to-speech with proper error handling"""
    try:
        # Create a new engine instance each time to avoid reference issues
        engine = pyttsx3.init()
        
        # Set properties for better quality and performance
        engine.setProperty('rate', settings.VOICE_RATE)
        engine.setProperty('volume', settings.VOICE_VOLUME)
        
        # Get available voices and try to use one that matches preferred gender
        voices = engine.getProperty('voices')
        if voices:
            preferred_gender = settings.VOICE_GENDER.lower()
            found_preferred_voice = False
            
            # First pass: try to find a voice matching the preferred gender
            for voice in voices:
                voice_name = voice.name.lower()
                if preferred_gender == "male" and ("male" in voice_name or "david" in voice_name or "george" in voice_name):
                    engine.setProperty('voice', voice.id)
                    found_preferred_voice = True
                    logger.info(f"Using male voice: {voice.name}")
                    break
                elif preferred_gender == "female" and ("female" in voice_name or "zira" in voice_name or "susan" in voice_name):
                    engine.setProperty('voice', voice.id)
                    found_preferred_voice = True
                    logger.info(f"Using female voice: {voice.name}")
                    break
                
            # If no gender-specific voice found, try to find a high-quality voice
            if not found_preferred_voice:
                for voice in voices:
                    if "english" in voice.name.lower() and ("high" in voice.name.lower() or "premium" in voice.name.lower()):
                        engine.setProperty('voice', voice.id)
                        logger.info(f"Using high-quality voice: {voice.name}")
                        break
        
        # Use a lock to prevent multiple TTS operations from interfering
        tts_lock = threading.Lock()
        
        with tts_lock:
            # Start in a thread with a timeout to prevent hanging
            def speak_thread():
                try:
                    engine.say(text)
                    engine.runAndWait()
                except Exception as e:
                    logger.error(f"TTS engine error: {e}")
                finally:
                    # Clean up
                    try:
                        engine.stop()
                    except:
                        pass
            
            thread = threading.Thread(target=speak_thread)
            thread.daemon = True
            thread.start()
            thread.join(timeout=15)  # Allow up to 15 seconds for speech
            
            # If thread is still alive after timeout, it's stuck
            if thread.is_alive():
                logger.warning("TTS operation timed out, trying to stop engine")
                try:
                    engine.stop()
                except:
                    pass
                    
    except Exception as e:
        logger.error(f"pyttsx3 error: {e}")
        try_fallback_tts(text)

def try_fallback_tts(text):
    """Fallback TTS using system commands if available"""
    system = platform.system().lower()
    
    try:
        if system == 'linux':
            # Try espeak directly with modulation parameters
            command = [
                'espeak',
                f'-a {int(settings.VOICE_VOLUME * 100)}',  # Amplitude (volume)
                f'-p {settings.ESPEAK_PITCH}',             # Pitch
                f'-s {settings.ESPEAK_SPEED}',             # Speed
                f'-v {settings.ESPEAK_VOICE}'              # Voice variant
            ]
            
            # Add the text at the end
            command.append(text)
            
            # Run espeak with the parameters
            subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
        elif system == 'darwin':  # macOS
            # macOS 'say' command with voice rate
            rate_param = str(settings.VOICE_RATE / 175.0)  # Normalize rate
            voice_name = "Alex"  # Default male voice
            
            if settings.VOICE_GENDER.lower() == "female":
                voice_name = "Samantha"
            
            subprocess.run(['say', '-r', rate_param, '-v', voice_name, text], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
                           
        elif system == 'windows':
            # Create a temporary VBS script for Windows with voice modulation
            vbs_script = f'''
            Dim sapi
            Set sapi = CreateObject("SAPI.SpVoice")
            
            ' Set voice based on gender preference
            gender = "{settings.VOICE_GENDER}"
            Dim voiceFound
            voiceFound = False
            
            For Each voice in sapi.GetVoices
                If gender = "male" And InStr(voice.GetDescription, "Male") > 0 Then
                    Set sapi.Voice = voice
                    voiceFound = True
                    Exit For
                ElseIf gender = "female" And InStr(voice.GetDescription, "Female") > 0 Then
                    Set sapi.Voice = voice
                    voiceFound = True
                    Exit For
                End If
            Next
            
            ' Set rate (-10 to 10, with 0 being normal)
            sapi.Rate = ({settings.VOICE_RATE} - 170) / 17
            
            ' Set volume (0 to 100)
            sapi.Volume = {int(settings.VOICE_VOLUME * 100)}
            
            ' Speak the text
            sapi.Speak "{text}"
            '''
            
            # Write VBS script to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.vbs') as f:
                f.write(vbs_script.encode())
                script_path = f.name
            
            # Execute the script
            subprocess.run(['cscript', '//nologo', script_path], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
            
            # Clean up
            try:
                os.unlink(script_path)
            except:
                pass
                
    except Exception as e:
        logger.error(f"Fallback TTS failed: {e}")
        # At this point, we've tried everything and failed
        logger.warning("All TTS methods failed, speech will not be played")