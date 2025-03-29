"""
Database module for storing personal information and responses to common questions
"""

# Sample personal information database
PERSONAL_INFO = {
    "life_story": "I grew up in a small coastal town before moving to the city to pursue computer science. After graduating, I spent three years at a tech startup where I discovered my passion for AI and machine learning. Now I'm working on innovative projects that combine technology with practical human needs.",
    
    "superpower": "My superpower is definitely creative problem-solving. I can look at complex problems from multiple angles and find connections that others miss. This helps me develop innovative solutions that consider both technical constraints and human factors.",
    
    "growth_areas": [
        "Expanding my knowledge of large language models and their applications in everyday technology",
        "Improving my public speaking skills to better communicate technical concepts to non-technical audiences",
        "Developing stronger leadership abilities to guide teams through challenging projects"
    ],
    
    "misconception": "My coworkers often think I'm always serious because I'm focused during meetings. What they don't realize is that I have a pretty adventurous side outside of work - I love outdoor activities and have a quirky sense of humor that comes out once we get to know each other better.",
    
    "pushing_boundaries": "I push my boundaries by deliberately taking on projects that make me uncomfortable. Each month, I try to learn something completely outside my expertise. Last month it was woodworking, this month it's advanced data visualization. I also regularly seek feedback from mentors who will be brutally honest about my work."
}

def get_response(question_type):
    """
    Get a response from the personal information database
    
    Args:
        question_type (str): The type of question being asked
        
    Returns:
        str: The response from the database
    """
    question_map = {
        "life_story": ["life story", "background", "about you", "about yourself"],
        "superpower": ["superpower", "strength", "best at", "good at"],
        "growth_areas": ["grow", "improve", "develop", "learning"],
        "misconception": ["misconception", "misunderstand", "wrong about you", "misconceive"],
        "pushing_boundaries": ["push", "boundary", "limit", "challenge yourself", "comfort zone"]
    }
    
    # Check for exact match first
    if question_type in PERSONAL_INFO:
        response = PERSONAL_INFO[question_type]
        if isinstance(response, list):
            return ". ".join(response)
        return response
        
    # Check for keyword matches
    for key, keywords in question_map.items():
        for keyword in keywords:
            if keyword.lower() in question_type.lower():
                response = PERSONAL_INFO[key]
                if isinstance(response, list):
                    return ". ".join(response)
                return response
                
    # Default response if no match is found
    return "I don't have specific information about that. Please ask me about my life story, superpower, areas for growth, misconceptions about me, or how I push my boundaries."