import React, { useRef, useState, useEffect } from 'react';
import { Play, Pause, Volume2, VolumeX, Download, RotateCcw } from 'lucide-react';

const VideoPlayer = ({ 
  originalVideoUrl, 
  dubbedVideoUrl, 
  audioUrl, 
  onDownload, 
  onRestart 
}) => {
  const videoRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isMuted, setIsMuted] = useState(false);
  const [showComparison, setShowComparison] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;

    const updateTime = () => setCurrentTime(video.currentTime);
    const updateDuration = () => setDuration(video.duration);

    video.addEventListener('timeupdate', updateTime);
    video.addEventListener('loadedmetadata', updateDuration);

    return () => {
      video.removeEventListener('timeupdate', updateTime);
      video.removeEventListener('loadedmetadata', updateDuration);
    };
  }, [dubbedVideoUrl]);

  const togglePlayPause = () => {
    const video = videoRef.current;
    if (!video) return;

    if (isPlaying) {
      video.pause();
    } else {
      video.play();
    }
    setIsPlaying(!isPlaying);
  };

  const toggleMute = () => {
    const video = videoRef.current;
    if (!video) return;

    video.muted = !isMuted;
    setIsMuted(!isMuted);
  };

  const formatTime = (time) => {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  const handleSeek = (e) => {
    const video = videoRef.current;
    if (!video) return;

    const rect = e.currentTarget.getBoundingClientRect();
    const pos = (e.clientX - rect.left) / rect.width;
    video.currentTime = pos * duration;
  };

  return (
    <div className="w-full max-w-4xl mx-auto space-y-6">
      {/* Video Container */}
      <div className="relative bg-black rounded-2xl overflow-hidden shadow-2xl">
        <video
          ref={videoRef}
          src={dubbedVideoUrl || originalVideoUrl}
          className="w-full h-auto max-h-96 object-contain"
          onPlay={() => setIsPlaying(true)}
          onPause={() => setIsPlaying(false)}
        />
        
        {/* Video Controls Overlay */}
        <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-4">
          <div className="space-y-3">
            {/* Progress Bar */}
            <div 
              className="w-full h-2 bg-white/20 rounded-full cursor-pointer"
              onClick={handleSeek}
            >
              <div 
                className="h-full bg-white rounded-full transition-all duration-150"
                style={{ width: `${(currentTime / duration) * 100 || 0}%` }}
              />
            </div>
            
            {/* Controls */}
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-4">
                <button
                  onClick={togglePlayPause}
                  className="p-2 bg-white/20 hover:bg-white/30 rounded-full transition-colors"
                >
                  {isPlaying ? (
                    <Pause className="w-6 h-6 text-white" />
                  ) : (
                    <Play className="w-6 h-6 text-white" />
                  )}
                </button>
                
                <button
                  onClick={toggleMute}
                  className="p-2 bg-white/20 hover:bg-white/30 rounded-full transition-colors"
                >
                  {isMuted ? (
                    <VolumeX className="w-6 h-6 text-white" />
                  ) : (
                    <Volume2 className="w-6 h-6 text-white" />
                  )}
                </button>
                
                <div className="text-white text-sm">
                  {formatTime(currentTime)} / {formatTime(duration)}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      {/* Comparison Toggle */}
      {originalVideoUrl && dubbedVideoUrl && (
        <div className="flex justify-center">
          <button
            onClick={() => setShowComparison(!showComparison)}
            className={`
              px-6 py-3 rounded-lg font-medium transition-all duration-200 transform hover:scale-105
              ${showComparison 
                ? 'bg-blue-500 text-white' 
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }
            `}
          >
            {showComparison ? 'Hide Comparison' : 'Compare Original'}
          </button>
        </div>
      )}
      
      {/* Action Buttons */}
      <div className="flex flex-col sm:flex-row gap-4 justify-center">
        {dubbedVideoUrl && (
          <button
            onClick={() => onDownload('video')}
            className="flex items-center justify-center space-x-2 px-8 py-4 bg-gradient-to-r from-green-500 to-emerald-600 text-white font-medium rounded-xl hover:from-green-600 hover:to-emerald-700 transition-all duration-200 transform hover:scale-105 shadow-lg"
          >
            <Download className="w-5 h-5" />
            <span>Download Video</span>
          </button>
        )}
        
        {audioUrl && (
          <button
            onClick={() => onDownload('audio')}
            className="flex items-center justify-center space-x-2 px-8 py-4 bg-gradient-to-r from-purple-500 to-violet-600 text-white font-medium rounded-xl hover:from-purple-600 hover:to-violet-700 transition-all duration-200 transform hover:scale-105 shadow-lg"
          >
            <Download className="w-5 h-5" />
            <span>Download Audio</span>
          </button>
        )}
        
        <button
          onClick={onRestart}
          className="flex items-center justify-center space-x-2 px-8 py-4 bg-gradient-to-r from-gray-500 to-slate-600 text-white font-medium rounded-xl hover:from-gray-600 hover:to-slate-700 transition-all duration-200 transform hover:scale-105 shadow-lg"
        >
          <RotateCcw className="w-5 h-5" />
          <span>New Project</span>
        </button>
      </div>
    </div>
  );
};

export default VideoPlayer;

