import openai
from openai import OpenAI
from voice_bot.config import settings
from voice_bot.core.personal_database import get_response

def chat_with_gpt(prompt):
    """
    Process user input and return appropriate response.
    Checks personal database first, then falls back to OpenAI API.
    
    Args:
        prompt (str): The user's prompt
        
    Returns:
        str: Response from personal database or ChatGPT
    """
    # Check for specific personal questions first
    personal_question_keywords = [
        "life story", "about you", "background", 
        "superpower", "strength", "best at",
        "grow", "areas", "improve", "develop",
        "misconception", "misunderstand", "coworkers", 
        "push", "boundary", "boundaries", "limit", "challenge"
    ]
    
    # Check if this is a personal question
    for keyword in personal_question_keywords:
        if keyword.lower() in prompt.lower():
            # This seems to be a personal question, check our database
            return get_response(prompt)
    
    # Not a personal question, use the OpenAI API
    try:
        # Create a client instance with the API key and base URL
        client = OpenAI(api_key=settings.OPENAI_API_KEY, base_url=settings.OPENAI_API_BASE_URL)
        
        # Use the new API format
        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant representing a real person. Respond in a natural, conversational way."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error communicating with ChatGPT: {e}")
        return "Sorry, I am having trouble responding right now. Please try asking about my background, superpower, areas I want to grow in, misconceptions about me, or how I push my boundaries."