import React, { useState, useEffect } from 'react';
import { Globe, ChevronDown } from 'lucide-react';
import { getSupportedLanguages } from '../services/api';

const LanguageSelector = ({ selectedLanguage, onLanguageChange }) => {
  const [languages, setLanguages] = useState({});
  const [isOpen, setIsOpen] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadLanguages();
  }, []);

  const loadLanguages = async () => {
    try {
      const response = await getSupportedLanguages();
      setLanguages(response.data.languages);
    } catch (error) {
      console.error('Failed to load languages:', error);
      // Fallback languages
      setLanguages({
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'hi': 'Hindi'
      });
    } finally {
      setLoading(false);
    }
  };

  const flags = {
    'en': '🇺🇸',
    'es': '🇪🇸',
    'fr': '🇫🇷',
    'de': '🇩🇪',
    'it': '🇮🇹',
    'pt': '🇵🇹',
    'hi': '🇮🇳',
    'ja': '🇯🇵',
    'ko': '🇰🇷'
  };

  if (loading) {
    return (
      <div className="animate-pulse">
        <div className="h-12 bg-gray-200 rounded-lg"></div>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      <label className="flex items-center space-x-2 text-sm font-medium text-gray-700">
        <Globe className="w-4 h-4" />
        <span>Output Language</span>
      </label>
      
      <div className="relative">
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="w-full p-3 bg-white border border-gray-300 rounded-lg shadow-sm hover:border-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <span className="text-xl">{flags[selectedLanguage] || '🌐'}</span>
              <span className="font-medium">{languages[selectedLanguage] || 'Select Language'}</span>
            </div>
            <ChevronDown className={`w-5 h-5 text-gray-400 transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`} />
          </div>
        </button>
        
        {isOpen && (
          <div className="absolute z-10 w-full mt-1 bg-white border border-gray-300 rounded-lg shadow-lg max-h-60 overflow-auto">
            {Object.entries(languages).map(([code, name]) => (
              <button
                key={code}
                onClick={() => {
                  onLanguageChange(code);
                  setIsOpen(false);
                }}
                className={`
                  w-full p-3 text-left hover:bg-gray-50 transition-colors duration-150
                  flex items-center space-x-3
                  ${selectedLanguage === code ? 'bg-blue-50 text-blue-600' : 'text-gray-700'}
                `}
              >
                <span className="text-xl">{flags[code] || '🌐'}</span>
                <span className="font-medium">{name}</span>
                {selectedLanguage === code && (
                  <div className="ml-auto w-2 h-2 bg-blue-600 rounded-full" />
                )}
              </button>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default LanguageSelector;

