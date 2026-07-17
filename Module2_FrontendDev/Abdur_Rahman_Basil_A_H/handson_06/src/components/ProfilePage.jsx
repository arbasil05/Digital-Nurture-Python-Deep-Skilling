import { useSelector, useDispatch } from "react-redux";
import StudentProfile from "./StudentProfile";
import { unenroll } from "../redux/enrollmentSlice";
import "./css/ProfilePage.css";

function ProfilePage() {
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);
  const dispatch = useDispatch();

  return (
    <div className="profile-container">
      <section className="profile-section">
        <h3>Student Profile</h3>
        <StudentProfile />
      </section>

      <section className="profile-section">
        <h3>Enrolled Courses</h3>
        {enrolledCourses.length === 0 ? (
          <p style={{ color: "#6b7280", fontStyle: "italic", margin: 0 }}>
            No courses enrolled yet.
          </p>
        ) : (
          <div className="enrolled-list">
            {enrolledCourses.map((course, index) => (
              <div key={index} className="enrolled-item">
                <div className="enrolled-item-details">
                  <h4>{course.name}</h4>
                  <p>Code: {course.code} | Credits: {course.credits}</p>
                </div>
                <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
                  {course.grade && (
                    <span className="enrolled-item-badge">
                      Grade: {course.grade}
                    </span>
                  )}
                  <button 
                    className="unenroll-btn"
                    onClick={() => dispatch(unenroll(course.id))}
                  >
                    Un-enroll
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}

export default ProfilePage;
