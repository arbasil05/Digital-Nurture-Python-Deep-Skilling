import { useState } from "react"
import "./css/StudentProfile.css";

function StudentProfile() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [semester, setSemester] = useState("");
    return (
        <form className="profile-form">
            <div className="form-group">
                <label>Name</label>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            </div>
            <div className="form-group">
                <label>Email</label>
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            </div>
            <div className="form-group">
                <label>Semester</label>
                <input type="number" value={semester} onChange={(e) => setSemester(e.target.value)} />
            </div>
        </form>
    )
}

export default StudentProfile