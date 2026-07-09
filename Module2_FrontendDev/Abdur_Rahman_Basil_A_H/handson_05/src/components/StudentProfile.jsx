import { useState } from "react"

function StudentProfile() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [semester, setSemester] = useState("");
    return (
        <>
            <form>
                <label>Name</label>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                <label>Email</label>
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
                <label>Semester</label>
                <input type="number" value={semester} onChange={(e) => setSemester(e.target.value)} />
            </form>
        </>
    )
}

export default StudentProfile