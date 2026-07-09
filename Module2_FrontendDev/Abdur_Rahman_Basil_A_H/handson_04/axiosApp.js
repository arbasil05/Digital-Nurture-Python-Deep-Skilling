axios.interceptors.request.use((config) => {
    console.log(`API call started: ${config.url}`);
    return config;
});



async function apiFetch(url, params = {}) {
    const response = await axios.get(url, { params });
    return response.data;
}

async function fetchPostsByUser() {
    try {
        const posts = await apiFetch("https://jsonplaceholder.typicode.com/posts", { userId: 1 });
        console.log(`Fetched ${posts.length} posts for userId 1`);
        console.log(posts);
    } catch (error) {
        console.error("Error fetching posts by user:", error.message);
    }
}

fetchPostsByUser();