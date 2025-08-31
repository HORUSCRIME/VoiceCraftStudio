# # # import google.generativeai as genai
# # # from app.config import settings
# # # import cv2
# # # import numpy as np
# # # from typing import List, Dict

# # # class GeminiClient:
# # #     def __init__(self):
# # #         genai.configure(api_key=settings.GEMINI_API_KEY)
# # #         self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
# # #     async def analyze_video_content(self, video_path: str) -> Dict:
# # #         """Analyze video content and generate script"""
# # #         try:
# # #             # Extract key frames from video
# # #             frames = self._extract_key_frames(video_path)
            
# # #             # Generate script based on video analysis
# # #             script_prompt = """
# # #             Analyze this video and create a compelling voiceover script. 
# # #             Consider:
# # #             1. Visual elements and actions
# # #             2. Mood and tone
# # #             3. Target audience (social media users)
# # #             4. Keep it engaging and concise (15-60 seconds max)
            
# # #             Return a natural, conversational script that matches the video content.
# # #             """
            
# # #             response = self.model.generate_content([script_prompt] + frames)
            
# # #             return {
# # #                 "script": response.text,
# # #                 "estimated_duration": self._estimate_duration(response.text),
# # #                 "key_moments": self._identify_key_moments(response.text)
# # #             }
            
# # #         except Exception as e:
# # #             print(f"Gemini analysis error: {e}")
# # #             return {
# # #                 "script": "Welcome to this amazing content! Let's dive right in.",
# # #                 "estimated_duration": 10,
# # #                 "key_moments": []
# # #             }
    
# # #     def _extract_key_frames(self, video_path: str, max_frames: int = 5) -> List:
# # #         """Extract key frames from video for analysis"""
# # #         cap = cv2.VideoCapture(video_path)
# # #         frames = []
# # #         total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
# # #         for i in range(max_frames):
# # #             frame_number = (total_frames // max_frames) * i
# # #             cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
# # #             ret, frame = cap.read()
            
# # #             if ret:
# # #                 # Convert to RGB and encode for Gemini
# # #                 frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# # #                 frames.append(frame_rgb)
        
# # #         cap.release()
# # #         return frames
    
# # #     def _estimate_duration(self, script: str) -> int:
# # #         """Estimate script duration in seconds"""
# # #         word_count = len(script.split())
# # #         # Average speaking rate: 150 words per minute
# # #         return max(5, int((word_count / 150) * 60))
    
# # #     def _identify_key_moments(self, script: str) -> List[Dict]:
# # #         """Identify key moments for lip sync"""
# # #         sentences = script.split('.')
# # #         moments = []
        
# # #         for i, sentence in enumerate(sentences):
# # #             if sentence.strip():
# # #                 moments.append({
# # #                     "timestamp": i * 3,  # Rough estimate
# # #                     "text": sentence.strip(),
# # #                     "emphasis": "high" if "!" in sentence else "normal"
# # #                 })
        
# # #         return moments

# # #     async def translate_script(self, script: str, target_language: str) -> str:
# # #         """Translate script to target language"""
# # #         try:
# # #             translation_prompt = f"""
# # #             Translate the following script to {target_language}, maintaining:
# # #             1. Natural flow and conversational tone
# # #             2. Cultural appropriateness
# # #             3. Similar duration when spoken
# # #             4. Emotional impact
            
# # #             Script: {script}
# # #             """
            
# # #             response = self.model.generate_content(translation_prompt)
# # #             return response.text
            
# # #         except Exception as e:
# # #             print(f"Translation error: {e}")
# # #             return script  # Return original if translation fails





# # import google.generativeai as genai
# # from app.config import settings
# # import cv2
# # import numpy as np
# # from PIL import Image
# # import io
# # import base64
# # from typing import List, Dict

# # class GeminiClient:
# #     def __init__(self):
# #         genai.configure(api_key=settings.GEMINI_API_KEY)
# #         self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
# #     async def analyze_video_content(self, video_path: str) -> Dict:
# #         """Analyze video content and generate script"""
# #         try:
# #             # Extract key frames from video
# #             frames = self._extract_key_frames(video_path)
            
# #             # Convert frames to PIL Images for Gemini
# #             pil_images = []
# #             for frame in frames:
# #                 if frame is not None:
# #                     # Convert BGR to RGB
# #                     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #                     # Convert to PIL Image
# #                     pil_image = Image.fromarray(rgb_frame)
# #                     pil_images.append(pil_image)
            
# #             # Generate script based on video analysis
# #             script_prompt = """
# #             Analyze this video and create a compelling voiceover script. 
# #             Consider:
# #             1. Visual elements and actions shown in the frames
# #             2. Mood and tone appropriate for the content
# #             3. Target audience (social media users)
# #             4. Keep it engaging and concise (15-60 seconds max)
            
# #             Return a natural, conversational script that matches the video content.
# #             Make it sound like a human narrator describing what's happening.
# #             """
            
# #             # Create content list with prompt and images
# #             content = [script_prompt] + pil_images
            
# #             if pil_images:
# #                 response = self.model.generate_content(content)
# #                 script = response.text
# #             else:
# #                 # Fallback if no frames could be extracted
# #                 script = "Welcome to this amazing content! Let's explore what we have here."
            
# #             return {
# #                 "script": script,
# #                 "estimated_duration": self._estimate_duration(script),
# #                 "key_moments": self._identify_key_moments(script)
# #             }
            
# #         except Exception as e:
# #             print(f"Gemini analysis error: {e}")
# #             # Return a default script if analysis fails
# #             return {
# #                 "script": "Welcome to this amazing video! Today we're going to explore something really interesting. Let's dive right in and see what we can discover together.",
# #                 "estimated_duration": 15,
# #                 "key_moments": [
# #                     {"timestamp": 0, "text": "Welcome to this amazing video!", "emphasis": "high"},
# #                     {"timestamp": 5, "text": "Let's dive right in", "emphasis": "normal"},
# #                     {"timestamp": 10, "text": "see what we can discover", "emphasis": "normal"}
# #                 ]
# #             }
    
# #     def _extract_key_frames(self, video_path: str, max_frames: int = 5) -> List:
# #         """Extract key frames from video for analysis"""
# #         cap = cv2.VideoCapture(video_path)
# #         frames = []
        
# #         if not cap.isOpened():
# #             print(f"Error: Could not open video file {video_path}")
# #             return frames
            
# #         total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
# #         if total_frames == 0:
# #             print(f"Error: Video has no frames {video_path}")
# #             cap.release()
# #             return frames
        
# #         # Extract frames at regular intervals
# #         for i in range(max_frames):
# #             if total_frames <= max_frames:
# #                 frame_number = i if i < total_frames else total_frames - 1
# #             else:
# #                 frame_number = (total_frames // max_frames) * i
            
# #             cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
# #             ret, frame = cap.read()
            
# #             if ret and frame is not None:
# #                 # Resize frame to reduce processing time and API payload
# #                 height, width = frame.shape[:2]
# #                 if width > 800:  # Resize if too large
# #                     scale = 800 / width
# #                     new_width = 800
# #                     new_height = int(height * scale)
# #                     frame = cv2.resize(frame, (new_width, new_height))
                
# #                 frames.append(frame)
# #             else:
# #                 print(f"Could not read frame {frame_number}")
        
# #         cap.release()
# #         return frames
    
# #     def _estimate_duration(self, script: str) -> int:
# #         """Estimate script duration in seconds"""
# #         word_count = len(script.split())
# #         # Average speaking rate: 150-180 words per minute, using 160
# #         duration_seconds = (word_count / 160) * 60
# #         return max(5, int(duration_seconds))  # Minimum 5 seconds
    
# #     def _identify_key_moments(self, script: str) -> List[Dict]:
# #         """Identify key moments for lip sync"""
# #         sentences = [s.strip() for s in script.split('.') if s.strip()]
# #         moments = []
        
# #         estimated_duration = self._estimate_duration(script)
# #         time_per_sentence = estimated_duration / len(sentences) if sentences else 1
        
# #         for i, sentence in enumerate(sentences):
# #             if sentence:
# #                 moments.append({
# #                     "timestamp": i * time_per_sentence,
# #                     "text": sentence,
# #                     "emphasis": "high" if ("!" in sentence or "?" in sentence) else "normal"
# #                 })
        
# #         return moments

# #     async def translate_script(self, script: str, target_language: str) -> str:
# #         """Translate script to target language"""
# #         try:
# #             # Map language codes to full names
# #             language_names = {
# #                 "es": "Spanish",
# #                 "fr": "French", 
# #                 "de": "German",
# #                 "it": "Italian",
# #                 "pt": "Portuguese",
# #                 "hi": "Hindi",
# #                 "ja": "Japanese",
# #                 "ko": "Korean"
# #             }
            
# #             language_name = language_names.get(target_language, target_language)
            
# #             translation_prompt = f"""
# #             Translate the following script to {language_name}, maintaining:
# #             1. Natural flow and conversational tone
# #             2. Cultural appropriateness for {language_name} speakers
# #             3. Similar duration when spoken aloud
# #             4. Emotional impact and enthusiasm
# #             5. Keep it suitable for social media content
            
# #             Original script: "{script}"
            
# #             Provide only the translated text, nothing else.
# #             """
            
# #             response = self.model.generate_content(translation_prompt)
# #             return response.text.strip()
            
# #         except Exception as e:
# #             print(f"Translation error: {e}")
# #             return script  # Return original if translation fails





# import google.generativeai as genai
# from app.config import settings
# import cv2
# import numpy as np
# from typing import List, Dict
# import tempfile
# import os

# class GeminiClient:
#     def __init__(self):
#         genai.configure(api_key=settings.GEMINI_API_KEY)
#         self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
#     async def analyze_video_content(self, video_path: str) -> Dict:
#         """Analyze video content and generate script"""
#         try:
#             # Extract key frames from video and save as image files
#             frame_paths = self._extract_and_save_frames(video_path)
            
#             # Generate script based on video analysis
#             script_prompt = """
#             Analyze the visual content and create a compelling voiceover script. 
#             Consider:
#             1. Visual elements and actions you can observe
#             2. Mood and tone appropriate for social media content
#             3. Target audience (social media users aged 18-35)
#             4. Keep it engaging and concise (15-60 seconds when spoken)
#             5. Make it sound natural and conversational
            
#             Create a script that would work well as a voiceover for this video content.
#             Focus on being engaging and describing what viewers would find interesting.
#             """
            
#             # For now, let's use text-only analysis since image processing has issues
#             # In production, you would upload the frame images to Gemini
#             response = self.model.generate_content(script_prompt)
#             script = response.text.strip()
            
#             # Clean up temporary files
#             for path in frame_paths:
#                 try:
#                     os.remove(path)
#                 except:
#                     pass
            
#             return {
#                 "script": script,
#                 "estimated_duration": self._estimate_duration(script),
#                 "key_moments": self._identify_key_moments(script)
#             }
            
#         except Exception as e:
#             print(f"Gemini analysis error: {e}")
#             # Return a default script if analysis fails
#             return {
#                 "script": "Welcome to this incredible video! Get ready for something amazing that's about to unfold. This content is going to capture your attention and keep you engaged from start to finish. Let's dive into this exciting journey together!",
#                 "estimated_duration": 18,
#                 "key_moments": [
#                     {"timestamp": 0, "text": "Welcome to this incredible video!", "emphasis": "high"},
#                     {"timestamp": 6, "text": "Get ready for something amazing", "emphasis": "high"},
#                     {"timestamp": 12, "text": "Let's dive into this exciting journey", "emphasis": "normal"}
#                 ]
#             }
    
#     def _extract_and_save_frames(self, video_path: str, max_frames: int = 3) -> List[str]:
#         """Extract key frames from video and save as temporary files"""
#         cap = cv2.VideoCapture(video_path)
#         frame_paths = []
        
#         if not cap.isOpened():
#             print(f"Error: Could not open video file {video_path}")
#             return frame_paths
            
#         total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
#         if total_frames == 0:
#             print(f"Error: Video has no frames {video_path}")
#             cap.release()
#             return frame_paths
        
#         # Extract frames at regular intervals
#         for i in range(max_frames):
#             if total_frames <= max_frames:
#                 frame_number = i if i < total_frames else total_frames - 1
#             else:
#                 frame_number = (total_frames // max_frames) * i
            
#             cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
#             ret, frame = cap.read()
            
#             if ret and frame is not None:
#                 # Create temporary file for the frame
#                 temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
#                 temp_path = temp_file.name
#                 temp_file.close()
                
#                 # Resize frame to reduce file size
#                 height, width = frame.shape[:2]
#                 if width > 800:
#                     scale = 800 / width
#                     new_width = 800
#                     new_height = int(height * scale)
#                     frame = cv2.resize(frame, (new_width, new_height))
                
#                 # Save frame as JPEG
#                 cv2.imwrite(temp_path, frame)
#                 frame_paths.append(temp_path)
        
#         cap.release()
#         return frame_paths
    
#     def _estimate_duration(self, script: str) -> int:
#         """Estimate script duration in seconds"""
#         word_count = len(script.split())
#         # Average speaking rate: 150-180 words per minute, using 160
#         duration_seconds = (word_count / 160) * 60
#         return max(5, int(duration_seconds))  # Minimum 5 seconds
    
#     def _identify_key_moments(self, script: str) -> List[Dict]:
#         """Identify key moments for lip sync"""
#         sentences = [s.strip() for s in script.split('.') if s.strip()]
#         moments = []
        
#         estimated_duration = self._estimate_duration(script)
#         time_per_sentence = estimated_duration / len(sentences) if sentences else 1
        
#         for i, sentence in enumerate(sentences):
#             if sentence:
#                 moments.append({
#                     "timestamp": i * time_per_sentence,
#                     "text": sentence,
#                     "emphasis": "high" if ("!" in sentence or "?" in sentence) else "normal"
#                 })
        
#         return moments

#     async def translate_script(self, script: str, target_language: str) -> str:
#         """Translate script to target language"""
#         try:
#             # Map language codes to full names
#             language_names = {
#                 "es": "Spanish",
#                 "fr": "French", 
#                 "de": "German",
#                 "it": "Italian",
#                 "pt": "Portuguese",
#                 "hi": "Hindi",
#                 "ja": "Japanese",
#                 "ko": "Korean"
#             }
            
#             language_name = language_names.get(target_language, target_language)
            
#             translation_prompt = f"""
#             Translate the following script to {language_name}, maintaining:
#             1. Natural flow and conversational tone
#             2. Cultural appropriateness for {language_name} speakers
#             3. Similar duration when spoken aloud
#             4. Emotional impact and enthusiasm
#             5. Keep it suitable for social media content
            
#             Original script: "{script}"
            
#             Provide only the translated text, nothing else.
#             """
            
#             response = self.model.generate_content(translation_prompt)
#             return response.text.strip()
            
#         except Exception as e:
#             print(f"Translation error: {e}")
#             return script  # Return original if translation fails



import google.generativeai as genai
from app.config import settings
import cv2
import numpy as np
from typing import List, Dict
import tempfile
import os


class GeminiClient:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')

    # async def analyze_video_content(self, video_path: str) -> Dict:
    #     """Analyze video content and generate script"""
    #     try:
    #         # Extract key frames (not sent yet, just for possible future use/logging)
    #         frame_paths = self._extract_and_save_frames(video_path)

    #         script_prompt = """
    #         Analyze the visual content and create a compelling voiceover script. 
    #         Consider:
    #         1. Visual elements and actions you can observe
    #         2. Mood and tone appropriate for social media content
    #         3. Target audience (social media users aged 18-35)
    #         4. Keep it engaging and concise (15-60 seconds when spoken)
    #         5. Make it sound natural and conversational

    #         Create a script that would work well as a voiceover for this video content.
    #         Focus on being engaging and describing what viewers would find interesting.
    #         """

    #         # Ask Gemini for script
    #         response = self.model.generate_content(script_prompt)

    #         # Debug log Gemini response
    #         print("🔹 Gemini raw response:", response)

    #         # Parse response safely
    #         script = self._extract_text_from_response(response)

    #         # Ensure non-empty script
    #         if not script or len(script.split()) < 3:
    #             script = "Welcome to this amazing video! Let's dive right in."

    #         # Cleanup temp frames
    #         for path in frame_paths:
    #             try:
    #                 os.remove(path)
    #             except Exception as e:
    #                 print(f"⚠️ Failed to delete temp frame {path}: {e}")

    #         return {
    #             "script": script,
    #             "estimated_duration": self._estimate_duration(script),
    #             "key_moments": self._identify_key_moments(script)
    #         }

    #     except Exception as e:
    #         print(f"❌ Gemini analysis error: {e}")
    #         # Fallback script so Murf always has something
    #         return {
    #             "script": "Welcome to this incredible video! Get ready for something amazing. Let's dive into this exciting journey together!",
    #             "estimated_duration": 18,
    #             "key_moments": [
    #                 {"timestamp": 0, "text": "Welcome to this incredible video!", "emphasis": "high"},
    #                 {"timestamp": 6, "text": "Get ready for something amazing", "emphasis": "high"},
    #                 {"timestamp": 12, "text": "Let's dive into this exciting journey", "emphasis": "normal"}
    #             ]
    #         }

    async def analyze_video_content(self, video_path: str) -> Dict:
        "  ""Analyze video content and generate script"""
        try:
            # Extract key frames
            frame_paths = self._extract_and_save_frames(video_path)

            # Prepare prompt
            script_prompt = """
            Analyze the visual content of these frames and create a compelling voiceover script. 
            Consider:
            1. Visual elements and actions visible in the frames
            2. Mood and tone appropriate for social media content
            3. Target audience (social media users aged 18-35)
            4. Keep it engaging and concise (15-60 seconds when spoken)
            5. Make it sound natural and conversational

            Your output should be ONLY the voiceover script.
            """

            # Send both prompt and images to Gemini
            contents = [{"role": "user", "parts": [script_prompt]}]
            for frame in frame_paths:
                with open(frame, "rb") as f:
                    contents[0]["parts"].append({"mime_type": "image/jpeg", "data": f.read()})

            response = self.model.generate_content(contents)

            # Debug log
            print("🔹 Gemini raw response:", response)

            # Parse response
            script = self._extract_text_from_response(response)

            if not script or len(script.split()) < 3:
                script = "Welcome to this amazing video! Let's dive right in."

            # Cleanup
            for path in frame_paths:
                try:
                    os.remove(path)
                except Exception as e:
                    print(f"⚠️ Failed to delete temp frame {path}: {e}")

            return {
                "script": script,
                "estimated_duration": self._estimate_duration(script),
                "key_moments": self._identify_key_moments(script)
            }

        except Exception as e:
            print(f"❌ Gemini analysis error: {e}")
            return {
                "script": "Welcome to this incredible video! Get ready for something amazing. Let's dive into this exciting journey together!",
                "estimated_duration": 18,
                "key_moments": [
                    {"timestamp": 0, "text": "Welcome to this incredible video!", "emphasis": "high"},
                    {"timestamp": 6, "text": "Get ready for something amazing", "emphasis": "high"},
                    {"timestamp": 12, "text": "Let's dive into this exciting journey", "emphasis": "normal"}
                ]
            }


    def _extract_text_from_response(self, response) -> str:
        """Safely extract text from Gemini response"""
        try:
            if hasattr(response, "text") and response.text:
                return response.text.strip()
            elif hasattr(response, "candidates") and response.candidates:
                parts = response.candidates[0].content.parts
                return " ".join([p.text for p in parts if hasattr(p, "text")])
        except Exception as e:
            print(f"⚠️ Failed to parse Gemini response: {e}")
        return ""

    def _extract_and_save_frames(self, video_path: str, max_frames: int = 3) -> List[str]:
        """Extract key frames from video and save as temporary files"""
        cap = cv2.VideoCapture(video_path)
        frame_paths = []

        if not cap.isOpened():
            print(f"❌ Error: Could not open video file {video_path}")
            return frame_paths

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if total_frames == 0:
            print(f"❌ Error: Video has no frames {video_path}")
            cap.release()
            return frame_paths

        for i in range(max_frames):
            if total_frames <= max_frames:
                frame_number = i if i < total_frames else total_frames - 1
            else:
                frame_number = (total_frames // max_frames) * i

            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = cap.read()

            if ret and frame is not None:
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
                temp_path = temp_file.name
                temp_file.close()

                # Resize if too large
                height, width = frame.shape[:2]
                if width > 800:
                    scale = 800 / width
                    frame = cv2.resize(frame, (800, int(height * scale)))

                cv2.imwrite(temp_path, frame)
                frame_paths.append(temp_path)
            else:
                print(f"⚠️ Could not read frame {frame_number}")

        cap.release()
        return frame_paths

    def _estimate_duration(self, script: str) -> int:
        """Estimate script duration in seconds"""
        word_count = len(script.split())
        duration_seconds = (word_count / 160) * 60  # ~160 wpm
        return max(5, int(duration_seconds))

    def _identify_key_moments(self, script: str) -> List[Dict]:
        """Identify key moments for lip sync"""
        sentences = [s.strip() for s in script.split('.') if s.strip()]
        moments = []
        estimated_duration = self._estimate_duration(script)
        time_per_sentence = estimated_duration / len(sentences) if sentences else 1

        for i, sentence in enumerate(sentences):
            moments.append({
                "timestamp": i * time_per_sentence,
                "text": sentence,
                "emphasis": "high" if ("!" in sentence or "?" in sentence) else "normal"
            })

        return moments

    async def translate_script(self, script: str, target_language: str) -> str:
        """Translate script to target language"""
        try:
            language_names = {
                "es": "Spanish", "fr": "French", "de": "German",
                "it": "Italian", "pt": "Portuguese", "hi": "Hindi",
                "ja": "Japanese", "ko": "Korean"
            }
            language_name = language_names.get(target_language, target_language)

            translation_prompt = f"""
            Translate the following script to {language_name}, maintaining:
            1. Natural flow and conversational tone
            2. Cultural appropriateness for {language_name} speakers
            3. Similar duration when spoken aloud
            4. Emotional impact and enthusiasm
            5. Keep it suitable for social media content

            Original script: "{script}"

            Provide only the translated text, nothing else.
            """

            response = self.model.generate_content(translation_prompt)
            translated = self._extract_text_from_response(response)
            return translated if translated else script

        except Exception as e:
            print(f"❌ Translation error: {e}")
            return script
