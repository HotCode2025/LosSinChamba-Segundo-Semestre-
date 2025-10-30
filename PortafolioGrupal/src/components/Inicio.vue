<script setup>
const scrollToSection = (id) => {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <div class="inicio-section">
    <div class="inicio-content">
      <div class="logo-container">
        <img 
          src="/LosSinChamba.png" 
          alt="LosSinChamba Logo" 
          class="logo-image"
        />
      </div>
      <h1 class="titulo-principal">LosSinChamba</h1>
      <p class="subtitulo">
        Equipo de desarrollo de software enfocado en crear soluciones innovadoras
      </p>
      <div class="botones-container">
        <button @click="scrollToSection('equipo')" class="btn-primary">
          Conoce al Equipo
        </button>
        <button @click="scrollToSection('contacto')" class="btn-secondary">
          Contáctanos
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.inicio-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

.inicio-content {
  text-align: center;
  max-width: 64rem;
  margin: 0 auto;
}

.logo-container {
  margin-bottom: 2rem;
  display: flex;
  justify-content: center;
}

.logo-image {
  width: 200px;
  height: 200px;
  object-fit: contain;
  filter: drop-shadow(0 0 30px rgba(6, 182, 212, 0.6))
          drop-shadow(0 0 60px rgba(168, 85, 247, 0.4));
  animation: float 4s ease-in-out infinite, glow 3s ease-in-out infinite;
  transition: transform 0.3s ease;
}

.logo-image:hover {
  transform: scale(1.1) rotate(5deg);
  filter: drop-shadow(0 0 40px rgba(6, 182, 212, 0.8))
          drop-shadow(0 0 80px rgba(168, 85, 247, 0.6))
          drop-shadow(0 0 100px rgba(236, 72, 153, 0.4));
}

.titulo-principal {
  font-size: 4rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  background: linear-gradient(to right, #06b6d4, #a855f7, #ec4899);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: pulse 3s ease-in-out infinite;
}

.subtitulo {
  font-size: 1.5rem;
  color: #cbd5e1;
  margin-bottom: 2rem;
}

.botones-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.btn-primary,
.btn-secondary {
  padding: 0.75rem 2rem;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 9999px;
  cursor: pointer;
  transition: transform 0.3s;
  border: none;
}

.btn-primary {
  background: linear-gradient(to right, #06b6d4, #a855f7);
  color: white;
}

.btn-primary:hover {
  transform: scale(1.05);
}

.btn-secondary {
  background: transparent;
  border: 2px solid #06b6d4;
  color: #06b6d4;
}

.btn-secondary:hover {
  background: rgba(6, 182, 212, 0.1);
}

@media (min-width: 640px) {
  .titulo-principal {
    font-size: 6rem;
  }
  
  .logo-image {
    width: 300px;
    height: 300px;
  }
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.8;
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes glow {
  0%, 100% {
    filter: drop-shadow(0 0 30px rgba(6, 182, 212, 0.6))
            drop-shadow(0 0 60px rgba(168, 85, 247, 0.4));
  }
  50% {
    filter: drop-shadow(0 0 40px rgba(6, 182, 212, 0.8))
            drop-shadow(0 0 80px rgba(168, 85, 247, 0.6))
            drop-shadow(0 0 100px rgba(236, 72, 153, 0.3));
  }
}
</style>