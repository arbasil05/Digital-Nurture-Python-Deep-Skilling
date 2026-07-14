<script setup>

defineProps({
    name: String,
    code: String,
    credits: Number,
    grade: String
})

</script>

<template>
  <div class="card">
    <div class="card-header">
      <span class="course-code">{{ code }}</span>
      <h3 class="course-name">{{ name }}</h3>
    </div>
    <div class="card-body">
      <div class="metric">
        <span class="label">Credits</span>
        <span class="value">{{ credits }}</span>
      </div>
      <div class="metric">
        <span class="label">Grade</span>
        <span class="value grade-badge" :class="grade.charAt(0).toLowerCase()">{{ grade }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  background-color: var(--color-background);
  border: 1px solid var(--color-border);
  border-radius: 12px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02), 0 1px 3px rgba(0, 0, 0, 0.04);
  cursor: pointer;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.06), 0 4px 8px rgba(0, 0, 0, 0.04);
  border-color: #6366f1; /* Indigo focus color */
}

.card-header {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.course-code {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #6366f1;
}

.course-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--color-heading);
  margin: 0;
  line-height: 1.3;
}

.card-body {
  display: flex;
  justify-content: flex-start;
  gap: 32px;
  margin-top: auto;
  border-top: 1px solid var(--color-border);
  padding-top: 16px;
}

.metric {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.label {
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--color-text);
  opacity: 0.7;
  text-transform: uppercase;
}

.value {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-heading);
}

.grade-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 2px 8px;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 700;
}

/* Flat colors for grades, no gradients */
.grade-badge.a { background-color: #dcfce7; color: #166534; }
.grade-badge.b { background-color: #dbeafe; color: #1e40af; }
.grade-badge.c { background-color: #fef9c3; color: #854d0e; }
.grade-badge.d { background-color: #ffedd5; color: #9a3412; }
.grade-badge.f { background-color: #fee2e2; color: #991b1b; }
</style>