<script setup>
import { ref } from 'vue';

const proyectos = [
  {
    titulo: 'TaskCore v1.0: Gestor de Microservicios',
    tecnologiaPrincipal: 'JavaScript & CSS',
    descripcion:
      'Aplicación full-stack para la gestión de tareas (CRUD) con frontend en JavaScript vanilla y backend simulado con JSON Server.',
    stack: ['JavaScript', 'HTML5', 'CSS3', 'JSON Server'],
    fecha: 'Junio 2025',
    imagen: '/TaskCorev1.0.png',
    enlace: 'https://github.com/Lean-O/PROYECPORTA2/tree/main/TaskCorev1.0',
  },
  {
    titulo: 'CryptoGuard: Simulador RSA',
    tecnologiaPrincipal: 'Python',
    descripcion:
      'Script en Python para demostrar conceptos de ciberseguridad mediante el cifrado RSA, con enfoque educativo.',
    stack: ['Python', 'Matemáticas', 'Criptografía Básica'],
    fecha: 'Enero 2025',
    imagen: '/CryptoGuard.png',
    enlace: 'https://github.com/Lean-O/PROYECPORTA2/tree/main/CryptoGuard',
  },
  {
    titulo: 'Nexus UI/UX Portfolio (Vue.js)',
    tecnologiaPrincipal: 'Vue.js/Framework',
    descripcion:
      'Portafolio personal interactivo con Vue.js, diseño responsivo y componentes reutilizables.',
    stack: ['Vue.js', 'Vite', 'CSS Scoped', 'RespDesign'],
    fecha: 'Noviembre 2024',
    imagen: '/Coding.jpeg', // 🔹 Imagen actualizada desde /public
    enlace: null,
  },
  {
    titulo: 'StockTracker Console (Java I/O)',
    tecnologiaPrincipal: 'Java',
    descripcion:
      'Aplicación de consola en Java para la gestión de inventario utilizando colecciones y archivos de texto (I/O).',
    stack: ['Java (SE)', 'POO', 'Archivos TXT'],
    fecha: 'Septiembre 2024',
    imagen: '/Coding.jpeg', // 🔹 Imagen actualizada desde /public
    enlace: null,
  },
];

const carouselRef = ref(null);

function scrollCarousel(direction) {
  const container = carouselRef.value;
  if (container) {
    const scrollAmount = 350;
    container.scrollBy({
      left: direction === 'left' ? -scrollAmount : scrollAmount,
      behavior: 'smooth',
    });
  }
}
</script>

<template>
  <section class="proyectos aparecer-inicio" id="proyectos">
    <div class="contenedor-proyectos">
      <h2 class="section-title text-glow">
        <img src="/jugador.png" alt="Logo" class="logo-icon-img" />
        <span class="glitch-text">PROJECT-LOG</span>
      </h2>
      <p class="section-subtitle">**TRAZANDO LA RUTA**: Proyectos clave en mi desarrollo</p>

      <!-- 🔹 Flechas de navegación -->
      <button class="arrow left" @click="scrollCarousel('left')">❮</button>
      <button class="arrow right" @click="scrollCarousel('right')">❯</button>

      <!-- 🔹 Carrusel -->
      <div class="carousel" ref="carouselRef">
        <div
          v-for="(proyecto, index) in proyectos"
          :key="index"
          class="carousel-item"
        >
          <div class="proyecto-card">
            <img
              :src="proyecto.imagen"
              :alt="proyecto.titulo"
              class="proyecto-img"
            />
            <div class="proyecto-info">
              <h3>{{ proyecto.titulo }}</h3>
              <span class="proyecto-tech">{{ proyecto.tecnologiaPrincipal }}</span>
              <p>{{ proyecto.descripcion }}</p>
              <div class="proyecto-stack">
                <span
                  v-for="tech in proyecto.stack"
                  :key="tech"
                  class="stack-tag"
                  >{{ tech }}</span
                >
              </div>

              <!-- 🔹 GitHub o En proceso -->
              <div class="github-link" v-if="proyecto.enlace">
                <a :href="proyecto.enlace" target="_blank">
                  <img src="/github.png" alt="GitHub" class="github-icon" />
                </a>
              </div>
              <div class="github-link" v-else>
                <span class="en-proceso">En proceso 🚧</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
:root {
  --bg-color: #0d1117;
  --card-bg: #161b22;
  --text-color: #c9d1d9;
  --primary-color: #4c87e4;
  --secondary-text: #8b949e;
  --shadow-color: rgba(76, 135, 228, 0.6);
  --glow-light: rgba(76, 135, 228, 0.1);
}

.proyectos {
  min-height: 100vh;
  width: 100vw;
  background: var(--bg-color);
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 120px 0;
  background: radial-gradient(circle at top left, rgba(76, 135, 228, 0.15), transparent 70%),
              radial-gradient(circle at bottom right, rgba(248, 81, 73, 0.05), transparent 70%);
}

.contenedor-proyectos {
  width: 90%;
  max-width: 1100px;
  text-align: center;
  position: relative;
}

.section-title {
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--primary-color);
  font-size: 2.4rem;
  text-shadow: 0 0 10px var(--shadow-color);
  gap: 10px;
}

.logo-icon-img {
  width: 45px;
  height: 45px;
}

.section-subtitle {
  color: var(--secondary-text);
  margin-bottom: 40px;
}

.carousel {
  display: flex;
  overflow-x: auto;
  scroll-behavior: smooth;
  gap: 25px;
  padding: 20px;
  scrollbar-width: none;
}
.carousel::-webkit-scrollbar {
  display: none;
}
.carousel-item {
  flex: 0 0 270px;
  perspective: 1000px;
  transition: transform 0.5s;
}
.carousel-item:hover {
  transform: scale(1.05) rotateY(3deg);
}

.proyecto-card {
  background-color: var(--card-bg);
  border-radius: 12px;
  border: 1px solid rgba(76, 135, 228, 0.2);
  box-shadow: 0 0 15px var(--glow-light);
  overflow: hidden;
  transition: all 0.3s ease-in-out;
}
.proyecto-card:hover {
  box-shadow: 0 0 25px var(--shadow-color);
}

.proyecto-img {
  width: 100%;
  height: 150px;
  object-fit: contain;
  background: #0a0f14;
  padding: 10px;
  border-bottom: 1px solid rgba(76, 135, 228, 0.2);
}

.proyecto-info {
  padding: 15px;
  color: var(--text-color);
}
.proyecto-info h3 {
  font-size: 1.1rem;
  margin-bottom: 5px;
}
.proyecto-tech {
  background: var(--primary-color);
  color: var(--bg-color);
  padding: 3px 7px;
  border-radius: 5px;
  font-size: 0.8rem;
}
.proyecto-info p {
  font-size: 0.9rem;
  color: var(--secondary-text);
  margin: 10px 0;
}

.proyecto-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-top: 5px;
  justify-content: center;
}
.stack-tag {
  background: var(--glow-light);
  color: var(--primary-color);
  font-size: 0.8rem;
  padding: 4px 8px;
  border-radius: 4px;
  transition: 0.3s;
}
.stack-tag:hover {
  background: var(--primary-color);
  color: var(--bg-color);
}

.github-link {
  margin-top: 10px;
}
.github-icon {
  width: 28px;
  height: 28px;
  transition: transform 0.3s ease, filter 0.3s ease;
  filter: drop-shadow(0 0 5px var(--shadow-color));
}
.github-icon:hover {
  transform: scale(1.2);
  filter: drop-shadow(0 0 10px var(--primary-color));
}
.en-proceso {
  color: var(--secondary-text);
  font-size: 0.9rem;
  font-style: italic;
}

.arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(76, 135, 228, 0.15);
  border: 1px solid rgba(76, 135, 228, 0.4);
  color: var(--primary-color);
  font-size: 1.8rem;
  border-radius: 50%;
  cursor: pointer;
  width: 45px;
  height: 45px;
  transition: all 0.3s ease;
  z-index: 5;
}
.arrow:hover {
  background: var(--primary-color);
  color: var(--bg-color);
  box-shadow: 0 0 15px var(--shadow-color);
}
.arrow.left {
  left: -20px;
}
.arrow.right {
  right: -20px;
}

@media (max-width: 768px) {
  .carousel-item {
    flex: 0 0 250px;
  }
  .arrow.left {
    left: 10px;
  }
  .arrow.right {
    right: 10px;
  }
}
</style>
