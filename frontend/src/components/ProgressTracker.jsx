import React from 'react';
import { Clock, CheckCircle, Loader, AlertCircle } from 'lucide-react';

const ProgressTracker = ({ status, progress, currentStep, estimatedTime }) => {
  const steps = [
    { id: 1, name: 'Video Analysis', icon: '🎥' },
    { id: 2, name: 'Script Generation', icon: '📝' },
    { id: 3, name: 'Voice Synthesis', icon: '🎙️' },
    { id: 4, name: 'Audio Processing', icon: '🎵' },
    { id: 5, name: 'Lip Sync', icon: '👄' },
    { id: 6, name: 'Optimization', icon: '⚡' }
  ];

  const getStepStatus = (stepProgress) => {
    if (progress >= stepProgress) return 'completed';
    if (progress >= stepProgress - 15) return 'active';
    return 'pending';
  };

  const getStatusIcon = () => {
    switch (status) {
      case 'processing':
        return <Loader className="w-6 h-6 text-blue-600 animate-spin" />;
      case 'completed':
        return <CheckCircle className="w-6 h-6 text-green-600" />;
      case 'failed':
        return <AlertCircle className="w-6 h-6 text-red-600" />;
      default:
        return <Clock className="w-6 h-6 text-gray-400" />;
    }
  };

  if (status === 'idle') {
    return null;
  }

  return (
    <div className="w-full max-w-2xl mx-auto bg-white rounded-2xl shadow-lg p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-3">
          {getStatusIcon()}
          <div>
            <h3 className="font-semibold text-gray-800">
              {status === 'processing' ? 'Processing Video...' :
               status === 'completed' ? 'Processing Complete!' :
               status === 'failed' ? 'Processing Failed' : 'Ready'}
            </h3>
            <p className="text-sm text-gray-600">{currentStep}</p>
          </div>
        </div>
        
        {estimatedTime && status === 'processing' && (
          <div className="text-right">
            <div className="text-sm text-gray-500">Est. time remaining</div>
            <div className="font-medium text-gray-700">{estimatedTime}s</div>
          </div>
        )}
      </div>
      
      {/* Progress Bar */}
      {status === 'processing' && (
        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span className="text-gray-600">Progress</span>
            <span className="font-medium text-gray-700">{progress}%</span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
            <div 
              className="h-full bg-gradient-to-r from-blue-500 to-purple-600 transition-all duration-500 ease-out"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>
      )}
      
      {/* Steps */}
      <div className="grid grid-cols-3 md:grid-cols-6 gap-4">
        {steps.map((step, index) => {
          const stepProgress = ((index + 1) / steps.length) * 100;
          const stepStatus = getStepStatus(stepProgress);
          
          return (
            <div key={step.id} className="text-center">
              <div className={`
                w-12 h-12 mx-auto rounded-full flex items-center justify-center text-xl transition-all duration-300
                ${stepStatus === 'completed' ? 'bg-green-100 scale-110' :
                  stepStatus === 'active' ? 'bg-blue-100 animate-pulse scale-110' :
                  'bg-gray-100'
                }
              `}>
                {step.icon}
              </div>
              <div className="mt-2">
                <div className={`text-xs font-medium transition-colors duration-300 ${
                  stepStatus === 'completed' ? 'text-green-600' :
                  stepStatus === 'active' ? 'text-blue-600' :
                  'text-gray-400'
                }`}>
                  {step.name}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ProgressTracker;

