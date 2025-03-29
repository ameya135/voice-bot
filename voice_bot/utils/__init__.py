"""
Utility functions for the Voice Bot application
"""

def sanitize_input(text):
    """
    Sanitize user input to prevent potential issues
    
    Args:
        text (str): The input text to sanitize
        
    Returns:
        str: Sanitized text
    """
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = " ".join(text.split())
    
    # Basic sanitization - can be expanded as needed
    return text.strip()


def format_bot_response(response):
    """
    Format the bot's response for better presentation
    
    Args:
        response (str): The raw response from the AI
        
    Returns:
        str: Formatted response
    """
    if not response:
        return "I don't have a response for that."
    
    # Add any formatting logic here
    return response