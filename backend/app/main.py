# from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# import aiofiles
# import os
# import uuid
# from typing import Dict
# import asyncio

# from app.models.schemas import DubbingRequest, DubbingResponse, ProcessingStatus
# from app.services.gemini_client import GeminiClient
# from app.services.murf_client import MurfClient
# from app.services.video_processor import VideoProcessor
# from app.services.audio_processor import AudioProcessor
# from app.config import settings

# app = FastAPI(title="Voice Dubbing API", version="1.0.0")

# # CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # React frontend
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Static files
# app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# # Initialize services
# gemini_client = GeminiClient()
# murf_client = MurfClient()
# video_processor = VideoProcessor()
# audio_processor = AudioProcessor()

# # In-memory task storage (use Redis in production)
# tasks: Dict[str, Dict] = {}

# @app.post("/api/upload-video")
# async def upload_video(file: UploadFile = File(...)):
#     """Upload and validate video file"""
#     try:
#         # Validate file
#         if not file.filename:
#             raise HTTPException(status_code=400, detail="No file provided")
        
#         file_extension = file.filename.split('.')[-1].lower()
#         if file_extension not in settings.ALLOWED_EXTENSIONS:
#             raise HTTPException(
#                 status_code=400, 
#                 detail=f"Unsupported format. Allowed: {settings.ALLOWED_EXTENSIONS}"
#             )
        
#         # Generate unique filename
#         video_id = str(uuid.uuid4())
#         filename = f"{video_id}.{file_extension}"
#         file_path = os.path.join(settings.UPLOAD_DIR, "videos", filename)
        
#         # Ensure directory exists
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
#         # Save file
#         async with aiofiles.open(file_path, 'wb') as buffer:
#             content = await file.read()
#             if len(content) > settings.MAX_FILE_SIZE:
#                 raise HTTPException(status_code=413, detail="File too large")
#             await buffer.write(content)
        
#         # Extract video info
#         video_info = await video_processor.extract_video_info(file_path)
        
#         # Analyze content with Gemini
#         content_analysis = await gemini_client.analyze_video_content(file_path)
        
#         return {
#             "video_id": video_id,
#             "filename": file.filename,
#             "video_info": video_info,
#             "suggested_script": content_analysis["script"],
#             "estimated_duration": content_analysis["estimated_duration"]
#         }
        
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/api/generate-dubbing", response_model=DubbingResponse)
# async def generate_dubbing(request: DubbingRequest, background_tasks: BackgroundTasks):
#     """Generate voice dubbing for video"""
#     try:
#         task_id = str(uuid.uuid4())
#         video_path = os.path.join(settings.UPLOAD_DIR, "videos", f"{request.video_id}.mp4")
        
#         if not os.path.exists(video_path):
#             raise HTTPException(status_code=404, detail="Video not found")
        
#         # Initialize task
#         tasks[task_id] = {
#             "status": "starting",
#             "progress": 0,
#             "current_step": "Initializing...",
#             "video_id": request.video_id
#         }
        
#         # Start background processing
#         background_tasks.add_task(
#             process_dubbing_task,
#             task_id,
#             video_path,
#             request
#         )
        
#         return DubbingResponse(
#             task_id=task_id,
#             status="processing",
#             message="Dubbing generation started"
#         )
        
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/api/status/{task_id}", response_model=ProcessingStatus)
# async def get_processing_status(task_id: str):
#     """Get processing status"""
#     if task_id not in tasks:
#         raise HTTPException(status_code=404, detail="Task not found")
    
#     task = tasks[task_id]
    
#     return ProcessingStatus(
#         task_id=task_id,
#         status=task["status"],
#         progress=task["progress"],
#         current_step=task["current_step"],
#         estimated_time=task.get("estimated_time")
#     )

# @app.get("/api/download/{task_id}/{file_type}")
# async def download_file(task_id: str, file_type: str):
#     """Download processed files"""
#     if task_id not in tasks:
#         raise HTTPException(status_code=404, detail="Task not found")
    
#     task = tasks[task_id]
    
#     if task["status"] != "completed":
#         raise HTTPException(status_code=400, detail="Processing not completed")
    
#     if file_type == "video":
#         file_path = task.get("output_video_path")
#     elif file_type == "audio":
#         file_path = task.get("output_audio_path")
#     else:
#         raise HTTPException(status_code=400, detail="Invalid file type")
    
#     if not file_path or not os.path.exists(file_path):
#         raise HTTPException(status_code=404, detail="File not found")
    
#     return FileResponse(file_path)

# @app.get("/api/languages")
# async def get_supported_languages():
#     """Get supported languages"""
#     return {"languages": settings.SUPPORTED_LANGUAGES}

# async def process_dubbing_task(task_id: str, video_path: str, request: DubbingRequest):
#     """Background task for processing dubbing"""
#     try:
#         # Step 3: Generate TTS audio
#         tasks[task_id].update({
#             "progress": 40,
#             "current_step": "Generating voiceover..."
#         })
        
#         tts_result = await murf_client.generate_tts(
#             script, 
#             request.voice_personality, 
#             request.target_language
#         )
        
#         if not tts_result["success"]:
#             tasks[task_id].update({
#                 "status": "failed",
#                 "error": tts_result["error"]
#             })
#             return
        
#         # Step 4: Process and enhance audio
#         tasks[task_id].update({
#             "progress": 60,
#             "current_step": "Processing audio..."
#         })
        
#         # Download generated audio (simulated)
#         audio_path = f"uploads/audio/{task_id}.mp3"
#         # In real implementation, download from tts_result["audio_url"]
        
#         enhanced_audio_path = await audio_processor.enhance_audio(audio_path)
        
#         # Step 5: Create lip-sync preview
#         if request.lip_sync:
#             tasks[task_id].update({
#                 "progress": 80,
#                 "current_step": "Creating lip-sync preview..."
#             })
            
#             video_info = await video_processor.extract_video_info(video_path)
#             timed_audio_path = await audio_processor.match_audio_duration(
#                 enhanced_audio_path, 
#                 video_info["duration"]
#             )
            
#             output_video_path = await video_processor.create_lip_sync_preview(
#                 video_path, 
#                 timed_audio_path
#             )
#         else:
#             output_video_path = video_path
#             timed_audio_path = enhanced_audio_path
        
#         # Step 6: Optimize for social media
#         tasks[task_id].update({
#             "progress": 90,
#             "current_step": "Optimizing for social media..."
#         })
        
#         final_video_path = await video_processor.optimize_for_social_media(
#             output_video_path, 
#             "reels"
#         )
        
#         # Complete
#         tasks[task_id].update({
#             "status": "completed",
#             "progress": 100,
#             "current_step": "Processing complete!",
#             "output_video_path": final_video_path,
#             "output_audio_path": timed_audio_path,
#             "script_used": script
#         })
        
#     except Exception as e:
#         tasks[task_id].update({
#             "status": "failed",
#             "error": str(e)
#         })

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)




from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import aiofiles
import os
import uuid
from typing import Dict
import asyncio

from app.models.schemas import DubbingRequest, DubbingResponse, ProcessingStatus
from app.services.gemini_client import GeminiClient
from app.services.murf_client import MurfClient
from app.services.video_processor import VideoProcessor
from app.services.audio_processor import AudioProcessor
from app.config import settings

# Create required directories on startup
def create_directories():
    """Create required directories if they don't exist"""
    directories = [
        "uploads",
        "uploads/videos", 
        "uploads/audio",
        "uploads/temp",
        "uploads/processed"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Directory created/verified: {directory}")

# Initialize directories before creating the app
create_directories()

app = FastAPI(title="Voice Dubbing API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:5173"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files - now safe to mount since directories exist
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Initialize services
# gemini_client = GeminiClient()
# murf_client = MurfClient()
# video_processor = VideoProcessor()
# audio_processor = AudioProcessor()
gemini_client = GeminiClient()
murf_client = MurfClient()  # Use mock for testing
video_processor = VideoProcessor()
audio_processor = AudioProcessor()
print(f"Initialized Murf client: {type(murf_client).__name__}")
# In-memory task storage (use Redis in production)
tasks: Dict[str, Dict] = {}

@app.on_event("startup")
async def startup_event():
    """Startup event handler"""
    print("🚀 Voice Dubbing API started successfully!")
    print(f"📁 Upload directory: {os.path.abspath('uploads')}")
    print(f"🔑 API keys configured: MURF={'✓' if settings.MURF_API_KEY else '✗'}, GEMINI={'✓' if settings.GEMINI_API_KEY else '✗'}")

@app.post("/api/upload-video")
async def upload_video(file: UploadFile = File(...)):
    """Upload and validate video file"""
    try:
        # Validate file
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")
        
        file_extension = file.filename.split('.')[-1].lower()
        if file_extension not in settings.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400, 
                detail=f"Unsupported format. Allowed: {settings.ALLOWED_EXTENSIONS}"
            )
        
        # Generate unique filename
        video_id = str(uuid.uuid4())
        filename = f"{video_id}.{file_extension}"
        file_path = os.path.join(settings.UPLOAD_DIR, "videos", filename)
        
        # Ensure directory exists (double-check)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Save file
        async with aiofiles.open(file_path, 'wb') as buffer:
            content = await file.read()
            if len(content) > settings.MAX_FILE_SIZE:
                raise HTTPException(status_code=413, detail="File too large")
            await buffer.write(content)
        
        # Extract video info
        video_info = await video_processor.extract_video_info(file_path)
        
        # Analyze content with Gemini
        content_analysis = await gemini_client.analyze_video_content(file_path)
        
        return {
            "video_id": video_id,
            "filename": file.filename,
            "video_info": video_info,
            "suggested_script": content_analysis["script"],
            "estimated_duration": content_analysis["estimated_duration"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-dubbing", response_model=DubbingResponse)
async def generate_dubbing(request: DubbingRequest, background_tasks: BackgroundTasks):
    """Generate voice dubbing for video"""
    try:
        task_id = str(uuid.uuid4())
        
        # Look for video file with any supported extension
        video_path = None
        for ext in settings.ALLOWED_EXTENSIONS:
            potential_path = os.path.join(settings.UPLOAD_DIR, "videos", f"{request.video_id}.{ext}")
            if os.path.exists(potential_path):
                video_path = potential_path
                break
        
        if not video_path:
            raise HTTPException(status_code=404, detail="Video not found")
        
        # Initialize task
        tasks[task_id] = {
            "status": "starting",
            "progress": 0,
            "current_step": "Initializing...",
            "video_id": request.video_id
        }
        
        # Start background processing
        background_tasks.add_task(
            process_dubbing_task,
            task_id,
            video_path,
            request
        )
        
        return DubbingResponse(
            task_id=task_id,
            status="processing",
            message="Dubbing generation started"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/status/{task_id}", response_model=ProcessingStatus)
async def get_processing_status(task_id: str):
    """Get processing status"""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks[task_id]
    
    return ProcessingStatus(
        task_id=task_id,
        status=task["status"],
        progress=task["progress"],
        current_step=task["current_step"],
        estimated_time=task.get("estimated_time")
    )

@app.get("/api/download/{task_id}/{file_type}")
async def download_file(task_id: str, file_type: str):
    """Download processed files"""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks[task_id]
    
    if task["status"] != "completed":
        raise HTTPException(status_code=400, detail="Processing not completed")
    
    if file_type == "video":
        file_path = task.get("output_video_path")
    elif file_type == "audio":
        file_path = task.get("output_audio_path")
    else:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    if not file_path or not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(file_path)

@app.get("/api/languages")
async def get_supported_languages():
    """Get supported languages"""
    return {"languages": settings.SUPPORTED_LANGUAGES}

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "directories": {
            "uploads": os.path.exists("uploads"),
            "videos": os.path.exists("uploads/videos"),
            "audio": os.path.exists("uploads/audio"),
            "temp": os.path.exists("uploads/temp"),
            "processed": os.path.exists("uploads/processed")
        },
        "api_keys": {
            "murf": bool(settings.MURF_API_KEY),
            "gemini": bool(settings.GEMINI_API_KEY)
        }
    }

# async def process_dubbing_task(task_id: str, video_path: str, request: DubbingRequest):
#     """Background task for processing dubbing"""
#     try:
#         # Step 1: Analyze video content
#         tasks[task_id].update({
#             "status": "processing",
#             "progress": 10,
#             "current_step": "Analyzing video content..."
#         })
        
#         content_analysis = await gemini_client.analyze_video_content(video_path)
#         script = request.script_override or content_analysis["script"]
        
#         # Step 2: Translate if needed
#         if request.target_language != "en":
#             tasks[task_id].update({
#                 "progress": 25,
#                 "current_step": "Translating script..."
#             })
#             script = await gemini_client.translate_script(script, request.target_language.value)
        
#         # Step 3: Generate TTS audio
#         tasks[task_id].update({
#             "progress": 40,
#             "current_step": "Generating voiceover..."
#         })
        
#         tts_result = await murf_client.generate_tts(
#             script, 
#             request.voice_personality, 
#             request.target_language
#         )
        
#         if not tts_result["success"]:
#             tasks[task_id].update({
#                 "status": "failed",
#                 "error": tts_result["error"]
#             })
#             return
        
#         # Step 4: Process and enhance audio
#         tasks[task_id].update({
#             "progress": 60,
#             "current_step": "Processing audio..."
#         })
        
#         # Download generated audio (simulated for now)
#         audio_path = f"uploads/audio/{task_id}.mp3"
        
#         # Create a dummy audio file for testing
#         os.makedirs(os.path.dirname(audio_path), exist_ok=True)
#         with open(audio_path, 'w') as f:
#             f.write("")  # Create empty file for testing
        
#         enhanced_audio_path = await audio_processor.enhance_audio(audio_path)
        
#         # Step 5: Create lip-sync preview
#         if request.lip_sync:
#             tasks[task_id].update({
#                 "progress": 80,
#                 "current_step": "Creating lip-sync preview..."
#             })
            
#             video_info = await video_processor.extract_video_info(video_path)
#             timed_audio_path = await audio_processor.match_audio_duration(
#                 enhanced_audio_path, 
#                 video_info.get("duration", 10)
#             )
            
#             output_video_path = await video_processor.create_lip_sync_preview(
#                 video_path, 
#                 timed_audio_path
#             )
#         else:
#             output_video_path = video_path
#             timed_audio_path = enhanced_audio_path
        
#         # Step 6: Optimize for social media
#         tasks[task_id].update({
#             "progress": 90,
#             "current_step": "Optimizing for social media..."
#         })
        
#         final_video_path = await video_processor.optimize_for_social_media(
#             output_video_path or video_path, 
#             "reels"
#         )
        
#         # Complete
#         tasks[task_id].update({
#             "status": "completed",
#             "progress": 100,
#             "current_step": "Processing complete!",
#             "output_video_path": final_video_path or video_path,
#             "output_audio_path": timed_audio_path or audio_path,
#             "script_used": script
#         })
        
#     except Exception as e:
#         print(f"Processing error: {e}")
#         tasks[task_id].update({
#             "status": "failed",
#             "error": str(e)
#         })

async def process_dubbing_task(task_id: str, video_path: str, request: DubbingRequest):
    """Background task for processing dubbing"""
    try:
        print(f"🚀 Starting dubbing task {task_id}")
        
        # Step 1: Analyze video content
        tasks[task_id].update({
            "status": "processing",
            "progress": 10,
            "current_step": "Analyzing video content..."
        })
        
        content_analysis = await gemini_client.analyze_video_content(video_path)
        script = request.script_override or content_analysis["script"]
        
        print(f"📝 Generated script: {script[:100]}...")
        
        # Step 2: Translate if needed
        if request.target_language != "en":
            tasks[task_id].update({
                "progress": 25,
                "current_step": "Translating script..."
            })
            script = await gemini_client.translate_script(script, request.target_language.value)
            print(f"🌐 Translated script: {script[:100]}...")
        
        # Step 3: Generate TTS audio
        tasks[task_id].update({
            "progress": 40,
            "current_step": "Generating voiceover..."
        })
        
        print(f"🎙️ Generating TTS with Murf client: {type(murf_client).__name__}")
        
        tts_result = await murf_client.generate_tts(
            script, 
            request.voice_personality, 
            request.target_language
        )
        
        print(f"🔊 TTS result: {tts_result}")
        
        if not tts_result.get("success", False):
            error_msg = tts_result.get("error", "Unknown TTS error")
            print(f"❌ TTS failed: {error_msg}")
            tasks[task_id].update({
                "status": "failed",
                "error": f"Voice generation failed: {error_msg}"
            })
            return
        
        audio_path = tts_result.get("audio_path")
        if not audio_path or not os.path.exists(audio_path):
            print(f"❌ Audio file not found: {audio_path}")
            tasks[task_id].update({
                "status": "failed",
                "error": "Generated audio file not found"
            })
            return
        
        # Step 4: Process and enhance audio
        tasks[task_id].update({
            "progress": 60,
            "current_step": "Processing audio..."
        })
        
        try:
            enhanced_audio_path = await audio_processor.enhance_audio(audio_path)
            print(f"🎵 Enhanced audio: {enhanced_audio_path}")
        except Exception as e:
            print(f"⚠️ Audio enhancement failed, using original: {e}")
            enhanced_audio_path = audio_path
        
        # Step 5: Create lip-sync preview
        if request.lip_sync:
            tasks[task_id].update({
                "progress": 80,
                "current_step": "Creating lip-sync preview..."
            })
            
            try:
                video_info = await video_processor.extract_video_info(video_path)
                target_duration = video_info.get("duration", 10)
                
                timed_audio_path = await audio_processor.match_audio_duration(
                    enhanced_audio_path, 
                    target_duration
                )
                
                output_video_path = await video_processor.create_lip_sync_preview(
                    video_path, 
                    timed_audio_path
                )
                
                print(f"🎬 Lip-sync video: {output_video_path}")
                
            except Exception as e:
                print(f"⚠️ Lip-sync failed, using original video: {e}")
                output_video_path = video_path
                timed_audio_path = enhanced_audio_path
        else:
            output_video_path = video_path
            timed_audio_path = enhanced_audio_path
        
        # Step 6: Optimize for social media
        tasks[task_id].update({
            "progress": 90,
            "current_step": "Optimizing for social media..."
        })
        
        try:
            final_video_path = await video_processor.optimize_for_social_media(
                output_video_path, 
                "reels"
            )
            print(f"📱 Optimized video: {final_video_path}")
        except Exception as e:
            print(f"⚠️ Optimization failed, using original: {e}")
            final_video_path = output_video_path
        
        # Complete
        tasks[task_id].update({
            "status": "completed",
            "progress": 100,
            "current_step": "Processing complete!",
            "output_video_path": final_video_path,
            "output_audio_path": timed_audio_path,
            "script_used": script
        })
        
        print(f"✅ Dubbing task {task_id} completed successfully")
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Processing error in task {task_id}: {error_msg}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        
        tasks[task_id].update({
            "status": "failed",
            "error": f"Processing failed: {error_msg}"
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


    