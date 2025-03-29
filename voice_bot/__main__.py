#!/usr/bin/env python3
"""
Main entry point for the Voice Bot application
"""
from voice_bot.ui.web_interface import WebInterface

def main():
    """
    Start the Voice Bot application with the web interface
    """
    print("Starting Voice Bot with web interface...")
    web_interface = WebInterface(host='localhost', port=5000)
    web_interface.run()

if __name__ == "__main__":
    main()