import speech_recognition as sr

def speech_to_text(callback=None):
    """
    Convert speech to text using the microphone
    
    Args:
        callback: Optional callback function to report status
    
    Returns:
        str: Recognized text or None if recognition failed
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if callback:
            callback("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            if callback:
                callback(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            if callback:
                callback("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            if callback:
                callback(f"Could not request results; {e}")
            return None