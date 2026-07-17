import CourseCard from "./CourseCard";

function CoursesPage({
  courses,
  searchTerm,
  handleSearch,
  loading,
  errorMessage
}) {
  return (
    <div>
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
              id={course.id}
              name={course.name}
              code={course.code}
              credits={course.credits}
              grade={course.grade}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default CoursesPage;
