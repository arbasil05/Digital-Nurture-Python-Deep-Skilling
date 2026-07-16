import COURSES from "./data.js";

for (const course of COURSES) {
    const { name, credits } = course;
    console.log(name, credits);
}

const formatedCourse = COURSES.map((course) => {
    const { code, name, credits } = course;
    return `${code}--${name}(${credits} credits)`;
});

console.log(formatedCourse);

const filteredCourse = COURSES.filter((course) => course.credits >= 4);

console.log("Courses with a minimum of 4 credits : ", filteredCourse.length);

const totalCredits = COURSES.reduce((acc, course) => acc + course.credits, 0);

console.log("Total Credits enrolled : ", totalCredits);

COURSES.forEach((course) => {
    console.log(`${course.code} — ${course.name} (${course.credits} credits)`);
});

const courseGrid = document.querySelector(".course-grid");
const creditsDisplay = document.getElementById("total-credits");

function createCourseCard(course) {
    const article = document.createElement("article");
    article.className = "course-card";
    article.dataset.name = course.name;
    article.dataset.code = course.code;
    article.setAttribute("role", "button");
    article.setAttribute("tabindex", "0");
    article.innerHTML = `
        <h3>${course.name}</h3>
        <p>${course.code}</p>
        <p>${course.credits} credits</p>
    `;
    return article;
}

function renderCourses(courses) {
    courseGrid.replaceChildren();
    
    const resultsCount = document.getElementById("results-count");
    if (resultsCount) {
        resultsCount.textContent = `${courses.length} course${courses.length !== 1 ? 's' : ''} found`;
    }

    if (courses.length < 1) {
        courseGrid.innerHTML = "<p>No course Found</p>";
        return;
    }
    courses.forEach((course) => courseGrid.appendChild(createCourseCard(course)));
}

courseGrid.addEventListener("click", (event) => {
    const card = event.target.closest(".course-card");
    if (!card) return;
    alert(`${card.dataset.name} (${card.dataset.code})`);
});

courseGrid.addEventListener("keydown", (event) => {
    if (event.key === "Enter" || event.key === " ") {
        const card = event.target.closest(".course-card");
        if (!card) return;
        event.preventDefault();
        alert(`${card.dataset.name} (${card.dataset.code})`);
    }
});

renderCourses(COURSES);

creditsDisplay.innerText =
    "Total Credits : " + COURSES.reduce((acc, course) => acc + course.credits, 0);

const searchBar = document.getElementById("search-course");

searchBar.addEventListener("input", (event) => {
    const query = event.target.value.toLowerCase();
    const filtered = COURSES.filter((course) =>
        course.name.toLowerCase().startsWith(query)
    );
    renderCourses(filtered);
});

const sortButton = document.querySelector(".sort-button");

sortButton.addEventListener("click", () => {
    const sorted = [...COURSES].sort((a, b) => b.credits - a.credits);
    renderCourses(sorted);
});
