import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
});

apiClient.interceptors.request.use(
  (config) => {
    const token = 'mock_jwt_token_12345';
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

apiClient.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    const customError = new Error(
      error.response?.data?.message || error.message || 'An unexpected error occurred'
    );
    customError.statusCode = error.response?.status || 500;
    
    return Promise.reject(customError);
  }
);

export default apiClient;
