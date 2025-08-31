import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MURF_API_KEY = os.getenv("MURF_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "100000000"))  # 100MB
    ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS", "mp4,avi,mov,mkv").split(",")
    
    # Murf API endpoints
    MURF_BASE_URL = "https://api.murf.ai/v1"
    MURF_TTS_ENDPOINT = f"{MURF_BASE_URL}/speech"
    MURF_DUBBING_ENDPOINT = f"{MURF_BASE_URL}/dubbing"
    
    # Supported languages
    SUPPORTED_LANGUAGES = {
        "en": "English",
        "es": "Spanish", 
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "hi": "Hindi",
        "ja": "Japanese",
        "ko": "Korean"
    }

settings = Settings()