import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

// We name it useEnrollmentStore (like a React custom hook: useSomething)
export const useEnrollmentStore = defineStore('enrollment', () => {
  
  // 1. STATE (Just like React useState)
  const enrolledCourses = ref([])

  // 2. GETTERS (Just like React useMemo - recalculates only when state changes)
  const totalCredits = computed(() => {
    return enrolledCourses.value.reduce((total, course) => total + course.credits, 0)
  })

  // 3. ACTIONS (Just normal JavaScript functions!)
  const enroll = (course) => {
    // Check if they are already enrolled so we don't add duplicates
    const alreadyEnrolled = enrolledCourses.value.find(c => c.id === course.id)
    if (!alreadyEnrolled) {
      enrolledCourses.value.push(course)
    }
  }

  const unenroll = (courseId) => {
    enrolledCourses.value = enrolledCourses.value.filter(c => c.id !== courseId)
  }

  // Finally, return everything you want components to be able to use
  return { 
    enrolledCourses, 
    totalCredits, 
    enroll, 
    unenroll 
  }
})