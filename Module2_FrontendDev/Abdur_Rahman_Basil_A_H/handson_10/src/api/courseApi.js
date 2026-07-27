import apiClient from './apiClient';

export const getAllCourses = async () => {
  return await apiClient.get('/courses');
};

export const getCourseById = async (id) => {
  return await apiClient.get(`/courses/${id}`);
};

export const enrollStudent = async (studentId, courseId) => {
  return await apiClient.post('/enrollments', {
    studentId,
    courseId
  });
};
