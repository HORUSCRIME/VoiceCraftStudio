from pydub import AudioSegment
from pydub.effects import normalize, compress_dynamic_range
import os
from typing import Dict

class AudioProcessor:
    def __init__(self):
        self.temp_dir = "uploads/temp"
        os.makedirs(self.temp_dir, exist_ok=True)
    
    async def enhance_audio(self, audio_path: str) -> str:
        """Enhance audio quality"""
        try:
            audio = AudioSegment.from_file(audio_path)
            
            # Normalize audio levels
            normalized_audio = normalize(audio)
            
            # Apply dynamic range compression
            compressed_audio = compress_dynamic_range(normalized_audio)
            
            # Adjust volume
            final_audio = compressed_audio + 3  # Boost by 3dB
            
            # Save enhanced version
            output_path = f"{self.temp_dir}/enhanced_{os.path.basename(audio_path)}"
            final_audio.export(output_path, format="mp3", bitrate="192k")
            
            return output_path
            
        except Exception as e:
            print(f"Audio enhancement error: {e}")
            return audio_path
    
    async def match_audio_duration(self, audio_path: str, target_duration: float) -> str:
        """Match audio duration to video"""
        try:
            audio = AudioSegment.from_file(audio_path)
            current_duration = len(audio) / 1000.0  # Convert to seconds
            
            if abs(current_duration - target_duration) < 0.5:
                return audio_path  # Already close enough
            
            if current_duration > target_duration:
                # Speed up audio slightly
                speed_factor = current_duration / target_duration
                faster_audio = audio.speedup(playback_speed=speed_factor)
                final_audio = faster_audio
            else:
                # Add silence at the end
                silence_duration = (target_duration - current_duration) * 1000
                silence = AudioSegment.silent(duration=int(silence_duration))
                final_audio = audio + silence
            
            # Save adjusted audio
            output_path = f"{self.temp_dir}/timed_{os.path.basename(audio_path)}"
            final_audio.export(output_path, format="mp3")
            
            return output_path
            
        except Exception as e:
            print(f"Audio timing error: {e}")
            return audio_path
    
    def get_audio_info(self, audio_path: str) -> Dict:
        """Get audio file information"""
        try:
            audio = AudioSegment.from_file(audio_path)
            
            return {
                "duration": len(audio) / 1000.0,
                "channels": audio.channels,
                "frame_rate": audio.frame_rate,
                "sample_width": audio.sample_width,
                "size_mb": os.path.getsize(audio_path) / (1024 * 1024)
            }
        except Exception as e:
            return {"error": str(e)}