import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { 
  fetchAllCourses, 
  selectCourses, 
  selectCoursesLoading, 
  selectCoursesError 
} from '../store/coursesSlice';

const CoursesPage = () => {
  const dispatch = useDispatch();
  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  if (loading) {
    return <div>Loading courses...</div>;
  }

  if (error) {
    return <div className="error-message">Error: {error}</div>;
  }

  return (
    <div>
      <h1>Courses List</h1>
      {courses.length === 0 ? (
        <p>No courses found.</p>
      ) : (
        <ul>
          {courses.map(course => (
            <li key={course.id}>{course.title || course.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CoursesPage;
