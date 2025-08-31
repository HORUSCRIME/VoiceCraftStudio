// // import React, { useCallback, useState } from 'react';
// // import { useDropzone } from 'react-dropzone';
// // import { Upload, Video, AlertCircle, CheckCircle } from 'lucide-react';

// // const VideoUploader = ({ onVideoUploaded, isUploading }) => {
// //   const [uploadProgress, setUploadProgress] = useState(0);
// //   const [error, setError] = useState(null);

// //   const onDrop = useCallback(async (acceptedFiles) => {
// //     const file = acceptedFiles[0];
// //     if (!file) return;

// //     setError(null);
// //     setUploadProgress(0);
    
// //     try {
// //       // Simulate upload progress
// //       const progressInterval = setInterval(() => {
// //         setUploadProgress(prev => {
// //           if (prev >= 90) {
// //             clearInterval(progressInterval);
// //             return 90;
// //           }
// //           return prev + 10;
// //         });
// //       }, 200);

// //       const result = await onVideoUploaded(file);
      
// //       clearInterval(progressInterval);
// //       setUploadProgress(100);
      
// //       setTimeout(() => setUploadProgress(0), 2000);
      
// //     } catch (err) {
// //       setError(err.message || 'Upload failed');
// //       setUploadProgress(0);
// //     }
// //   }, [onVideoUploaded]);

// //   const { getRootProps, getInputProps, isDragActive, isDragReject } = useDropzone({
// //     onDrop,
// //     accept: {
// //       'video/*': ['.mp4', '.avi', '.mov', '.mkv']
// //     },
// //     maxSize: 100 * 1024 * 1024, // 100MB
// //     multiple: false,
// //     disabled: isUploading
// //   });

// //   return (
// //     <div className="w-full max-w-2xl mx-auto">
// //       <div
// //         {...getRootProps()}
// //         className={`
// //           relative border-2 border-dashed rounded-2xl p-12 text-center cursor-pointer
// //           transition-all duration-300 ease-in-out transform hover:scale-105
// //           ${isDragActive && !isDragReject ? 'border-blue-400 bg-blue-50' : ''}
// //           ${isDragReject ? 'border-red-400 bg-red-50' : ''}
// //           ${!isDragActive ? 'border-gray-300 hover:border-blue-400 hover:bg-blue-50' : ''}
// //           ${isUploading ? 'opacity-50 cursor-not-allowed' : ''}
// //         `}
// //       >
// //         <input {...getInputProps()} />
        
// //         <div className="space-y-4">
// //           {uploadProgress > 0 ? (
// //             <div className="space-y-3">
// //               <div className="w-16 h-16 mx-auto bg-blue-100 rounded-full flex items-center justify-center">
// //                 <Video className="w-8 h-8 text-blue-600 animate-pulse" />
// //               </div>
// //               <div className="w-full bg-gray-200 rounded-full h-3">
// //                 <div 
// //                   className="bg-gradient-to-r from-blue-500 to-purple-500 h-3 rounded-full transition-all duration-300"
// //                   style={{ width: `${uploadProgress}%` }}
// //                 />
// //               </div>
// //               <p className="text-blue-600 font-medium">Uploading... {uploadProgress}%</p>
// //             </div>
// //           ) : (
// //             <>
// //               <div className={`w-20 h-20 mx-auto rounded-full flex items-center justify-center transition-all duration-300 ${
// //                 isDragActive ? 'bg-blue-100 scale-110' : 'bg-gray-100'
// //               }`}>
// //                 <Upload className={`w-10 h-10 transition-colors duration-300 ${
// //                   isDragActive ? 'text-blue-600' : 'text-gray-400'
// //                 }`} />
// //               </div>
              
// //               <div className="space-y-2">
// //                 <h3 className="text-xl font-semibold text-gray-800">
// //                   {isDragActive ? 'Drop your video here!' : 'Upload your video'}
// //                 </h3>
// //                 <p className="text-gray-500">
// //                   Drag & drop or click to select • MP4, AVI, MOV, MKV • Max 100MB
// //                 </p>
// //               </div>
              
// //               <button
// //                 type="button"
// //                 className="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-medium rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all duration-200 transform hover:scale-105"
// //                 disabled={isUploading}
// //               >
// //                 <Upload className="w-5 h-5 mr-2" />
// //                 Choose File
// //               </button>
// //             </>
// //           )}
// //         </div>
// //       </div>
      
// //       {error && (
// //         <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg flex items-center space-x-2">
// //           <AlertCircle className="w-5 h-5 text-red-500" />
// //           <span className="text-red-700">{error}</span>
// //         </div>
// //       )}
// //     </div>
// //   );
// // };

// // export default VideoUploader;


// import React, { useCallback, useState } from 'react';
// import { useDropzone } from 'react-dropzone';
// import { Upload, Video, AlertCircle } from 'lucide-react';

// const VideoUploader = ({ onVideoUploaded, isUploading }) => {
//   const [uploadProgress, setUploadProgress] = useState(0);
//   const [error, setError] = useState(null);

//   const onDrop = useCallback(async (acceptedFiles) => {
//     const file = acceptedFiles[0];
//     if (!file) return;

//     setError(null);
//     setUploadProgress(0);
    
//     try {
//       const progressInterval = setInterval(() => {
//         setUploadProgress(prev => {
//           if (prev >= 90) {
//             clearInterval(progressInterval);
//             return 90;
//           }
//           return prev + 10;
//         });
//       }, 200);

//       await onVideoUploaded(file);
      
//       clearInterval(progressInterval);
//       setUploadProgress(100);
      
//       setTimeout(() => setUploadProgress(0), 2000);
      
//     } catch (err) {
//       setError(err.message || 'Upload failed');
//       setUploadProgress(0);
//     }
//   }, [onVideoUploaded]);

//   const { getRootProps, getInputProps, isDragActive, isDragReject } = useDropzone({
//     onDrop,
//     accept: {
//       'video/*': ['.mp4', '.avi', '.mov', '.mkv']
//     },
//     maxSize: 100 * 1024 * 1024,
//     multiple: false,
//     disabled: isUploading
//   });

//   return (
//     <div className="w-full max-w-2xl mx-auto">
//       <div
//         {...getRootProps()}
//         className={`
//           relative border-2 border-dashed rounded-2xl p-12 text-center cursor-pointer
//           transition-all duration-300 ease-in-out
//           ${isDragActive && !isDragReject ? 'border-blue-400 bg-blue-50' : ''}
//           ${isDragReject ? 'border-red-400 bg-red-50' : ''}
//           ${!isDragActive ? 'border-gray-300 hover:border-blue-400 hover:bg-blue-50' : ''}
//           ${isUploading ? 'opacity-50 cursor-not-allowed' : ''}
//         `}
//       >
//         <input {...getInputProps()} />
        
//         <div className="space-y-4">
//           {uploadProgress > 0 ? (
//             <div className="space-y-3">
//               <div className="w-16 h-16 mx-auto bg-blue-100 rounded-full flex items-center justify-center">
//                 <Video className="w-8 h-8 text-blue-600 animate-pulse" />
//               </div>
//               <div className="w-full bg-gray-200 rounded-full h-3">
//                 <div 
//                   className="bg-gradient-to-r from-blue-500 to-purple-500 h-3 rounded-full transition-all duration-300"
//                   style={{ width: `${uploadProgress}%` }}
//                 />
//               </div>
//               <p className="text-blue-600 font-medium">Uploading... {uploadProgress}%</p>
//             </div>
//           ) : (
//             <div className="space-y-4">
//               <div className={`w-20 h-20 mx-auto rounded-full flex items-center justify-center transition-all duration-300 ${
//                 isDragActive ? 'bg-blue-100 scale-110' : 'bg-gray-100'
//               }`}>
//                 <Upload className={`w-10 h-10 transition-colors duration-300 ${
//                   isDragActive ? 'text-blue-600' : 'text-gray-400'
//                 }`} />
//               </div>
              
//               <div className="space-y-2">
//                 <h3 className="text-xl font-semibold text-gray-800">
//                   {isDragActive ? 'Drop your video here!' : 'Upload your video'}
//                 </h3>
//                 <p className="text-gray-500">
//                   Drag & drop or click to select • MP4, AVI, MOV, MKV • Max 100MB
//                 </p>
//               </div>
              
//               <button
//                 type="button"
//                 className="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-medium rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all duration-200"
//                 disabled={isUploading}
//               >
//                 <Upload className="w-5 h-5 mr-2" />
//                 Choose File
//               </button>
//             </div>
//           )}
//         </div>
//       </div>
      
//       {error && (
//         <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg flex items-center space-x-2">
//           <AlertCircle className="w-5 h-5 text-red-500" />
//           <span className="text-red-700">{error}</span>
//         </div>
//       )}
//     </div>
//   );
// };

// export default VideoUploader;




import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, Video, AlertCircle } from 'lucide-react';

const VideoUploader = ({ onVideoUploaded, isUploading }) => {
  const [uploadProgress, setUploadProgress] = useState(0);
  const [error, setError] = useState(null);

  const onDrop = useCallback(async (acceptedFiles) => {
    const file = acceptedFiles[0];
    if (!file) return;

    setError(null);
    setUploadProgress(0);
    
    try {
      // Simulate upload progress
      const progressInterval = setInterval(() => {
        setUploadProgress(prev => {
          if (prev >= 90) {
            clearInterval(progressInterval);
            return 90;
          }
          return prev + 10;
        });
      }, 200);

      const result = await onVideoUploaded(file);
      
      clearInterval(progressInterval);
      setUploadProgress(100);
      
      setTimeout(() => setUploadProgress(0), 2000);
      
    } catch (err) {
      setError(err.message || 'Upload failed');
      setUploadProgress(0);
    }
  }, [onVideoUploaded]);

  const { getRootProps, getInputProps, isDragActive, isDragReject } = useDropzone({
    onDrop,
    accept: {
      'video/*': ['.mp4', '.avi', '.mov', '.mkv']
    },
    maxSize: 100 * 1024 * 1024, // 100MB
    multiple: false,
    disabled: isUploading
  });

  return (
    <div className="w-full max-w-2xl mx-auto">
      <div
        {...getRootProps()}
        className={`
          relative border-2 border-dashed rounded-2xl p-12 text-center cursor-pointer
          transition-all duration-300 ease-in-out transform hover:scale-105
          ${isDragActive && !isDragReject 
            ? 'border-blue-400 bg-blue-50' 
            : ''
          }
          ${isDragReject 
            ? 'border-red-400 bg-red-50' 
            : ''
          }
          ${!isDragActive 
            ? 'border-gray-300 hover:border-blue-400 hover:bg-blue-50' 
            : ''
          }
          ${isUploading 
            ? 'opacity-50 cursor-not-allowed' 
            : ''
          }
        `}
      >
        <input {...getInputProps()} />
        
        <div className="space-y-4">
          {uploadProgress > 0 ? (
            <div className="space-y-3">
              <div className="w-16 h-16 mx-auto bg-blue-100 rounded-full flex items-center justify-center">
                <Video className="w-8 h-8 text-blue-600 animate-pulse" />
              </div>
              <div className="w-full bg-gray-200 rounded-full h-3">
                <div 
                  className="bg-gradient-to-r from-blue-500 to-purple-500 h-3 rounded-full transition-all duration-300"
                  style={{ width: `${uploadProgress}%` }}
                />
              </div>
              <p className="text-blue-600 font-medium">
                Uploading... {uploadProgress}%
              </p>
            </div>
          ) : (
            <div className="space-y-4">
              <div className={`w-20 h-20 mx-auto rounded-full flex items-center justify-center transition-all duration-300 ${
                isDragActive ? 'bg-blue-100 scale-110' : 'bg-gray-100'
              }`}>
                <Upload className={`w-10 h-10 transition-colors duration-300 ${
                  isDragActive ? 'text-blue-600' : 'text-gray-400'
                }`} />
              </div>
              
              <div className="space-y-2">
                <h3 className="text-xl font-semibold text-gray-800">
                  {isDragActive ? 'Drop your video here!' : 'Upload your video'}
                </h3>
                <p className="text-gray-500">
                  Drag & drop or click to select • MP4, AVI, MOV, MKV • Max 100MB
                </p>
              </div>
              
              <button
                type="button"
                className="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-medium rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all duration-200 transform hover:scale-105"
                disabled={isUploading}
              >
                <Upload className="w-5 h-5 mr-2" />
                Choose File
              </button>
            </div>
          )}
        </div>
      </div>
      
      {error && (
        <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg flex items-center space-x-2">
          <AlertCircle className="w-5 h-5 text-red-500" />
          <span className="text-red-700">{error}</span>
        </div>
      )}
    </div>
  );
};

export default VideoUploader;

