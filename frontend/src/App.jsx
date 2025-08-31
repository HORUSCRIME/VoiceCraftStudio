// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vite.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.jsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }

// export default App




import React, { useState, useEffect } from 'react';
import { Mic, Sparkles, Globe, Video } from 'lucide-react';
import VideoUploader from './components/VideoUploader';
import VoiceSelector from './components/VoiceSelector';
import LanguageSelector from './components/LanguageSelector';
import ProgressTracker from './components/ProgressTracker';
import VideoPlayer from './components/VideoPlayer';
import { uploadVideo, generateDubbing, getProcessingStatus, downloadFile } from './services/api';



function App() {
  const [currentStep, setCurrentStep] = useState('upload');
  const [videoData, setVideoData] = useState(null);
  const [selectedPersonality, setSelectedPersonality] = useState('serious');
  const [selectedLanguage, setSelectedLanguage] = useState('en');
  const [customScript, setCustomScript] = useState('');
  const [lipSync, setLipSync] = useState(true);
  const [processing, setProcessing] = useState({
    status: 'idle',
    progress: 0,
    currentStep: '',
    taskId: null
  });
  const [results, setResults] = useState({
    videoUrl: null,
    audioUrl: null
  });

  // Poll for processing status
  useEffect(() => {
    if (processing.taskId && processing.status === 'processing') {
      const interval = setInterval(async () => {
        try {
          const response = await getProcessingStatus(processing.taskId);
          const status = response.data;
          
          setProcessing(prev => ({
            ...prev,
            status: status.status,
            progress: status.progress,
            currentStep: status.current_step,
            estimatedTime: status.estimated_time
          }));
          
          if (status.status === 'completed') {
            setResults({
              videoUrl: `/api/download/${processing.taskId}/video`,
              audioUrl: `/api/download/${processing.taskId}/audio`
            });
            setCurrentStep('results');
            clearInterval(interval);
          } else if (status.status === 'failed') {
            clearInterval(interval);
          }
        } catch (error) {
          console.error('Status check failed:', error);
          clearInterval(interval);
        }
      }, 2000);

      return () => clearInterval(interval);
    }
  }, [processing.taskId, processing.status]);

  const handleVideoUpload = async (file) => {
    try {
      setProcessing(prev => ({ ...prev, status: 'uploading' }));
      
      const response = await uploadVideo(file);
      const data = response.data;
      
      setVideoData({
        id: data.video_id,
        filename: data.filename,
        info: data.video_info,
        suggestedScript: data.suggested_script,
        estimatedDuration: data.estimated_duration
      });
      
      setCustomScript(data.suggested_script);
      setCurrentStep('configure');
      setProcessing(prev => ({ ...prev, status: 'idle' }));
      
    } catch (error) {
      console.error('Upload failed:', error);
      throw new Error(error.response?.data?.detail || 'Upload failed');
    }
  };

  const handleStartDubbing = async () => {
    try {
      const response = await generateDubbing({
        video_id: videoData.id,
        voice_personality: selectedPersonality,
        target_language: selectedLanguage,
        script_override: customScript.trim() || null,
        lip_sync: lipSync
      });
      
      const data = response.data;
      
      setProcessing({
        status: 'processing',
        progress: 0,
        currentStep: 'Starting processing...',
        taskId: data.task_id
      });
      
      setCurrentStep('processing');
      
    } catch (error) {
      console.error('Dubbing failed:', error);
      alert(error.response?.data?.detail || 'Processing failed');
    }
  };

  const handleDownload = async (fileType) => {
    try {
      const response = await downloadFile(processing.taskId, fileType);
      const blob = response.data;
      
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `dubbed_${fileType}.${fileType === 'video' ? 'mp4' : 'mp3'}`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
      
    } catch (error) {
      console.error('Download failed:', error);
      alert('Download failed');
    }
  };

  const handleRestart = () => {
    setCurrentStep('upload');
    setVideoData(null);
    setSelectedPersonality('serious');
    setSelectedLanguage('en');
    setCustomScript('');
    setProcessing({
      status: 'idle',
      progress: 0,
      currentStep: '',
      taskId: null
    });
    setResults({
      videoUrl: null,
      audioUrl: null
    });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-lg border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center">
                <Mic className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                  VoiceCraft Studio
                </h1>
                <p className="text-sm text-gray-600">AI-Powered Voice Dubbing for Social Media</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-4">
              <div className="hidden sm:flex items-center space-x-6 text-sm">
                <div className={`flex items-center space-x-2 ${currentStep === 'upload' ? 'text-blue-600 font-medium' : 'text-gray-400'}`}>
                  <Video className="w-4 h-4" />
                  <span>Upload</span>
                </div>
                <div className={`flex items-center space-x-2 ${currentStep === 'configure' ? 'text-blue-600 font-medium' : 'text-gray-400'}`}>
                  <Sparkles className="w-4 h-4" />
                  <span>Configure</span>
                </div>
                <div className={`flex items-center space-x-2 ${currentStep === 'processing' ? 'text-blue-600 font-medium' : 'text-gray-400'}`}>
                  <Globe className="w-4 h-4" />
                  <span>Process</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-8">
        {currentStep === 'upload' && (
          <div className="space-y-8">
            <div className="text-center space-y-4">
              <h2 className="text-4xl font-bold text-gray-800">
                Transform Your Videos with
                <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent"> AI Voice Dubbing</span>
              </h2>
              <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                Upload your video and let our AI create professional voiceovers in multiple languages with perfect lip-sync
              </p>
            </div>
            
            <VideoUploader 
              onVideoUploaded={handleVideoUpload}
              isUploading={processing.status === 'uploading'}
            />
            
            {/* Features */}
            <div className="grid md:grid-cols-3 gap-6 max-w-4xl mx-auto mt-12">
              <div className="text-center p-6 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                <div className="w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
                  <Mic className="w-8 h-8 text-blue-600" />
                </div>
                <h3 className="font-semibold text-gray-800 mb-2">AI Voice Generation</h3>
                <p className="text-gray-600 text-sm">Multiple personalities and natural-sounding voices</p>
              </div>
              
              <div className="text-center p-6 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                <div className="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
                  <Globe className="w-8 h-8 text-purple-600" />
                </div>
                <h3 className="font-semibold text-gray-800 mb-2">Multi-Language Support</h3>
                <p className="text-gray-600 text-sm">Translate and dub in 9+ languages automatically</p>
              </div>
              
              <div className="text-center p-6 bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                <div className="w-16 h-16 bg-green-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
                  <Sparkles className="w-8 h-8 text-green-600" />
                </div>
                <h3 className="font-semibold text-gray-800 mb-2">Lip-Sync Technology</h3>
                <p className="text-gray-600 text-sm">Advanced lip-sync for natural-looking results</p>
              </div>
            </div>
          </div>
        )}

        {currentStep === 'configure' && videoData && (
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-800 mb-2">Configure Your Dubbing</h2>
              <p className="text-gray-600">Customize voice, language, and script for your video</p>
            </div>
            
            {/* Video Info Card */}
            <div className="bg-white rounded-2xl shadow-lg p-6 max-w-2xl mx-auto">
              <div className="flex items-center space-x-4">
                <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                  <Video className="w-6 h-6 text-blue-600" />
                </div>
                <div className="flex-1">
                  <h3 className="font-semibold text-gray-800">{videoData.filename}</h3>
                  <div className="text-sm text-gray-600 space-y-1">
                    <p>Duration: {videoData.info.duration?.toFixed(1)}s • Size: {videoData.info.size_mb?.toFixed(1)}MB</p>
                    <p>Resolution: {videoData.info.resolution?.[0]}x{videoData.info.resolution?.[1]}</p>
                  </div>
                </div>
              </div>
            </div>
            
            {/* Voice Selector */}
            <VoiceSelector 
              selectedPersonality={selectedPersonality}
              onPersonalityChange={setSelectedPersonality}
            />
            
            {/* Language & Script Configuration */}
            <div className="bg-white rounded-2xl shadow-lg p-6 max-w-4xl mx-auto space-y-6">
              <div className="grid md:grid-cols-2 gap-6">
                <LanguageSelector 
                  selectedLanguage={selectedLanguage}
                  onLanguageChange={setSelectedLanguage}
                />
                
                <div className="space-y-3">
                  <label className="flex items-center space-x-2 text-sm font-medium text-gray-700">
                    <Sparkles className="w-4 h-4" />
                    <span>Lip-Sync</span>
                  </label>
                  <div className="flex items-center space-x-3">
                    <button
                      onClick={() => setLipSync(!lipSync)}
                      className={`
                        relative inline-flex h-6 w-11 items-center rounded-full transition-colors duration-200
                        ${lipSync ? 'bg-blue-600' : 'bg-gray-300'}
                      `}
                    >
                      <span
                        className={`
                          inline-block h-4 w-4 transform rounded-full bg-white transition-transform duration-200
                          ${lipSync ? 'translate-x-6' : 'translate-x-1'}
                        `}
                      />
                    </button>
                    <span className="text-sm text-gray-600">
                      {lipSync ? 'Enabled' : 'Disabled'}
                    </span>
                  </div>
                </div>
              </div>
              
              {/* Script Editor */}
              <div className="space-y-3">
                <label className="text-sm font-medium text-gray-700">
                  Script (AI Generated - Edit if needed)
                </label>
                <textarea
                  value={customScript}
                  onChange={(e) => setCustomScript(e.target.value)}
                  className="w-full h-32 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                  placeholder="AI will generate a script based on your video content..."
                />
                <div className="text-xs text-gray-500">
                  Estimated reading time: ~{Math.ceil(customScript.split(' ').length / 150 * 60)}s
                </div>
              </div>
              
              {/* Generate Button */}
              <div className="pt-4">
                <button
                  onClick={handleStartDubbing}
                  disabled={!customScript.trim()}
                  className="w-full py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold rounded-xl hover:from-blue-600 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-105 shadow-lg"
                >
                  <span className="flex items-center justify-center space-x-2">
                    <Sparkles className="w-5 h-5" />
                    <span>Generate AI Dubbing</span>
                  </span>
                </button>
              </div>
            </div>
          </div>
        )}

        {currentStep === 'processing' && (
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-800 mb-2">Creating Your Dubbing</h2>
              <p className="text-gray-600">Our AI is working its magic on your video</p>
            </div>
            
            <ProgressTracker 
              status={processing.status}
              progress={processing.progress}
              currentStep={processing.currentStep}
              estimatedTime={processing.estimatedTime}
            />
          </div>
        )}

        {currentStep === 'results' && (
          <div className="space-y-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold text-gray-800 mb-2">🎉 Your Dubbing is Ready!</h2>
              <p className="text-gray-600">Download your enhanced video or try different settings</p>
            </div>
            
            <VideoPlayer 
              originalVideoUrl={`/uploads/videos/${videoData?.id}.mp4`}
              dubbedVideoUrl={results.videoUrl}
              audioUrl={results.audioUrl}
              onDownload={handleDownload}
              onRestart={handleRestart}
            />
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-gray-50 border-t border-gray-200 mt-16">
        <div className="max-w-7xl mx-auto px-6 py-8">
          <div className="text-center space-y-4">
            <div className="flex justify-center space-x-6 text-sm text-gray-600">
              <span>• AI-Powered Voice Generation</span>
              <span>• Multi-Language Support</span>
              <span>• Professional Lip-Sync</span>
              <span>• Social Media Optimized</span>
            </div>
            <p className="text-gray-500 text-sm">
              Powered by Murf AI • Gemini 2.0 Flash • Advanced Audio Processing
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
