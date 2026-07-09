import { useEffect, useState } from "react";
import Footer from "./components/Footer";
import Header from "./components/Header";
import COURSES from "../public/data";
import CourseCard from "./components/CourseCard";
import "./App.css";

function App() {

  const [courses, setCourses] = useState(COURSES);
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourse, setEnrolledCourse] = useState([]);
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
    <>
      <Header title="Student Portal" count={enrolledCourse.length} />

      <main className="main-content">
        <div className="controls">
          <input
            type="text"
            id="search-course"
            placeholder="Search courses by name..."
            value={searchTerm}
            onChange={(e) => handleSearch(e)}
          />
        </div>

        {loading && (
          <p className="status-loading">Loading course data...</p>
        )}

        {errorMessage && (
          <p className="status-error">{errorMessage}</p>
        )}

        {!loading && !errorMessage && courses.length === 0 && (
          <p className="status-empty">No courses found.</p>
        )}

        {!loading && (
          <div className="course-grid">
            {courses.map((course) => (
              <CourseCard
                key={course.id}
                name={course.name}
                code={course.code}
                credits={course.credits}
                grade={course.grade}
                setEnrolledCourse={setEnrolledCourse}
              />
            ))}
          </div>
        )}
      </main>

      <Footer />
    </>
  );
}

export default App;