import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
from typing import Dict, List, Tuple
import os

class VideoProcessor:
    def __init__(self):
        self.temp_dir = "uploads/temp"
        os.makedirs(self.temp_dir, exist_ok=True)
    
    async def extract_video_info(self, video_path: str) -> Dict:
        """Extract basic video information"""
        try:
            clip = VideoFileClip(video_path)
            
            return {
                "duration": clip.duration,
                "fps": clip.fps,
                "resolution": (clip.w, clip.h),
                "has_audio": clip.audio is not None,
                "size_mb": os.path.getsize(video_path) / (1024 * 1024)
            }
        except Exception as e:
            return {"error": str(e)}
    
    async def create_lip_sync_preview(self, video_path: str, audio_path: str) -> str:
        """Create a lip-sync preview (basic implementation)"""
        try:
            # Load video and new audio
            video_clip = VideoFileClip(video_path)
            new_audio = AudioFileClip(audio_path)
            
            # Basic lip-sync (replace audio)
            final_video = video_clip.set_audio(new_audio)
            
            # Save preview
            output_path = f"{self.temp_dir}/preview_{os.path.basename(video_path)}"
            final_video.write_videofile(
                output_path,
                codec='libx264',
                audio_codec='aac',
                temp_audiofile='temp-audio.m4a',
                remove_temp=True
            )
            
            # Cleanup
            video_clip.close()
            new_audio.close()
            final_video.close()
            
            return output_path
            
        except Exception as e:
            print(f"Lip sync error: {e}")
            return None
    
    async def detect_speech_segments(self, video_path: str) -> List[Tuple[float, float]]:
        """Detect speech segments in video for better lip-sync"""
        try:
            clip = VideoFileClip(video_path)
            if not clip.audio:
                return []
            
            # Basic audio analysis (you'd want more sophisticated detection)
            audio_array = clip.audio.to_soundarray()
            
            # Simple volume-based segmentation
            segments = []
            threshold = np.percentile(np.abs(audio_array), 70)
            
            in_speech = False
            start_time = 0
            
            for i, frame in enumerate(audio_array):
                time_pos = i / clip.audio.fps
                volume = np.max(np.abs(frame))
                
                if volume > threshold and not in_speech:
                    start_time = time_pos
                    in_speech = True
                elif volume <= threshold and in_speech:
                    segments.append((start_time, time_pos))
                    in_speech = False
            
            clip.close()
            return segments
            
        except Exception as e:
            print(f"Speech detection error: {e}")
            return []
    
    async def optimize_for_social_media(self, video_path: str, platform: str = "reels") -> str:
        """Optimize video for social media platforms"""
        try:
            clip = VideoFileClip(video_path)
            
            # Platform-specific optimizations
            if platform.lower() in ["reels", "tiktok", "shorts"]:
                # Vertical format 9:16
                target_width, target_height = 1080, 1920
            else:
                # Square format 1:1
                target_width, target_height = 1080, 1080
            
            # Resize and crop to fit
            resized_clip = clip.resize(height=target_height)
            
            if resized_clip.w > target_width:
                # Center crop
                x_center = resized_clip.w // 2
                x1 = x_center - target_width // 2
                x2 = x_center + target_width // 2
                final_clip = resized_clip.crop(x1=x1, x2=x2)
            else:
                final_clip = resized_clip
            
            # Save optimized version
            output_path = f"{self.temp_dir}/optimized_{os.path.basename(video_path)}"
            final_clip.write_videofile(
                output_path,
                codec='libx264',
                bitrate='2000k',
                audio_codec='aac'
            )
            
            # Cleanup
            clip.close()
            resized_clip.close()
            final_clip.close()
            
            return output_path
            
        except Exception as e:
            print(f"Optimization error: {e}")
            return video_path