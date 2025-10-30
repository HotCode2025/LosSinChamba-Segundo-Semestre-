<script setup>
import { ref } from 'vue'
import TeamCard from './TeamCard.vue'

const team = ref([
  { name: 'Lautaro Martínez', role: 'Full Stack Developer', color: '#06b6d4' },
  { name: 'Leandro Orozco', role: 'Frontend Specialist', color: '#8b5cf6' },
  { name: 'Gabriel Maculus', role: 'Backend Engineer', color: '#ec4899' },
  { name: 'Kevin Castilla', role: 'UI/UX Developer', color: '#f59e0b' },
  { name: 'Mariano Rasgido', role: 'DevOps Engineer', color: '#10b981' },
  { name: 'Ezequiel Díaz', role: 'Mobile Developer', color: '#ef4444' }
])
</script>

<template>
  <div class="equipo-section">
    <div class="equipo-container">
      <h2 class="section-title">Nuestro Equipo</h2>
      <div class="team-grid">
        <TeamCard
          v-for="(member, index) in team"
          :key="index"
          :member="member"
          :index="index"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.equipo-section {
  min-height: 100vh;
  padding: 5rem 1rem;
}

.equipo-container {
  max-width: 80rem;
  margin: 0 auto;
}

.section-title {
  font-size: 3rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 4rem;
  background: linear-gradient(to right, #06b6d4, #a855f7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.team-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

@media (min-width: 640px) {
  .team-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .team-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>