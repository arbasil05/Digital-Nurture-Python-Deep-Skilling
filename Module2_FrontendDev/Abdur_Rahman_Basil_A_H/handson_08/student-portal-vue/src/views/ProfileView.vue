<script setup>
import { useEnrollmentStore } from '../stores/enrollment';

const store = useEnrollmentStore();
</script>

<template>
  <div class="profile-page">
    <div class="page-header">
      <h1 class="page-title">My Profile</h1>
      <p class="page-subtitle">Manage your enrolled courses and review your academic progress.</p>
    </div>
    
    <div class="summary-card">
      <div class="summary-label">Total Credits Enrolled</div>
      <div class="summary-value">{{ store.totalCredits }}</div>
    </div>

    <div class="enrolled-section">
      <h3 class="section-title">Enrolled Courses</h3>
      
      <div v-if="store.enrolledCourses.length > 0" class="enrolled-list">
        <div v-for="course in store.enrolledCourses" :key="course.id" class="enrolled-item">
          <div class="course-info">
            <span class="course-code">{{ course.code }}</span>
            <h4 class="course-name">{{ course.name }}</h4>
            <div class="course-meta">
              <span class="credits">{{ course.credits }} Credits</span>
            </div>
          </div>
          <button @click="store.unenroll(course.id)" class="unenroll-btn">Remove</button>
        </div>
      </div>
      
      <div v-else class="empty-state">
        <div class="empty-icon">📚</div>
        <h3>No courses enrolled</h3>
        <p>You haven't enrolled in any courses yet. Browse the courses page to get started.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-page {
  padding: 40px 24px;
  max-width: 800px;
  margin: 0 auto;
}

.page-header {
  margin-bottom: 40px;
}

.page-title {
  font-size: 2rem;
  font-weight: 800;
  color: var(--color-heading);
  margin-bottom: 8px;
  letter-spacing: -0.03em;
}

.page-subtitle {
  color: var(--color-text);
  font-size: 1.1rem;
  opacity: 0.8;
  margin: 0;
}

.summary-card {
  background-color: #e0e7ff; /* Soft Indigo */
  padding: 32px;
  border-radius: 16px;
  margin-bottom: 48px;
  text-align: center;
  border: 1px solid #c7d2fe;
}

.summary-label {
  font-size: 0.95rem;
  font-weight: 600;
  color: #4f46e5;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 8px;
}

.summary-value {
  font-size: 3rem;
  font-weight: 800;
  color: #3730a3;
  line-height: 1;
}

.section-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-heading);
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--color-border);
}

.enrolled-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.enrolled-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px;
  background-color: var(--color-background);
  border: 1px solid var(--color-border);
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.enrolled-item:hover {
  transform: translateX(4px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.04);
  border-color: var(--color-border-hover);
}

.course-info {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.course-code {
  font-size: 0.75rem;
  font-weight: 700;
  color: #6366f1;
  text-transform: uppercase;
}

.course-name {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--color-heading);
  margin: 0;
}

.course-meta {
  font-size: 0.85rem;
  color: var(--color-text);
  opacity: 0.8;
}

.unenroll-btn {
  background-color: #fee2e2;
  color: #b91c1c;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.unenroll-btn:hover {
  background-color: #fca5a5;
  color: #991b1b;
}

.empty-state {
  text-align: center;
  padding: 48px 24px;
  background-color: var(--color-background-soft);
  border-radius: 12px;
  border: 1px dashed var(--color-border);
}

.empty-icon {
  font-size: 40px;
  margin-bottom: 16px;
}

.empty-state h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--color-heading);
  margin-bottom: 8px;
}

.empty-state p {
  color: var(--color-text);
  opacity: 0.7;
  font-size: 0.95rem;
}
</style>