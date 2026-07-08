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
    article.innerHTML = `
        <h2>${course.name}</h2>
        <p>${course.code}</p>
        <p>${course.credits} credits</p>
    `;
    return article;
}

function renderCourses(courses) {
    courseGrid.replaceChildren();
    if (courses.length < 1) {
        courseGrid.innerHTML = "<h1>No course Found</h1>";
        return;
    }
    courses.forEach((course) => courseGrid.appendChild(createCourseCard(course)));
}

courseGrid.addEventListener("click", (event) => {
    const card = event.target.closest(".course-card");
    if (!card) return;
    alert(`${card.dataset.name} (${card.dataset.code})`);
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
