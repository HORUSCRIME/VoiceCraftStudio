import React, { useState } from 'react';
import { Volume2, Play, Pause } from 'lucide-react';

const VoiceSelector = ({ selectedPersonality, onPersonalityChange }) => {
  const [playingVoice, setPlayingVoice] = useState(null);

  const voicePersonalities = [
    {
      id: 'serious',
      name: 'Professional',
      description: 'Clear, authoritative, and trustworthy',
      icon: '🎯',
      color: 'bg-blue-500',
      preview: 'This is a professional and serious voice tone.'
    },
    {
      id: 'casual',
      name: 'Friendly', 
      description: 'Warm, approachable, and conversational',
      icon: '😊',
      color: 'bg-green-500',
      preview: 'Hey there! This is a casual and friendly voice.'
    },
    {
      id: 'funny',
      name: 'Humorous',
      description: 'Light-hearted, entertaining, and engaging',
      icon: '😄',
      color: 'bg-yellow-500',
      preview: 'Welcome to the fun zone! This voice brings the laughs.'
    },
    {
      id: 'energetic',
      name: 'Dynamic',
      description: 'High-energy, motivational, and exciting',
      icon: '⚡',
      color: 'bg-orange-500',
      preview: 'Get ready for an amazing experience with this energetic voice!'
    },
    {
      id: 'calm',
      name: 'Soothing',
      description: 'Gentle, peaceful, and relaxing',
      icon: '🧘',
      color: 'bg-purple-500',
      preview: 'Take a deep breath and enjoy this calm, soothing voice.'
    }
  ];

  const playVoicePreview = (voiceId) => {
    if (playingVoice === voiceId) {
      setPlayingVoice(null);
      // Stop audio playback
      return;
    }
    
    setPlayingVoice(voiceId);
    // Simulate audio preview (in real app, play actual voice sample)
    setTimeout(() => setPlayingVoice(null), 3000);
  };

  return (
    <div className="space-y-6">
      <div className="text-center">
        <h3 className="text-2xl font-bold text-gray-800 mb-2">Choose Voice Personality</h3>
        <p className="text-gray-600">Select the perfect voice to match your content's mood</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {voicePersonalities.map((voice) => (
          <div
            key={voice.id}
            className={`
              relative p-6 rounded-2xl border-2 cursor-pointer transition-all duration-300
              transform hover:scale-105 hover:shadow-lg
              ${selectedPersonality === voice.id 
                ? 'border-blue-500 bg-blue-50 shadow-md' 
                : 'border-gray-200 hover:border-gray-300'
              }
            `}
            onClick={() => onPersonalityChange(voice.id)}
          >
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div className={`w-12 h-12 ${voice.color} rounded-full flex items-center justify-center text-white text-xl`}>
                  {voice.icon}
                </div>
                
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    playVoicePreview(voice.id);
                  }}
                  className="p-2 hover:bg-gray-100 rounded-full transition-colors"
                >
                  {playingVoice === voice.id ? (
                    <Pause className="w-5 h-5 text-gray-600" />
                  ) : (
                    <Play className="w-5 h-5 text-gray-600" />
                  )}
                </button>
              </div>
              
              <div className="space-y-2">
                <h4 className="font-semibold text-gray-800">{voice.name}</h4>
                <p className="text-sm text-gray-600">{voice.description}</p>
                <p className="text-xs text-gray-500 italic">"{voice.preview}"</p>
              </div>
              
              {selectedPersonality === voice.id && (
                <div className="absolute top-2 right-2">
                  <div className="w-6 h-6 bg-blue-500 rounded-full flex items-center justify-center">
                    <div className="w-2 h-2 bg-white rounded-full" />
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default VoiceSelector;

