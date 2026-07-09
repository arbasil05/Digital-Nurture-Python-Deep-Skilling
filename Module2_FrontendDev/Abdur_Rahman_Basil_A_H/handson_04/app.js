import COURSES from "./data.js";

function fetchUser(id) {
    console.log("Fetched without Async");
    fetch('https://jsonplaceholder.typicode.com/users/' + id)
        .then((res) => res.json())
        .then((data) => {
            console.log(data.username);
        })
}


fetchUser(1);


async function fetchUserAsync(id) {
    try {
        console.log("Fetched using Async");
        const response = await fetch('https://jsonplaceholder.typicode.com/users/' + id);
        const data = await response.json();
        console.log(data.username);
    } catch (error) {
        console.log("Error fetching user :", error);
    }
}


fetchUserAsync(1);

async function fetchAllCourses() {
    await new Promise(resolve => setTimeout(resolve, 1000));
    return COURSES;
}


const courseGrid = document.querySelector(".course-grid");
const courses = [];

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

function showLoading() {
    if (courses.length < 1) {
        courseGrid.innerHTML = "<h1>Loading...</h1>";
    } else {
        courseGrid.innerHTML = "";
    }
}


async function loadCourses() {
    showLoading();
    const res = await fetchAllCourses();
    renderCourses(res);
}

loadCourses();


async function fetchUserIdbyPromiseAll(id) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    return response.json();
}

async function fetchBothUsers() {
    const [user1, user2] = await Promise.all([
        fetchUser(1),
        fetchUser(2)
    ]);

    console.log(user1.name);
    console.log(user2.name);
}

fetchBothUsers();



// TASK 2


async function apiFetch(url) {

    const response = await fetch(url);

    if (!response.ok) {
        throw new Error("Request failed");
    }

    return response.json();

}

let badUrl = "https://jsonplaceholder.typicode.com/posts/wrong";

async function populateNotifications() {
    const notifications = document.getElementById("notifications");
    const retryButton = document.getElementById("retry-button");

    retryButton.addEventListener("click", () => {
        badUrl = "https://jsonplaceholder.typicode.com/posts";
        populateNotifications();
    });

    const existingError = document.getElementById("notifications-error");
    if (existingError) existingError.remove();

    let isLoading = true;
    const loadingMsg = document.createElement("p");
    loadingMsg.id = "notifications-loading";
    loadingMsg.textContent = "Loading notifications...";
    notifications.appendChild(loadingMsg);

    try {
        const posts = await apiFetch(badUrl);
        const limitedPosts = posts.slice(0, 2);
        limitedPosts.forEach((post) => {
            const article = document.createElement("article");
            article.className = "notification-item";
            article.innerHTML = `
                <h2>${post.title}</h2>
                <p>${post.body}</p>
            `;
            notifications.appendChild(article);
        });
    } catch (error) {
        console.log("Error fetching notifications:", error);
        const errorMsg = document.createElement("p");
        errorMsg.id = "notifications-error";
        errorMsg.textContent = "Failed to load notifications.";
        notifications.appendChild(errorMsg);
    } finally {
        isLoading = false;
        const loader = document.getElementById("notifications-loading");
        if (loader) loader.remove();
    }
}

populateNotifications();

