import { Link } from "react-router-dom";

function HomePage() {
  return (
    <div style={{ textAlign: "center", padding: "2.5rem 1.5rem", fontFamily: "Georgia, serif" }}>
      <h2 style={{ color: "#1e3a8a", fontSize: "2rem", marginBottom: "1rem" }}>
        Welcome to the Student Portal
      </h2>
      <p style={{ color: "#555", fontSize: "1.1rem", maxWidth: "600px", margin: "0 auto 2.5rem", lineHeight: "1.6" }}>
        Manage your academic journey, browse available courses, track your grades, and monitor your enrollment details in one place.
      </p>
      
      <div style={{ display: "flex", justifyContent: "center", gap: "1.5rem", flexWrap: "wrap" }}>
        <Link 
          to="/courses" 
          style={{
            textDecoration: "none",
            backgroundColor: "#1e3a8a",
            color: "white",
            padding: "0.75rem 1.5rem",
            borderRadius: "6px",
            fontSize: "1rem",
            fontWeight: "bold",
            transition: "background-color 0.2s",
            border: "1px solid #1e3a8a"
          }}
          onMouseOver={(e) => e.target.style.backgroundColor = "#1d4ed8"}
          onMouseOut={(e) => e.target.style.backgroundColor = "#1e3a8a"}
        >
          Browse Courses
        </Link>
        <Link 
          to="/profile" 
          style={{
            textDecoration: "none",
            backgroundColor: "white",
            color: "#1e3a8a",
            padding: "0.75rem 1.5rem",
            borderRadius: "6px",
            fontSize: "1rem",
            fontWeight: "bold",
            border: "2px solid #1e3a8a",
            transition: "all 0.2s"
          }}
          onMouseOver={(e) => {
            e.target.style.backgroundColor = "#1e3a8a";
            e.target.style.color = "white";
          }}
          onMouseOut={(e) => {
            e.target.style.backgroundColor = "white";
            e.target.style.color = "#1e3a8a";
          }}
        >
          View Profile
        </Link>
      </div>
    </div>
  );
}

export default HomePage;
