#!/usr/bin/env python3
"""
Launcher for the Voice Bot application
This file provides a convenient way to start the application from the root directory
"""
import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the main function from the voice_bot package
from voice_bot.__main__ import main

if __name__ == "__main__":
    main()