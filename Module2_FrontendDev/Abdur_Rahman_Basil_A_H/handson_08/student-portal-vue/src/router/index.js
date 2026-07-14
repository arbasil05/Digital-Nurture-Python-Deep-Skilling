import { createRouter, createWebHistory } from 'vue-router'

// Step 112: Define the routes
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/courses',
      name: 'courses',
      component: () => import('../views/CoursesView.vue') // From Task 1
    },
    {
      path: '/courses/:id',
      name: 'course-detail',
      component: () => import('../views/CourseDetailView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    }
  ]
})

// Step 116: Navigation Guard (Similar to a global middleware/useEffect in React)
// This runs before every route change.
router.beforeEach((to, from) => {
  console.log(`Navigating to: ${to.path}`)
})

export default router