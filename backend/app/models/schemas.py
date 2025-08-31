from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class VoicePersonality(str, Enum):
    SERIOUS = "serious"
    CASUAL = "casual"
    FUNNY = "funny"
    ENERGETIC = "energetic"
    CALM = "calm"

class Language(str, Enum):
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    ITALIAN = "it"
    PORTUGUESE = "pt"
    HINDI = "hi"
    JAPANESE = "ja"
    KOREAN = "ko"

class DubbingRequest(BaseModel):
    video_id: str
    voice_personality: VoicePersonality
    target_language: Language = Language.ENGLISH
    script_override: Optional[str] = None
    lip_sync: bool = True

class DubbingResponse(BaseModel):
    task_id: str
    status: str
    video_url: Optional[str] = None
    audio_url: Optional[str] = None
    message: str

class ProcessingStatus(BaseModel):
    task_id: str
    status: str
    progress: int
    current_step: str
    estimated_time: Optional[int] = None