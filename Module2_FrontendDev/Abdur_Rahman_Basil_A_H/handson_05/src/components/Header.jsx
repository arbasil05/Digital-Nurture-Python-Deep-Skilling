import "./css/Header.css";

function Header({ title,count }) {
    return (
        <header className="header">
            <h1>{title}</h1>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Courses</a></li>
                    <li><a href="#">Profile</a></li>
                </ul>
            </nav>
            <p>Enrolled Course : {count}</p>
        </header>
    );
}

export default Header;