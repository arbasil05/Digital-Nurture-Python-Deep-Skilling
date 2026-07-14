<script setup>
import Header from './components/Header.vue';
</script>

<template>
  <div>
    <Header />
    
    <nav class="nav-menu">
      <router-link to="/">Home</router-link>
      <router-link to="/courses">Courses</router-link>
      <router-link to="/profile">Profile</router-link>
    </nav>

    <main class="page-content">
      <router-view /> 
    </main>
  </div>
</template>

<style scoped>
.nav-menu {
  display: flex;
  justify-content: center;
  gap: 32px;
  padding: 0 24px;
  background-color: var(--color-background);
  border-bottom: 1px solid var(--color-border);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02);
}

.nav-menu a {
  color: var(--color-text);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  padding: 16px 0;
  position: relative;
  opacity: 0.7;
  transition: opacity 0.2s ease, color 0.2s ease;
}

.nav-menu a:hover {
  opacity: 1;
  color: var(--color-heading);
}

/* Vue Router automatically adds this class to the active link! */
.nav-menu a.router-link-active {
  opacity: 1;
  color: #6366f1; /* Premium Indigo */
  font-weight: 600;
}

.nav-menu a.router-link-active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background-color: #6366f1;
  border-radius: 3px 3px 0 0;
}

.page-content {
  padding: 24px;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}
</style>