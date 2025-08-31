# # import httpx
# # import asyncio
# # from typing import Dict, Optional
# # from app.config import settings
# # from app.models.schemas import VoicePersonality, Language

# # class MurfClient:
# #     def __init__(self):
# #         self.api_key = settings.MURF_API_KEY
# #         self.base_url = settings.MURF_BASE_URL
        
# #         # Voice personality mapping
# #         self.voice_mapping = {
# #             VoicePersonality.SERIOUS: "en-US-AriaNeural",
# #             VoicePersonality.CASUAL: "en-US-JennyNeural", 
# #             VoicePersonality.FUNNY: "en-US-GuyNeural",
# #             VoicePersonality.ENERGETIC: "en-US-JasonNeural",
# #             VoicePersonality.CALM: "en-US-SaraNeural"
# #         }
    
# #     async def generate_tts(self, script: str, personality: VoicePersonality, 
# #                           language: Language = Language.ENGLISH) -> Dict:
# #         """Generate text-to-speech audio"""
# #         try:
# #             voice_id = self._get_voice_for_personality(personality, language)
            
# #             payload = {
# #                 "text": script,
# #                 "voice_id": voice_id,
# #                 "speed": 1.0,
# #                 "pitch": 0,
# #                 "volume": 1.0,
# #                 "output_format": "mp3",
# #                 "sample_rate": 44100
# #             }
            
# #             headers = {
# #                 "Authorization": f"Bearer {self.api_key}",
# #                 "Content-Type": "application/json"
# #             }
            
# #             async with httpx.AsyncClient() as client:
# #                 response = await client.post(
# #                     f"{self.base_url}/speech",
# #                     json=payload,
# #                     headers=headers,
# #                     timeout=60.0
# #                 )
                
# #                 if response.status_code == 200:
# #                     result = response.json()
# #                     return {
# #                         "success": True,
# #                         "audio_url": result.get("audio_url"),
# #                         "duration": result.get("duration"),
# #                         "task_id": result.get("task_id")
# #                     }
# #                 else:
# #                     return {"success": False, "error": f"API Error: {response.status_code}"}
                    
# #         except Exception as e:
# #             return {"success": False, "error": str(e)}
    
# #     async def create_dubbing_job(self, video_path: str, script: str, 
# #                                personality: VoicePersonality, language: Language) -> Dict:
# #         """Create a dubbing job with lip-sync"""
# #         try:
# #             voice_id = self._get_voice_for_personality(personality, language)
            
# #             # Upload video first
# #             upload_result = await self._upload_video(video_path)
# #             if not upload_result["success"]:
# #                 return upload_result
            
# #             payload = {
# #                 "video_url": upload_result["video_url"],
# #                 "script": script,
# #                 "voice_id": voice_id,
# #                 "lip_sync": True,
# #                 "auto_timing": True,
# #                 "language": language.value
# #             }
            
# #             headers = {
# #                 "Authorization": f"Bearer {self.api_key}",
# #                 "Content-Type": "application/json"
# #             }
            
# #             async with httpx.AsyncClient() as client:
# #                 response = await client.post(
# #                     f"{self.base_url}/dubbing",
# #                     json=payload,
# #                     headers=headers,
# #                     timeout=120.0
# #                 )
                
# #                 if response.status_code == 200:
# #                     result = response.json()
# #                     return {
# #                         "success": True,
# #                         "task_id": result.get("task_id"),
# #                         "status": "processing"
# #                     }
# #                 else:
# #                     return {"success": False, "error": f"Dubbing API Error: {response.status_code}"}
                    
# #         except Exception as e:
# #             return {"success": False, "error": str(e)}
    
# #     async def check_dubbing_status(self, task_id: str) -> Dict:
# #         """Check dubbing job status"""
# #         try:
# #             headers = {"Authorization": f"Bearer {self.api_key}"}
            
# #             async with httpx.AsyncClient() as client:
# #                 response = await client.get(
# #                     f"{self.base_url}/dubbing/{task_id}/status",
# #                     headers=headers
# #                 )
                
# #                 if response.status_code == 200:
# #                     return response.json()
# #                 else:
# #                     return {"success": False, "error": "Status check failed"}
                    
# #         except Exception as e:
# #             return {"success": False, "error": str(e)}
    
# #     async def _upload_video(self, video_path: str) -> Dict:
# #         """Upload video to Murf platform"""
# #         try:
# #             headers = {"Authorization": f"Bearer {self.api_key}"}
            
# #             async with httpx.AsyncClient() as client:
# #                 with open(video_path, 'rb') as video_file:
# #                     files = {"video": video_file}
# #                     response = await client.post(
# #                         f"{self.base_url}/upload",
# #                         files=files,
# #                         headers=headers,
# #                         timeout=300.0
# #                     )
                    
# #                 if response.status_code == 200:
# #                     result = response.json()
# #                     return {
# #                         "success": True,
# #                         "video_url": result.get("url"),
# #                         "video_id": result.get("id")
# #                     }
# #                 else:
# #                     return {"success": False, "error": "Upload failed"}
                    
# #         except Exception as e:
# #             return {"success": False, "error": str(e)}
    
# #     def _get_voice_for_personality(self, personality: VoicePersonality, language: Language) -> str:
# #         """Get appropriate voice ID for personality and language"""
# #         # This would typically map to actual Murf voice IDs
# #         voice_map = {
# #             (VoicePersonality.SERIOUS, Language.ENGLISH): "aria_serious_en",
# #             (VoicePersonality.CASUAL, Language.ENGLISH): "jenny_casual_en",
# #             (VoicePersonality.FUNNY, Language.ENGLISH): "guy_funny_en",
# #             (VoicePersonality.ENERGETIC, Language.ENGLISH): "jason_energetic_en",
# #             (VoicePersonality.CALM, Language.ENGLISH): "sara_calm_en",
# #             # Add more combinations as needed
# #         }
        
# #         return voice_map.get((personality, language), "aria_serious_en")





# import httpx
# import asyncio
# import os
# import aiofiles
# from typing import Dict, Optional
# from app.config import settings
# from app.models.schemas import VoicePersonality, Language

# class MurfClient:
#     def __init__(self):
#         self.api_key = settings.MURF_API_KEY
#         # Correct Murf API base URL
#         self.base_url = "https://api.murf.ai/v1"
        
#         # Actual Murf voice IDs (these need to be updated with real Murf voice IDs)
#         self.voice_mapping = {
#             VoicePersonality.SERIOUS: {
#                 Language.ENGLISH: "en-US_Aria_Premium",
#                 Language.SPANISH: "es-ES_Paloma_Premium", 
#                 Language.FRENCH: "fr-FR_Lea_Premium",
#                 Language.GERMAN: "de-DE_Petra_Premium",
#                 Language.HINDI: "hi-IN_Aditi_Premium",
#             },
#             VoicePersonality.CASUAL: {
#                 Language.ENGLISH: "en-US_Jenny_Premium",
#                 Language.SPANISH: "es-ES_Diego_Premium",
#                 Language.FRENCH: "fr-FR_Thomas_Premium", 
#                 Language.GERMAN: "de-DE_Conrad_Premium",
#                 Language.HINDI: "hi-IN_Ravi_Premium",
#             },
#             VoicePersonality.FUNNY: {
#                 Language.ENGLISH: "en-US_Guy_Premium",
#                 Language.SPANISH: "es-ES_Sofia_Premium",
#                 Language.FRENCH: "fr-FR_Henri_Premium",
#                 Language.GERMAN: "de-DE_Klaus_Premium", 
#                 Language.HINDI: "hi-IN_Kavya_Premium",
#             },
#             VoicePersonality.ENERGETIC: {
#                 Language.ENGLISH: "en-US_Jason_Premium",
#                 Language.SPANISH: "es-ES_Pablo_Premium",
#                 Language.FRENCH: "fr-FR_Antoine_Premium",
#                 Language.GERMAN: "de-DE_Stefan_Premium",
#                 Language.HINDI: "hi-IN_Arnab_Premium",
#             },
#             VoicePersonality.CALM: {
#                 Language.ENGLISH: "en-US_Sara_Premium",
#                 Language.SPANISH: "es-ES_Elena_Premium", 
#                 Language.FRENCH: "fr-FR_Celine_Premium",
#                 Language.GERMAN: "de-DE_Marlene_Premium",
#                 Language.HINDI: "hi-IN_Priya_Premium",
#             }
#         }
    
#     async def generate_tts(self, script: str, personality: VoicePersonality, 
#                           language: Language = Language.ENGLISH) -> Dict:
#         """Generate text-to-speech audio using Murf API"""
#         try:
#             voice_id = self._get_voice_for_personality(personality, language)
            
#             # Murf API payload structure
#             payload = {
#                 "voiceId": voice_id,
#                 "text": script,
#                 "format": "MP3",
#                 "sampleRate": "44100",
#                 "speed": "0",  # Murf uses -50 to +50 range
#                 "pitch": "0",  # Murf uses -50 to +50 range
#                 "emphasis": "0",
#                 "pronunciation": "default"
#             }
            
#             headers = {
#                 "accept": "application/json",
#                 "content-type": "application/json",
#                 "api-key": self.api_key  # Murf uses 'api-key' header
#             }
            
#             async with httpx.AsyncClient(timeout=60.0) as client:
#                 response = await client.post(
#                     f"{self.base_url}/speech/generate",
#                     json=payload,
#                     headers=headers
#                 )
                
#                 if response.status_code == 200:
#                     result = response.json()
                    
#                     # Download the audio file
#                     audio_url = result.get("audioFile")
#                     if audio_url:
#                         audio_path = await self._download_audio(audio_url)
#                         return {
#                             "success": True,
#                             "audio_path": audio_path,
#                             "audio_url": audio_url,
#                             "duration": result.get("duration"),
#                             "task_id": result.get("id")
#                         }
#                     else:
#                         return {"success": False, "error": "No audio URL in response"}
                        
#                 elif response.status_code == 401:
#                     return {"success": False, "error": "Invalid API key"}
#                 elif response.status_code == 429:
#                     return {"success": False, "error": "Rate limit exceeded"}
#                 else:
#                     error_detail = response.text
#                     return {"success": False, "error": f"API Error {response.status_code}: {error_detail}"}
                    
#         except httpx.TimeoutException:
#             return {"success": False, "error": "Request timed out"}
#         except Exception as e:
#             return {"success": False, "error": f"TTS Generation failed: {str(e)}"}
    
#     async def _download_audio(self, audio_url: str) -> str:
#         """Download generated audio file"""
#         try:
#             # Create unique filename
#             import uuid
#             filename = f"generated_{uuid.uuid4().hex}.mp3"
#             file_path = os.path.join("uploads", "audio", filename)
            
#             # Ensure directory exists
#             os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
#             async with httpx.AsyncClient(timeout=30.0) as client:
#                 response = await client.get(audio_url)
#                 response.raise_for_status()
                
#                 async with aiofiles.open(file_path, 'wb') as f:
#                     await f.write(response.content)
            
#             return file_path
            
#         except Exception as e:
#             print(f"Audio download failed: {e}")
#             return None
    
#     async def create_dubbing_job(self, video_path: str, script: str, 
#                                personality: VoicePersonality, language: Language) -> Dict:
#         """Create a dubbing job - Murf doesn't have direct dubbing API, so simulate with TTS + video processing"""
#         try:
#             # Generate TTS first
#             tts_result = await self.generate_tts(script, personality, language)
            
#             if not tts_result["success"]:
#                 return tts_result
            
#             # For now, return success - actual video+audio combination would be handled by video_processor
#             return {
#                 "success": True,
#                 "task_id": tts_result.get("task_id"),
#                 "audio_path": tts_result.get("audio_path"),
#                 "status": "completed"
#             }
                    
#         except Exception as e:
#             return {"success": False, "error": f"Dubbing failed: {str(e)}"}
    
#     async def get_available_voices(self, language: Language = Language.ENGLISH) -> Dict:
#         """Get list of available voices for a language"""
#         try:
#             headers = {
#                 "accept": "application/json",
#                 "api-key": self.api_key
#             }
            
#             # Map our language enum to Murf language codes
#             murf_lang_map = {
#                 Language.ENGLISH: "en-US",
#                 Language.SPANISH: "es-ES", 
#                 Language.FRENCH: "fr-FR",
#                 Language.GERMAN: "de-DE",
#                 Language.HINDI: "hi-IN",
#                 Language.JAPANESE: "ja-JP",
#                 Language.KOREAN: "ko-KR",
#                 Language.ITALIAN: "it-IT",
#                 Language.PORTUGUESE: "pt-BR"
#             }
            
#             lang_code = murf_lang_map.get(language, "en-US")
            
#             async with httpx.AsyncClient(timeout=30.0) as client:
#                 response = await client.get(
#                     f"{self.base_url}/speech/voices",
#                     headers=headers,
#                     params={"language": lang_code}
#                 )
                
#                 if response.status_code == 200:
#                     return {"success": True, "voices": response.json()}
#                 else:
#                     return {"success": False, "error": f"Failed to get voices: {response.status_code}"}
                    
#         except Exception as e:
#             return {"success": False, "error": f"Voice list failed: {str(e)}"}
    
#     def _get_voice_for_personality(self, personality: VoicePersonality, language: Language) -> str:
#         """Get appropriate voice ID for personality and language"""
#         voice_map = self.voice_mapping.get(personality, {})
#         return voice_map.get(language, "en-US_Aria_Premium")  # Default fallback
    
#     async def test_api_connection(self) -> Dict:
#         """Test if API key and connection work"""
#         try:
#             headers = {
#                 "accept": "application/json", 
#                 "api-key": self.api_key
#             }
            
#             async with httpx.AsyncClient(timeout=10.0) as client:
#                 response = await client.get(
#                     f"{self.base_url}/speech/voices",
#                     headers=headers,
#                     params={"language": "en-US"}
#                 )
                
#                 if response.status_code == 200:
#                     return {"success": True, "message": "Murf API connection successful"}
#                 elif response.status_code == 401:
#                     return {"success": False, "error": "Invalid API key"}
#                 else:
#                     return {"success": False, "error": f"API test failed: {response.status_code}"}
                    
#         except Exception as e:
#             return {"success": False, "error": f"Connection test failed: {str(e)}"}




import httpx
import asyncio
import os
import aiofiles
from typing import Dict, Optional
from app.config import settings
from app.models.schemas import VoicePersonality, Language

class MurfClient:
    def __init__(self):
        self.api_key = settings.MURF_API_KEY
        # Correct Murf API base URL
        self.base_url = "https://api.murf.ai/v1"
        
        # Real Murf voice IDs - these are common ones that should work
        self.voice_mapping = {
            VoicePersonality.SERIOUS: {
                Language.ENGLISH: "en-US-ariana",
                Language.SPANISH: "es-ES-elvira", 
                Language.FRENCH: "fr-FR-maxime",
                Language.GERMAN: "de-DE-matthias",
                Language.HINDI: "hi-IN-kabir",
            },
            VoicePersonality.CASUAL: {
                Language.ENGLISH: "en-US-jayden",
                Language.SPANISH: "es-ES-carmen",
                Language.FRENCH: "fr-FR-adélie", 
                Language.GERMAN: "de-DE-lia",
                Language.HINDI: "hi-IN-ayushi",
            },
            VoicePersonality.FUNNY: {
                Language.ENGLISH: "en-US-josie",
                Language.SPANISH: "es-ES-carla",
                Language.FRENCH: "fr-FR-axel",
                Language.GERMAN: "de-DE-björn", 
                Language.HINDI: "hi-IN-shaan",
            },
            VoicePersonality.ENERGETIC: {
                Language.ENGLISH: "en-US-river",
                Language.SPANISH: "es-ES-javier",
                Language.FRENCH: "fr-FR-justine",
                Language.GERMAN: "de-DE-erna",
                Language.HINDI: "hi-IN-shweta",
            },
            VoicePersonality.CALM: {
                Language.ENGLISH: "en-UK-pearl",
                Language.SPANISH: "es-ES-enrique", 
                Language.FRENCH: "fr-FR-louise",
                Language.GERMAN: "de-DE-josephine",
                Language.HINDI: "hi-IN-amit",
            }
        }
    
    async def generate_tts(self, script: str, personality: VoicePersonality, 
                          language: Language = Language.ENGLISH) -> Dict:
        """Generate text-to-speech audio using Murf API"""
        try:
            # First, try to get a valid voice ID
            voice_id = await self._get_valid_voice_id(personality, language)
            
            # Murf API payload structure
            payload = {
                "voiceId": voice_id,
                "text": script,
                "format": "MP3",
                "sampleRate": "44100",
                "speed": "0",  # Murf uses -50 to +50 range
                "pitch": "0",  # Murf uses -50 to +50 range
                "emphasis": "0",
                "pronunciation": "default"
            }
            
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "api-key": self.api_key  # Murf uses 'api-key' header
            }
            
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    f"{self.base_url}/speech/generate",
                    json=payload,
                    headers=headers
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Download the audio file
                    audio_url = result.get("audioFile")
                    if audio_url:
                        audio_path = await self._download_audio(audio_url)
                        return {
                            "success": True,
                            "audio_path": audio_path,
                            "audio_url": audio_url,
                            "duration": result.get("duration"),
                            "task_id": result.get("id")
                        }
                    else:
                        return {"success": False, "error": "No audio URL in response"}
                        
                elif response.status_code == 401:
                    return {"success": False, "error": "Invalid API key"}
                elif response.status_code == 429:
                    return {"success": False, "error": "Rate limit exceeded"}
                else:
                    error_detail = response.text
                    return {"success": False, "error": f"API Error {response.status_code}: {error_detail}"}
                    
        except httpx.TimeoutException:
            return {"success": False, "error": "Request timed out"}
        except Exception as e:
            return {"success": False, "error": f"TTS Generation failed: {str(e)}"}
    
    async def _get_valid_voice_id(self, personality: VoicePersonality, language: Language) -> str:
        """Get a valid voice ID by checking available voices"""
        try:
            # First try our predefined mapping
            voice_map = self.voice_mapping.get(personality, {})
            preferred_voice = voice_map.get(language)
            
            # Get available voices to validate
            voices_result = await self.get_available_voices(language)
            
            if voices_result.get("success") and voices_result.get("voices"):
                available_voices = voices_result["voices"].get("voices", [])
                
                # Try to find our preferred voice
                if preferred_voice:
                    for voice in available_voices:
                        if voice.get("id") == preferred_voice:
                            return preferred_voice
                
                # If preferred not found, pick first available voice for the language
                if available_voices:
                    return available_voices[0].get("id")
            
            # Ultimate fallback
            return self._get_voice_for_personality(personality, language)
            
        except Exception as e:
            print(f"Voice ID validation failed: {e}")
            return self._get_voice_for_personality(personality, language)
    
    async def _download_audio(self, audio_url: str) -> str:
        """Download generated audio file"""
        try:
            # Create unique filename
            import uuid
            filename = f"generated_{uuid.uuid4().hex}.mp3"
            file_path = os.path.join("uploads", "audio", filename)
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(audio_url)
                response.raise_for_status()
                
                async with aiofiles.open(file_path, 'wb') as f:
                    await f.write(response.content)
            
            return file_path
            
        except Exception as e:
            print(f"Audio download failed: {e}")
            return None
    
    async def create_dubbing_job(self, video_path: str, script: str, 
                               personality: VoicePersonality, language: Language) -> Dict:
        """Create a dubbing job - Murf doesn't have direct dubbing API, so simulate with TTS + video processing"""
        try:
            # Generate TTS first
            tts_result = await self.generate_tts(script, personality, language)
            
            if not tts_result["success"]:
                return tts_result
            
            # For now, return success - actual video+audio combination would be handled by video_processor
            return {
                "success": True,
                "task_id": tts_result.get("task_id"),
                "audio_path": tts_result.get("audio_path"),
                "status": "completed"
            }
                    
        except Exception as e:
            return {"success": False, "error": f"Dubbing failed: {str(e)}"}
    
    async def get_available_voices(self, language: Language = Language.ENGLISH) -> Dict:
        """Get list of available voices for a language"""
        try:
            headers = {
                "accept": "application/json",
                "api-key": self.api_key
            }
            
            # Map our language enum to Murf language codes
            murf_lang_map = {
                Language.ENGLISH: "en-US",
                Language.SPANISH: "es-ES", 
                Language.FRENCH: "fr-FR",
                Language.GERMAN: "de-DE",
                Language.HINDI: "hi-IN",
                Language.JAPANESE: "ja-JP",
                Language.KOREAN: "ko-KR",
                Language.ITALIAN: "it-IT",
                Language.PORTUGUESE: "pt-BR"
            }
            
            lang_code = murf_lang_map.get(language, "en-US")
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(
                    f"{self.base_url}/speech/voices",
                    headers=headers,
                    params={"language": lang_code}
                )
                
                if response.status_code == 200:
                    return {"success": True, "voices": response.json()}
                else:
                    return {"success": False, "error": f"Failed to get voices: {response.status_code}"}
                    
        except Exception as e:
            return {"success": False, "error": f"Voice list failed: {str(e)}"}
    
    def _get_voice_for_personality(self, personality: VoicePersonality, language: Language) -> str:
        """Get appropriate voice ID for personality and language"""
        voice_map = self.voice_mapping.get(personality, {})
        voice_id = voice_map.get(language)
        
        if voice_id:
            return voice_id
            
        # Fallback to common voice patterns if specific mapping not found
        lang_code = {
            Language.ENGLISH: "en-US",
            Language.SPANISH: "es-ES",
            Language.FRENCH: "fr-FR",
            Language.GERMAN: "de-DE",
            Language.HINDI: "hi-IN",
            Language.JAPANESE: "ja-JP",
            Language.KOREAN: "ko-KR",
            Language.ITALIAN: "it-IT",
            Language.PORTUGUESE: "pt-BR"
        }.get(language, "en-US")
        
        # Try common voice names as fallbacks
        fallback_voices = [
            f"{lang_code}-aria",
            f"{lang_code}-jenny", 
            f"{lang_code}-guy",
            f"{lang_code}-sarah",
            f"{lang_code}-premium-1",
            f"{lang_code}-neural-1"
        ]
        
        # Return first fallback for now - in production you'd validate against API
        return fallback_voices[0]
    
    async def test_api_connection(self) -> Dict:
        """Test if API key and connection work"""
        try:
            headers = {
                "accept": "application/json", 
                "api-key": self.api_key
            }
            
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    f"{self.base_url}/speech/voices",
                    headers=headers,
                    params={"language": "en-US"}
                )
                
                if response.status_code == 200:
                    return {"success": True, "message": "Murf API connection successful"}
                elif response.status_code == 401:
                    return {"success": False, "error": "Invalid API key"}
                else:
                    return {"success": False, "error": f"API test failed: {response.status_code}"}
                    
        except Exception as e:
            return {"success": False, "error": f"Connection test failed: {str(e)}"}