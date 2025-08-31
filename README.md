# VoiceCraft Studio

**AI-Powered Voice Dubbing for Short Videos (Reels/TikTok/YouTube Shorts)**

Transform your videos with professional AI voiceovers in multiple languages with advanced lip-sync technology. Perfect for content creators who want to scale their video production without spending hours on manual voiceover recording.

## Features

### Core Features
- **AI Video Analysis** - Gemini 2.5 Flash automatically analyzes your video content
- **Smart Script Generation** - Auto-generates engaging scripts based on video content
- **5 Voice Personalities** - Professional, Friendly, Humorous, Dynamic, Soothing
- **Multi-Language Support** - 9+ languages with automatic translation
- **Advanced Lip-Sync** - Natural-looking lip synchronization
- **Social Media Optimization** - Auto-format for Reels, TikTok, YouTube Shorts

### Advanced Features
- **Real-time Processing** - Live progress tracking with ETA
- **Audio Enhancement** - Professional audio normalization and compression
- **Custom Script Editing** - Override AI-generated scripts
- **Multi-format Downloads** - Separate video and audio file downloads
- **Video Analytics** - Duration, resolution, and format analysis
- **Batch Processing Ready** - Architecture supports multiple video processing

## Tech Stack

### Frontend
- **React 18** - Modern UI framework
- **Vite** - Lightning-fast build tool
- **Tailwind CSS** - Utility-first styling
- **Lucide React** - Beautiful icons
- **React Dropzone** - Drag & drop file uploads
- **Axios** - HTTP client for API calls

### Backend
- **FastAPI** - High-performance Python web framework
- **Python 3.8+** - Core backend language
- **Pydantic** - Data validation and serialization
- **AsyncIO** - Asynchronous processing
- **Uvicorn** - ASGI server

### AI Services
- **Google Gemini 2.5 Flash** - Video analysis and script generation
- **Murf AI** - Professional text-to-speech and dubbing
- **MoviePy** - Video processing and manipulation
- **OpenCV** - Computer vision for lip-sync
- **Pydub** - Audio processing and enhancement

## Quick Start

### Prerequisites
- Node.js 16 or higher
- Python 3.8 or higher
- Murf AI API Key
- Google Gemini API Key

### Installation

#### 1. Clone Repository
```bash
git clone https://github.com/yourusername/voicecraft-studio.git
cd voicecraft-studio
```

#### 2. Backend Setup
```bash
cd backend
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Frontend Setup
```bash
cd frontend
npm install
```

#### 4. Environment Configuration

**Backend Environment (.env file in backend folder):**
```env
MURF_API_KEY=your_murf_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
UPLOAD_DIR=uploads
MAX_FILE_SIZE=100000000
ALLOWED_EXTENSIONS=mp4,avi,mov,mkv
```

**Frontend Environment (optional .env file in frontend folder):**
```env
VITE_API_URL=http://localhost:8000
```

#### 5. Create Upload Directories
```bash
mkdir -p uploads/videos uploads/audio uploads/processed uploads/temp
```

### Running the Application

#### Start Backend Server
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Start Frontend Development Server
```bash
cd frontend
npm run dev
```

The application will be available at `http://localhost:5173`

## API Keys Setup

### Murf AI API Key
1. Visit [Murf.ai](https://murf.ai)
2. Create an account and subscribe to a plan
3. Navigate to API section in your dashboard
4. Generate your API key
5. Add to backend/.env file

### Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create new project or use existing one
3. Generate API key
4. Enable Gemini Pro API
5. Add to backend/.env file

## How It Works

### Step 1: Upload Video
- Drag and drop your video file or click to browse
- Supported formats: MP4, AVI, MOV, MKV
- Maximum file size: 100MB
- Automatic format validation and video analysis

### Step 2: AI Content Analysis
- Gemini 2.5 Flash analyzes your video frame by frame
- Identifies key visual elements and actions
- Generates contextually appropriate script
- Estimates optimal voice timing and duration

### Step 3: Voice Configuration
- Choose from 5 distinct voice personalities
- Select target language (supports 9+ languages)
- Edit the AI-generated script if needed
- Configure lip-sync and audio enhancement options

### Step 4: AI Processing Pipeline
- Murf AI generates professional-quality voiceover
- Advanced audio processing and normalization
- Lip-sync generation with facial landmark detection
- Social media format optimization

### Step 5: Download Results
- Download high-quality dubbed video
- Download separate audio file
- Files optimized for social media platforms

## Project Structure

```
voicecraft-studio/
├── frontend/                    # React + Vite Frontend
│   ├── src/
│   │   ├── components/         # Reusable UI components
│   │   │   ├── VideoUploader.jsx
│   │   │   ├── VoiceSelector.jsx
│   │   │   ├── ProgressTracker.jsx
│   │   │   ├── VideoPlayer.jsx
│   │   │   └── LanguageSelector.jsx
│   │   ├── services/           # API communication layer
│   │   │   └── api.js
│   │   ├── styles/             # CSS and styling
│   │   │   └── index.css
│   │   ├── App.jsx             # Main application component
│   │   └── main.jsx            # Application entry point
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── backend/                     # FastAPI Backend
│   ├── app/
│   │   ├── models/             # Pydantic data models
│   │   │   └── schemas.py
│   │   ├── services/           # Business logic services
│   │   │   ├── gemini_client.py    # Google Gemini integration
│   │   │   ├── murf_client.py      # Murf AI integration
│   │   │   ├── video_processor.py  # Video processing logic
│   │   │   └── audio_processor.py  # Audio enhancement
│   │   ├── utils/              # Helper utilities
│   │   │   └── file_handler.py
│   │   ├── main.py             # FastAPI application
│   │   └── config.py           # Configuration management
│   ├── requirements.txt
│   └── .env.example
│
├── uploads/                     # File storage directory
│   ├── videos/                 # Uploaded video files
│   ├── audio/                  # Generated audio files
│   ├── processed/              # Final processed videos
│   └── temp/                   # Temporary processing files
│
├── README.md
├── .gitignore
└── docker-compose.yml
```

## API Documentation

### Endpoints

#### Video Management
- `POST /api/upload-video` - Upload and analyze video file
- `GET /api/video/{video_id}` - Retrieve video information

#### Dubbing Operations
- `POST /api/generate-dubbing` - Start dubbing generation process
- `GET /api/status/{task_id}` - Check processing status
- `GET /api/download/{task_id}/{file_type}` - Download processed files

#### Configuration
- `GET /api/languages` - Get list of supported languages
- `GET /api/voices` - Get available voice personalities

### Request/Response Examples

#### Upload Video
```bash
curl -X POST -F "file=@video.mp4" http://localhost:8000/api/upload-video
```

#### Generate Dubbing
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "video_id": "uuid-here",
    "voice_personality": "casual",
    "target_language": "es",
    "lip_sync": true
  }' \
  http://localhost:8000/api/generate-dubbing
```

## Voice Personalities

| Personality | Description | Best Use Cases |
|-------------|-------------|----------------|
| **Professional** | Clear, authoritative, trustworthy tone | Business content, tutorials, educational videos |
| **Friendly** | Warm, approachable, conversational style | Lifestyle vlogs, personal content, casual tutorials |
| **Humorous** | Light-hearted, entertaining, engaging | Comedy content, memes, fun educational content |
| **Dynamic** | High-energy, motivational, exciting | Sports content, fitness videos, motivational content |
| **Soothing** | Gentle, peaceful, calming tone | Meditation videos, ASMR content, relaxation content |

## Supported Languages

- **English** (en) - Native support with all voice personalities
- **Spanish** (es) - Auto-translation with native voice synthesis
- **French** (fr) - Auto-translation with native voice synthesis
- **German** (de) - Auto-translation with native voice synthesis
- **Italian** (it) - Auto-translation with native voice synthesis
- **Portuguese** (pt) - Auto-translation with native voice synthesis
- **Hindi** (hi) - Auto-translation with native voice synthesis
- **Japanese** (ja) - Auto-translation with native voice synthesis
- **Korean** (ko) - Auto-translation with native voice synthesis

## Development

### Local Development Setup

#### Backend Development
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

#### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

#### Running Tests
```bash
# Backend tests (if implemented)
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

### Building for Production

#### Frontend Build
```bash
cd frontend
npm run build
```

#### Backend Production
```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Docker Deployment

### Using Docker Compose
```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d

# Stop services
docker-compose down
```

### Individual Docker Commands
```bash
# Build backend
docker build -t voicecraft-backend ./backend

# Build frontend
docker build -t voicecraft-frontend ./frontend

# Run backend
docker run -p 8000:8000 voicecraft-backend

# Run frontend
docker run -p 5173:5173 voicecraft-frontend
```

## Performance Specifications

- **Maximum Video Size**: 100MB per upload
- **Supported Formats**: MP4, AVI, MOV, MKV
- **Processing Time**: 30-60 seconds for typical short video (15-60 seconds)
- **Audio Quality**: 192kbps MP3 with professional enhancement
- **Concurrent Processing**: Multiple users supported
- **Output Optimization**: Automatic social media format optimization

## Security and Privacy

### Data Handling
- **Temporary Storage**: Files are processed and cleaned up automatically
- **No Permanent Storage**: Videos are not permanently stored on servers
- **API Security**: Rate limiting and input validation implemented
- **File Validation**: Strict file type and size checking
- **CORS Protection**: Secure cross-origin resource sharing

### Privacy Features
- **Local Processing**: Video analysis happens on your server
- **No Data Mining**: Content is not used for training or analytics
- **Secure Uploads**: Files are processed in isolated environment
- **Auto Cleanup**: Temporary files are automatically removed

## Troubleshooting

### Common Issues and Solutions

#### Application Won't Start
```bash
# Check Node.js version
node --version  # Should be 16+

# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
cd frontend && npm install
cd backend && pip install -r requirements.txt
```

#### Blank Page in Browser
```bash
# Check browser console for errors
# Verify dev server is running on correct port
# Check if index.html exists in frontend root directory
```

#### API Connection Errors
```bash
# Test backend connectivity
curl http://localhost:8000/api/languages

# Check CORS configuration
# Verify proxy settings in vite.config.js
```

#### Video Upload Failures
```bash
# Verify file format is supported
# Check file size is under 100MB
# Ensure upload directory exists and has write permissions
```

#### Processing Failures
```bash
# Verify API keys are correctly set in .env file
# Check API key quotas and limits
# Review backend logs for detailed error messages
```

### Debug Commands
```bash
# Test API endpoints
curl http://localhost:8000/docs  # FastAPI documentation
curl http://localhost:8000/api/languages  # Language support check

# Check file permissions
ls -la uploads/
ls -la backend/.env

# View backend logs
cd backend
uvicorn app.main:app --reload --log-level debug
```

## Contributing

### Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes and commit: `git commit -m 'Add new feature'`
4. Push to your branch: `git push origin feature/new-feature`
5. Create a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Use ESLint configuration for JavaScript/React code
- Add unit tests for new features
- Update documentation for API changes
- Test across different video formats and sizes

### Code Review Process
- All changes require review before merging
- Automated tests must pass
- Documentation must be updated for new features
- Performance impact should be considered

## Roadmap

### Phase 1 - Core Features (Completed)
- Basic video upload and processing
- AI script generation with Gemini
- Multi-personality voice synthesis
- Language translation capabilities
- Basic lip-sync implementation

### Phase 2 - Enhanced Features (In Progress)
- Advanced lip-sync with facial landmark detection
- Emotion-based voice modulation
- Background music integration
- Batch video processing capabilities
- Cloud storage integration (AWS S3, Google Cloud)

### Phase 3 - Advanced Features (Planned)
- Real-time collaboration tools
- Built-in video editing capabilities
- Custom voice cloning functionality
- Comprehensive analytics dashboard
- Mobile application (React Native)
- API rate limiting and user management

### Phase 4 - Enterprise Features (Future)
- White-label solutions
- Custom voice training
- Enterprise SSO integration
- Advanced analytics and reporting
- Custom deployment options

## Cost Analysis

### API Usage Costs
- **Murf AI**: Approximately $0.10-0.50 per minute of generated audio
- **Google Gemini**: Approximately $0.001 per 1,000 tokens for analysis
- **Storage**: Minimal cost for temporary file storage
- **Compute**: Variable based on video processing requirements

### Cost Optimization Strategies
- Implement caching for frequently generated scripts
- Use audio compression to reduce API costs
- Implement background job queues for efficient batch processing
- Monitor and set API usage limits
- Consider bulk API pricing for high-volume usage

## Deployment

### Production Environment Variables

#### Backend Configuration
```env
MURF_API_KEY=production_murf_key
GEMINI_API_KEY=production_gemini_key
UPLOAD_DIR=/app/uploads
MAX_FILE_SIZE=100000000
ALLOWED_EXTENSIONS=mp4,avi,mov,mkv
CORS_ORIGINS=https://yourdomain.com
DATABASE_URL=postgresql://user:pass@localhost/dbname
REDIS_URL=redis://localhost:6379
```

#### Frontend Configuration
```env
VITE_API_URL=https://api.yourdomain.com
VITE_APP_NAME=VoiceCraft Studio
VITE_MAX_FILE_SIZE=100000000
```

### Production Deployment Steps

#### Using Docker
```bash
# Build production images
docker-compose -f docker-compose.prod.yml build

# Deploy to production
docker-compose -f docker-compose.prod.yml up -d
```

#### Manual Deployment
```bash
# Build frontend
cd frontend
npm run build

# Deploy backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Serve frontend with nginx/apache
# Point web server to frontend/dist directory
```

## Testing

### Manual Testing Checklist
- [ ] Video upload with various formats (MP4, AVI, MOV, MKV)
- [ ] AI script generation accuracy
- [ ] Voice personality selection and audio generation
- [ ] Language translation functionality
- [ ] Dubbing process completion
- [ ] Lip-sync quality assessment
- [ ] File download functionality
- [ ] Error handling for invalid inputs
- [ ] Performance with large video files
- [ ] Cross-browser compatibility

### Automated Testing
```bash
# Run backend tests
cd backend
python -m pytest tests/ -v

# Run frontend tests
cd frontend
npm test

# Run integration tests
npm run test:integration
```

### Sample Test Cases
- **File Upload**: Test with 5s, 30s, and 60s videos
- **Format Support**: Test MP4, AVI, MOV, MKV files
- **Size Limits**: Test files near 100MB limit
- **Error Handling**: Test invalid formats and oversized files
- **API Integration**: Test all voice personalities and languages

## Monitoring and Analytics

### Key Metrics to Track
- **Upload Success Rate** - Percentage of successful video uploads
- **Processing Time** - Average time from upload to completion
- **API Usage** - Murf and Gemini API call volumes and costs
- **Error Rates** - Failed processing attempts and reasons
- **User Engagement** - Most popular voice personalities and languages

### Logging Configuration
```python
# Backend logging setup
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('voicecraft.log'),
        logging.StreamHandler()
    ]
)
```

## Security Considerations

### File Upload Security
- File type validation using magic numbers
- File size limits strictly enforced
- Virus scanning for uploaded files (recommended)
- Temporary file cleanup after processing

### API Security
- Rate limiting to prevent abuse
- Input validation and sanitization
- CORS properly configured
- API key rotation strategy

### Data Privacy
- No permanent storage of user videos
- Automatic cleanup of temporary files
- No logging of video content
- GDPR compliance considerations

## Support and Documentation

### Getting Help
- **GitHub Issues**: Report bugs and request features
- **Documentation**: Comprehensive API and setup guides
- **Community**: Join discussions and share tips

### Reporting Issues
When reporting bugs, please include:
- Operating system and version
- Node.js and Python versions
- Complete error messages and stack traces
- Steps to reproduce the issue
- Sample video files (if applicable and appropriate)

### Feature Requests
- Use GitHub Issues with "enhancement" label
- Provide detailed description of proposed feature
- Include use cases and potential implementation approach
- Consider contributing the feature yourself

## License

This project is licensed under the MIT License. See the LICENSE file for full details.

## Acknowledgments

### Third-Party Services
- **Murf AI** for professional voice synthesis capabilities
- **Google Gemini** for advanced AI video analysis
- **OpenAI** for natural language processing research
- **FFmpeg** for video processing foundations

### Open Source Libraries
- **React** and **Vite** for modern frontend development
- **FastAPI** for high-performance backend framework
- **MoviePy** for Python video processing
- **Tailwind CSS** for utility-first styling
- **Lucide React** for beautiful iconography

### Community
- All contributors who help improve this project
- Beta testers who provide valuable feedback
- Content creators who inspire new features

---

**Ready to transform your video content? Get started by uploading your first video and experience the power of AI voice dubbing.**
