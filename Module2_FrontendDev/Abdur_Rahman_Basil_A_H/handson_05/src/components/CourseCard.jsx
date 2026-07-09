import "./css/CourseCard.css";

function CourseCard({ name, code, credits, grade,setEnrolledCourse }) {
    return (
        <article className="course-card">
            <h2>{name}</h2>
            <p>Code: {code}</p>
            <p>Credits: {credits}</p>
            <p>Grade: {grade}</p>
            <button onClick={() => setEnrolledCourse(prev => [...prev, { name, code, credits, grade }])}>Enroll</button>
        </article>
    );
}

export default CourseCard;