from datetime import datetime
from chat_request import send_openai_request

def generate_horoscope(birth_datetime: datetime, place_of_birth: str) -> str:
    prompt = f"""
    Generate a Vedic astrology horoscope for a person born on {birth_datetime.strftime('%Y-%m-%d')} at {birth_datetime.strftime('%H:%M')} in {place_of_birth}. 
    Include the following aspects:
    1. Sun sign and Moon sign
    2. Rising sign (Ascendant)
    3. Planetary positions in houses
    4. Major life aspects (career, relationships, health)
    5. Current planetary transits and their effects
    6. Any specific influences based on the place of birth
    
    Provide a detailed and insightful horoscope based on Vedic astrology principles, taking into account the location of birth.
    """
    
    horoscope = send_openai_request(prompt)
    return horoscope
