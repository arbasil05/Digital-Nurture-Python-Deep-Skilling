import { useDispatch } from "react-redux";
import { useParams, useNavigate, Link } from "react-router-dom";
import { enroll } from "../redux/enrollmentSlice";
import COURSES from "../../public/data";

function CourseDetailPage({ courses }) {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  // Find the course in the fetched list or fallback to static data
  const course = (courses || []).find((c) => c.id === courseId) || COURSES.find((c) => c.id === courseId);

  if (!course) {
    return (
      <div style={{ padding: "2rem", textAlign: "center", fontFamily: "Georgia, serif" }}>
        <h3 style={{ color: "#b91c1c" }}>Course Not Found</h3>
        <p style={{ color: "#555" }}>The requested course does not exist.</p>
        <Link to="/courses" style={{ color: "#1e3a8a", textDecoration: "underline" }}>
          Back to Courses
        </Link>
      </div>
    );
  }

  const handleEnroll = () => {
    dispatch(enroll({
      id: course.id,
      name: course.name,
      code: course.code,
      credits: course.credits,
      grade: course.grade,
    }));
    // Navigate automatically to /profile
    navigate("/profile");
  };

  return (
    <div style={{ fontFamily: "Georgia, serif", maxWidth: "600px", margin: "0 auto", padding: "1rem" }}>
      <Link to="/courses" style={{ 
        display: "inline-block", 
        marginBottom: "1.5rem", 
        color: "#1e3a8a", 
        textDecoration: "none",
        fontSize: "0.9rem" 
      }}>
        &larr; Back to Courses
      </Link>

      <div style={{
        backgroundColor: "white",
        border: "1px solid #d0d7e5",
        borderRadius: "8px",
        padding: "2rem",
        boxShadow: "0 4px 12px rgba(30, 58, 138, 0.08)"
      }}>
        <h2 style={{ color: "#1e3a8a", margin: "0 0 1rem 0", fontSize: "1.75rem" }}>{course.name}</h2>
        
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem", marginBottom: "1.5rem" }}>
          <div>
            <strong style={{ color: "#6b7280", fontSize: "0.85rem", display: "block" }}>COURSE CODE</strong>
            <span style={{ fontSize: "1.1rem", fontWeight: "bold", color: "#374151" }}>{course.code}</span>
          </div>
          <div>
            <strong style={{ color: "#6b7280", fontSize: "0.85rem", display: "block" }}>CREDITS</strong>
            <span style={{ fontSize: "1.1rem", fontWeight: "bold", color: "#374151" }}>{course.credits}</span>
          </div>
        </div>

        {course.grade && (
          <div style={{ marginBottom: "1.5rem" }}>
            <strong style={{ color: "#6b7280", fontSize: "0.85rem", display: "block" }}>GRADE REQUIREMENT</strong>
            <span style={{ fontSize: "1.1rem", fontWeight: "bold", color: "#374151" }}>{course.grade}</span>
          </div>
        )}

        {course.body && (
          <div style={{ marginBottom: "2rem", borderTop: "1px solid #e5e7eb", paddingTop: "1.5rem" }}>
            <strong style={{ color: "#6b7280", fontSize: "0.85rem", display: "block", marginBottom: "0.5rem" }}>
              COURSE DESCRIPTION
            </strong>
            <p style={{ color: "#4b5563", lineHeight: "1.6", margin: 0 }}>
              {course.body}
            </p>
          </div>
        )}

        <button 
          onClick={handleEnroll}
          style={{
            width: "100%",
            padding: "0.75rem",
            backgroundColor: "#1e3a8a",
            color: "white",
            border: "none",
            borderRadius: "6px",
            fontSize: "1rem",
            fontWeight: "bold",
            cursor: "pointer",
            transition: "background-color 0.2s"
          }}
          onMouseOver={(e) => e.target.style.backgroundColor = "#1d4ed8"}
          onMouseOut={(e) => e.target.style.backgroundColor = "#1e3a8a"}
        >
          Enroll in Course
        </button>
      </div>
    </div>
  );
}

export default CourseDetailPage;
