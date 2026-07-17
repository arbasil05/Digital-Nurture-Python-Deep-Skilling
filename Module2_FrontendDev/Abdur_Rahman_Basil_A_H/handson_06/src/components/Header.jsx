import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import "./css/Header.css";

function Header({ title }) {
    const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);

    return (
        <header className="header">
            <h1>{title}</h1>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/courses">Courses</Link></li>
                    <li><Link to="/profile">Profile</Link></li>
                </ul>
            </nav>
            <p>Enrolled Course : {enrolledCourses.length}</p>
        </header>
    );
}

export default Header;