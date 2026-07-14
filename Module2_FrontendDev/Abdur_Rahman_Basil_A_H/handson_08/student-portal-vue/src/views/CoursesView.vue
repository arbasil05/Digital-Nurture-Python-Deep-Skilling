<script setup>
import { ref, onMounted, computed } from 'vue';
import CourseCard from '../components/CourseCard.vue';
import { useEnrollmentStore } from '../stores/enrollment';

// 1. Initialize the store (just like a custom hook in React)
const store = useEnrollmentStore();

const searchTerm = ref('');
const courses = ref([]);

onMounted(() => {
  courses.value = [
    { id: 1, name: 'Introduction to Vue', code: 'CS101', credits: 3, grade: 'A' },
    { id: 2, name: 'Advanced React', code: 'CS201', credits: 4, grade: 'B+' },
    { id: 3, name: 'Data Structures', code: 'CS301', credits: 4, grade: 'A-' },
    { id: 4, name: 'Web Design', code: 'DS105', credits: 2, grade: 'A' },
    { id: 5, name: 'Database Systems', code: 'CS404', credits: 3, grade: 'B' }
  ];
});

const filteredCourses = computed(() => {
  return courses.value.filter(course => 
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});
</script>

<template>
  <div class="courses-page">
    <div class="page-header">
      <div>
        <h1 class="page-title">Available Courses</h1>
        <p class="page-subtitle">Browse and enroll in new courses for the upcoming semester.</p>
      </div>
      
      <div class="search-wrapper">
        <svg class="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M11 19C15.4183 19 19 15.4183 19 11C19 6.58172 15.4183 3 11 3C6.58172 3 3 6.58172 3 11C3 15.4183 6.58172 19 11 19Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M21 21L16.65 16.65" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <input 
          v-model="searchTerm" 
          type="text" 
          placeholder="Search courses by name..." 
          class="search-box"
        />
      </div>
    </div>

    <div v-if="filteredCourses.length > 0" class="course-grid">
      <div v-for="course in filteredCourses" :key="course.id" class="course-wrapper">
        <CourseCard 
          :name="course.name"
          :code="course.code"
          :credits="course.credits"
          :grade="course.grade"
        />
        <button @click="store.enroll(course)" class="enroll-btn">
          Enroll Now
        </button>
      </div>
    </div>
    
    <div v-else class="empty-state">
      <div class="empty-icon">🔍</div>
      <h3>No courses found</h3>
      <p>We couldn't find any courses matching "{{ searchTerm }}"</p>
      <button @click="searchTerm = ''" class="clear-btn">Clear Search</button>
    </div>
  </div>
</template>

<style scoped>
.courses-page {
  padding: 40px 24px;
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-bottom: 40px;
}

@media (min-width: 768px) {
  .page-header {
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-end;
  }
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

.search-wrapper {
  position: relative;
  width: 100%;
  max-width: 400px;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--color-text);
  opacity: 0.5;
}

.search-box {
  width: 100%;
  padding: 14px 16px 14px 48px;
  font-size: 1rem;
  background-color: var(--color-background);
  border: 1px solid var(--color-border);
  border-radius: 12px;
  color: var(--color-text);
  transition: all 0.2s ease;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02);
}

.search-box:focus {
  outline: none;
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
}

.search-box::placeholder {
  color: var(--color-text);
  opacity: 0.4;
}

.course-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}

@media (min-width: 640px) {
  .course-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .course-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.course-wrapper {
  display: flex;
  flex-direction: column;
  position: relative;
}

/* Ensure CourseCard grows to fill space above the button */
.course-wrapper > :first-child {
  flex: 1;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
  border-bottom: none;
  margin-bottom: 0;
}

.enroll-btn {
  background-color: #6366f1;
  color: white;
  border: 1px solid var(--color-border);
  border-top: none;
  padding: 16px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  transition: background-color 0.2s ease;
  width: 100%;
}

.enroll-btn:hover {
  background-color: #4f46e5;
}

.empty-state {
  text-align: center;
  padding: 64px 24px;
  background-color: var(--color-background-soft);
  border-radius: 16px;
  border: 1px dashed var(--color-border);
}

.empty-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.empty-state h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--color-heading);
  margin-bottom: 8px;
}

.empty-state p {
  color: var(--color-text);
  opacity: 0.7;
  margin-bottom: 24px;
}

.clear-btn {
  background-color: #6366f1;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.2s ease;
}

.clear-btn:hover {
  background-color: #4f46e5;
  transform: translateY(-1px);
}
</style>