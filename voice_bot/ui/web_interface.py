import threading
from flask import Flask, render_template, request, jsonify
from voice_bot.core.speech_recognition import speech_to_text
from voice_bot.core.text_to_speech import text_to_speech
from voice_bot.core.ai_service import chat_with_gpt
from voice_bot.config import settings

class WebInterface:
    def __init__(self, host='0.0.0.0', port=5000):
        """
        Initialize the web interface for the voice bot
        
        Args:
            host (str): Host to run the server on
            port (int): Port to run the server on
        """
        self.app = Flask(__name__, 
                         template_folder='templates',
                         static_folder='static')
        self.host = host
        self.port = port
        self.setup_routes()
        
    def setup_routes(self):
        """Set up the Flask routes"""
        
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        @self.app.route('/send_message', methods=['POST'])
        def send_message():
            user_message = request.json.get('message', '')
            if not user_message:
                return jsonify({'error': 'No message provided'})
            
            # Get response from ChatGPT
            response = chat_with_gpt(user_message)
            
            # If text-to-speech is enabled, do it in a separate thread
            if request.json.get('speak', settings.TTS_DEFAULT_ENABLED):
                threading.Thread(target=text_to_speech, args=(response,), daemon=True).start()
                
            return jsonify({'response': response})
            
        @self.app.route('/listen', methods=['POST'])
        def listen():
            # This would normally use the microphone to listen
            # However, browser-based speech recognition is better done client-side with JavaScript
            # This endpoint is more of a placeholder for server-side processing if needed
            return jsonify({'error': 'Speech recognition should be done client-side'})
    
    def run(self):
        """Run the web server"""
        self.app.run(host=self.host, port=self.port, debug=True)