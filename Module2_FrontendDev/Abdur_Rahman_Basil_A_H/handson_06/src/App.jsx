import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import Footer from "./components/Footer";
import Header from "./components/Header";
import COURSES from "../public/data";
import HomePage from "./components/HomePage";
import CoursesPage from "./components/CoursesPage";
import ProfilePage from "./components/ProfilePage";
import CourseDetailPage from "./components/CourseDetailPage";
import "./App.css";

function App() {

  const [courses, setCourses] = useState(COURSES);
  const [searchTerm, setSearchTerm] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        setLoading(true);
        const response = await fetch("https://jsonplaceholder.typicode.com/posts");
        const jsonCourse = await response.json();

        // Fix: (course, index) — first arg is the item, second is the index
        const merged = COURSES.map((course, index) => ({
          ...jsonCourse[index],
          id: course.id,
          name: course.name,
          credits: course.credits,
          code: course.code,
          grade: course.grade,
        }));

        setCourses(merged);
      } catch (error) {
        console.log("error: ", error);
        setErrorMessage("Error loading course data");
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);

  // The dependency array of useEffect deteremines when this sideeffect will
  // get executed, so when the courses array changes, this sideeffect will be executed
  // An empty dependency array means this sideeffect will only be executed once
  // If the dependency array is omitted, the sideeffect will be executed after every render
  // If no dependency array is provided, the effect will run after every render.
  useEffect(() => {
    console.log("Course changed");
  }, [courses])

  const handleSearch = (e) => {
    const value = e.target.value;
    setSearchTerm(value);
    setCourses(COURSES.filter((course) =>
      course.name.toLowerCase().includes(value.toLowerCase())
    ));
  };

  return (
    <div className="app-container">
      <Header title="Student Portal" />

      <main className="main-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route 
            path="/courses" 
            element={
              <CoursesPage 
                courses={courses}
                searchTerm={searchTerm}
                handleSearch={handleSearch}
                loading={loading}
                errorMessage={errorMessage}
              />
            } 
          />
          <Route 
            path="/profile" 
            element={<ProfilePage />} 
          />
          <Route 
            path="/courses/:courseId" 
            element={
              <CourseDetailPage 
                courses={courses}
              />
            } 
          />
        </Routes>
      </main>

      <Footer />
    </div>
  );
}

export default App;