<script setup>
import { ref } from 'vue'

const particles = ref([...Array(50)].map((_, i) => ({
  id: i,
  width: Math.random() * 300 + 50,
  height: Math.random() * 300 + 50,
  left: Math.random() * 100,
  top: Math.random() * 100,
  duration: Math.random() * 10 + 5,
  delay: Math.random() * 5,
  opacity: Math.random() * 0.3
})))
</script>

<template>
  <div class="fondo-animado">
    <div class="gradient-overlay" />
    <div
      v-for="particle in particles"
      :key="particle.id"
      class="particle"
      :style="{
        width: `${particle.width}px`,
        height: `${particle.height}px`,
        left: `${particle.left}%`,
        top: `${particle.top}%`,
        animationDuration: `${particle.duration}s`,
        animationDelay: `${particle.delay}s`,
        opacity: particle.opacity
      }"
    />
  </div>
</template>

<style scoped>
.fondo-animado {
  position: fixed;
  inset: 0;
  z-index: 0;
}

.gradient-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, 
    rgba(6, 182, 212, 0.1) 0%,
    rgba(168, 85, 247, 0.1) 50%,
    rgba(236, 72, 153, 0.1) 100%
  );
}

.particle {
  position: absolute;
  border-radius: 50%;
  background: rgba(6, 182, 212, 0.2);
  filter: blur(60px);
  animation: pulse 5s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.3;
    transform: scale(1);
  }
  50% {
    opacity: 0.6;
    transform: scale(1.1);
  }
}
</style>