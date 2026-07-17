import { useDispatch } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import { enroll } from "../redux/enrollmentSlice";
import "./css/CourseCard.css";

function CourseCard({ id, name, code, credits, grade }) {
    const navigate = useNavigate();
    const dispatch = useDispatch();

    const handleEnroll = (e) => {
        e.stopPropagation();
        dispatch(enroll({ id, name, code, credits, grade }));
        navigate("/profile");
    };

    return (
        <article className="course-card">
            <h2>
                <Link to={`/courses/${id}`} style={{ textDecoration: "none", color: "#1e3a8a" }}>
                    {name}
                </Link>
            </h2>
            <p>Code: {code}</p>
            <p>Credits: {credits}</p>
            <p>Grade: {grade}</p>
            <div style={{ display: "flex", gap: "0.5rem", marginTop: "auto", flexDirection: "column" }}>
                <Link to={`/courses/${id}`} style={{
                    fontSize: "0.85rem",
                    color: "#1e3a8a",
                    textDecoration: "underline",
                    textAlign: "center",
                    marginBottom: "0.25rem"
                }}>
                    View Details
                </Link>
                <button onClick={handleEnroll}>Enroll</button>
            </div>
        </article>
    );
}

export default CourseCard;