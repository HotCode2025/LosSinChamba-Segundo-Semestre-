<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

defineProps({
  activeSection: String
})

const emit = defineEmits(['update:activeSection'])
const menuOpen = ref(false)

const scrollToSection = (id) => {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
  menuOpen.value = false
}

const handleScroll = () => {
  const sections = ['inicio', 'equipo', 'habilidades', 'contacto']
  const current = sections.find(section => {
    const element = document.getElementById(section)
    if (element) {
      const rect = element.getBoundingClientRect()
      return rect.top <= 100 && rect.bottom >= 100
    }
    return false
  })
  if (current) emit('update:activeSection', current)
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <nav class="navbar">
    <div class="nav-container">
      <div class="nav-content">
        <div class="nav-logo">
          <i class="fas fa-code"></i>
          <span class="logo-text">LosSinChamba</span>
        </div>

        <div class="nav-menu desktop-menu">
          <button
            v-for="section in ['inicio', 'equipo', 'habilidades', 'contacto']"
            :key="section"
            @click="scrollToSection(section)"
            :class="['nav-button', { active: activeSection === section }]"
          >
            {{ section }}
          </button>
        </div>

        <button @click="menuOpen = !menuOpen" class="mobile-menu-button">
          <i :class="menuOpen ? 'fas fa-times' : 'fas fa-bars'"></i>
        </button>
      </div>
    </div>

    <div v-if="menuOpen" class="mobile-menu">
      <div class="mobile-menu-content">
        <button
          v-for="section in ['inicio', 'equipo', 'habilidades', 'contacto']"
          :key="section"
          @click="scrollToSection(section)"
          class="mobile-nav-button"
        >
          {{ section }}
        </button>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
  background: rgba(2, 6, 23, 0.8);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(6, 182, 212, 0.2);
}

.nav-container {
  max-width: 80rem;
  margin: 0 auto;
  padding: 0 1rem;
}

.nav-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 4rem;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-logo i {
  font-size: 2rem;
  color: #06b6d4;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  background: linear-gradient(to right, #06b6d4, #a855f7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.desktop-menu {
  display: none;
  gap: 2rem;
}

.nav-button {
  background: none;
  border: none;
  color: #cbd5e1;
  font-size: 1rem;
  cursor: pointer;
  text-transform: capitalize;
  transition: color 0.3s;
  padding: 0.5rem 0;
}

.nav-button:hover,
.nav-button.active {
  color: #06b6d4;
}

.mobile-menu-button {
  display: block;
  background: none;
  border: none;
  color: #cbd5e1;
  font-size: 1.25rem;
  cursor: pointer;
}

.mobile-menu {
  background: rgba(15, 23, 42, 0.95);
  backdrop-filter: blur(20px);
  border-top: 1px solid rgba(6, 182, 212, 0.2);
}

.mobile-menu-content {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.mobile-nav-button {
  background: none;
  border: none;
  color: #cbd5e1;
  font-size: 1rem;
  cursor: pointer;
  text-align: left;
  text-transform: capitalize;
  padding: 0.5rem;
  transition: color 0.3s;
}

.mobile-nav-button:hover {
  color: #06b6d4;
}

@media (min-width: 768px) {
  .desktop-menu {
    display: flex;
  }
  
  .mobile-menu-button {
    display: none;
  }
}
</style>