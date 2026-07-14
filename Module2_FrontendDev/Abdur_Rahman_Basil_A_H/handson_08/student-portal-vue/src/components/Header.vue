<script setup>
import { useEnrollmentStore } from '../stores/enrollment';

const store = useEnrollmentStore();
</script>

<template>
  <header class="header">
    <div class="header-container">
      <div class="logo">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 2L2 7L12 12L22 7L12 2Z" fill="#6366f1"/>
          <path d="M2 17L12 22L22 17" stroke="#6366f1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M2 12L12 17L22 12" stroke="#6366f1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <h2>Student Portal</h2>
      </div>
      
      <div class="course-count">
        Enrolled Courses: <strong class="count-badge">{{ store.enrolledCourses.length }}</strong>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  background-color: var(--color-background);
  border-bottom: 1px solid var(--color-border);
  position: sticky;
  top: 0;
  z-index: 10;
  box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo h2 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-heading);
  margin: 0;
  letter-spacing: -0.02em;
}

.course-count {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: var(--color-background-soft);
  color: var(--color-text);
  padding: 8px 16px;
  border-radius: 24px;
  font-size: 0.9rem;
  font-weight: 500;
  border: 1px solid var(--color-border);
}

.count-badge {
  background-color: #6366f1; /* Premium Indigo */
  color: white;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.85rem;
}
</style>