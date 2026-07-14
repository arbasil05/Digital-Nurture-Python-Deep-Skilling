<script setup>
import { useRoute, useRouter } from 'vue-router';

// Initialize our router hooks
const route = useRoute();
const router = useRouter();

// Step 114: Get the ID from the URL (e.g., /courses/2 -> id is '2')
const courseId = route.params.id;

// A temporary fake course to display until we set up Pinia state
const course = {
  name: `Course ${courseId} Details`,
  description: 'This is a fantastic course that will teach you everything you need to know.'
};

// Step 115: Programmatic Navigation
const handleEnroll = () => {
  // This is exactly like React's navigate('/profile')
  router.push('/profile');
};
</script>

<template>
  <div class="detail-container">
    <h2>{{ course.name }}</h2>
    <p class="course-id">Course ID Reference: {{ courseId }}</p>
    <p>{{ course.description }}</p>
    
    <button @click="handleEnroll" class="enroll-btn">
      Enroll in Course
    </button>
  </div>
</template>

<style scoped>
.detail-container {
  max-width: 600px;
  margin: 40px auto;
  padding: 40px;
  border: 1px solid var(--color-border);
  border-radius: 16px;
  background-color: var(--color-background);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02), 0 1px 3px rgba(0, 0, 0, 0.04);
}

.detail-container h2 {
  font-size: 2rem;
  font-weight: 800;
  color: var(--color-heading);
  margin-bottom: 8px;
  letter-spacing: -0.02em;
}

.course-id {
  color: #6366f1; /* Indigo */
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 24px;
}

.detail-container p {
  font-size: 1.1rem;
  line-height: 1.6;
  color: var(--color-text);
  margin-bottom: 32px;
}

.enroll-btn {
  background-color: #6366f1; /* Indigo */
  color: white;
  border: none;
  padding: 14px 28px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  width: 100%;
  transition: transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 4px 6px rgba(99, 102, 241, 0.2);
}

.enroll-btn:hover {
  background-color: #4f46e5;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(99, 102, 241, 0.25);
}

.enroll-btn:active {
  transform: translateY(0);
}
</style>