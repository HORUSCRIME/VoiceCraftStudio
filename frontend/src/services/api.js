// // import axios from 'axios';

// // const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// // const api = axios.create({
// //   baseURL: API_BASE_URL,
// //   timeout: 300000, // 5 minutes for video processing
// // });

// // export const uploadVideo = async (file) => {
// //   const formData = new FormData();
// //   formData.append('file', file);
  
// //   return await api.post('/api/upload-video', formData, {
// //     headers: {
// //       'Content-Type': 'multipart/form-data',
// //     },
// //   });
// // };

// // export const generateDubbing = async (dubbingRequest) => {
// //   return await api.post('/api/generate-dubbing', dubbingRequest);
// // };

// // export const getProcessingStatus = async (taskId) => {
// //   return await api.get(`/api/status/${taskId}`);
// // };

// // export const downloadFile = async (taskId, fileType) => {
// //   return await api.get(`/api/download/${taskId}/${fileType}`, {
// //     responseType: 'blob',
// //   });
// // };

// // export const getSupportedLanguages = async () => {
// //   return await api.get('/api/languages');
// // };

// // export default api;





// import axios from 'axios';

// // Vite uses import.meta.env instead of process.env
// const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// const api = axios.create({
//   baseURL: API_BASE_URL,
//   timeout: 300000, // 5 minutes for video processing
//   headers: {
//     'Content-Type': 'application/json',
//   },
// });

// // Request interceptor for debugging
// api.interceptors.request.use(
//   (config) => {
//     console.log('API Request:', config.method?.toUpperCase(), config.url);
//     return config;
//   },
//   (error) => {
//     console.error('API Request Error:', error);
//     return Promise.reject(error);
//   }
// );

// // Response interceptor for error handling
// api.interceptors.response.use(
//   (response) => {
//     console.log('API Response:', response.status, response.config.url);
//     return response;
//   },
//   (error) => {
//     console.error('API Response Error:', error.response?.status, error.response?.data);
    
//     if (error.response?.status === 413) {
//       throw new Error('File too large. Please upload a smaller video.');
//     } else if (error.response?.status === 422) {
//       throw new Error('Invalid file format. Please upload MP4, AVI, MOV, or MKV.');
//     } else if (error.response?.status >= 500) {
//       throw new Error('Server error. Please try again later.');
//     }
    
//     return Promise.reject(error);
//   }
// );

// export const uploadVideo = async (file) => {
//   const formData = new FormData();
//   formData.append('file', file);
  
//   return await api.post('/api/upload-video', formData, {
//     headers: {
//       'Content-Type': 'multipart/form-data',
//     },
//     onUploadProgress: (progressEvent) => {
//       const progress = Math.round((progressEvent.loaded * 100) / progressEvent.total);
//       console.log('Upload progress:', progress + '%');
//     },
//   });
// };

// export const generateDubbing = async (dubbingRequest) => {
//   return await api.post('/api/generate-dubbing', dubbingRequest);
// };

// export const getProcessingStatus = async (taskId) => {
//   return await api.get(`/api/status/${taskId}`);
// };

// export const downloadFile = async (taskId, fileType) => {
//   return await api.get(`/api/download/${taskId}/${fileType}`, {
//     responseType: 'blob',
//   });
// };

// export const getSupportedLanguages = async () => {
//   return await api.get('/api/languages');
// };

// export default api;





import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 300000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request interceptor for debugging
api.interceptors.request.use(
  (config) => {
    console.log('🚀 API Request:', config.method?.toUpperCase(), config.url);
    return config;
  },
  (error) => {
    console.error('❌ API Request Error:', error);
    return Promise.reject(error);
  }
);

// Add response interceptor
api.interceptors.response.use(
  (response) => {
    console.log('✅ API Response:', response.status, response.config.url);
    return response;
  },
  (error) => {
    console.error('❌ API Error:', error.response?.status, error.message);
    
    if (error.code === 'ECONNREFUSED') {
      throw new Error('Cannot connect to server. Make sure backend is running on port 8000');
    }
    
    return Promise.reject(error);
  }
);

export const uploadVideo = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  
  return await api.post('/api/upload-video', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

export const generateDubbing = async (dubbingRequest) => {
  return await api.post('/api/generate-dubbing', dubbingRequest);
};

export const getProcessingStatus = async (taskId) => {
  return await api.get(`/api/status/${taskId}`);
};

export const downloadFile = async (taskId, fileType) => {
  return await api.get(`/api/download/${taskId}/${fileType}`, {
    responseType: 'blob',
  });
};

export const getSupportedLanguages = async () => {
  return await api.get('/api/languages');
};

export default api;