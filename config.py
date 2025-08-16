import os


class Config:
    """Configuration class for the Flask application"""
    
    # Deepgram API Configuration
    DEEPGRAM_API_KEY: str = os.getenv('DEEPGRAM_API_KEY')
