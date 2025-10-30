<script setup>
const proyectos = [
  {
    titulo: 'CryptoStart: Fundamentos de Criptografía',
    tecnologiaPrincipal: 'Python',
    descripcion: 'Inicio del aprendizaje en ciberseguridad con cifrado César, XOR y claves simétricas. Primer acercamiento al pensamiento en seguridad y anonimato digital.',
    stack: ['Python', 'Cifrado Básico', 'Hashing'],
    fecha: '2023',
  },
  {
    titulo: 'ForensicLab: Explorando Autopsy',
    tecnologiaPrincipal: 'Autopsy & FTK Imager',
    descripcion: 'Análisis forense básico en imágenes de disco. Recuperación de archivos y trazado de actividad digital simulada en un entorno controlado.',
    stack: ['Autopsy', 'FTK Imager', 'Análisis de Disco'],
    fecha: '2024 (Inicio)',
  },
  {
    titulo: 'NetShield Junior: Defensa de Red Local',
    tecnologiaPrincipal: 'Wireshark & Kali Linux',
    descripcion: 'Simulación de monitoreo de red, detección de patrones sospechosos y pruebas de sniffing controlado en entornos educativos.',
    stack: ['Kali Linux', 'Wireshark', 'TCP/IP'],
    fecha: '2024 (Mitad)',
  },
  {
    titulo: 'CryptoGuard: RSA Educativo',
    tecnologiaPrincipal: 'Python + Matemática',
    descripcion: 'Implementación didáctica del algoritmo RSA. Aprendizaje sobre generación de claves y encriptación de mensajes.',
    stack: ['Python', 'RSA', 'Números Primos'],
    fecha: '2025 (Inicio)',
  },
  {
    titulo: 'CyberDefense Jr: Proyecto Final',
    tecnologiaPrincipal: 'Integración',
    descripcion: 'Creación de un entorno simulado de ataque y defensa digital. Uso combinado de criptografía, análisis forense y monitoreo de red.',
    stack: ['Kali Linux', 'Python', 'Seguridad Integrada'],
    fecha: '2025 (Fin)',
  },
];
</script>

<template>
  <section class="proyectos aparecer-inicio" id="proyectos">
    <div class="contenedor-proyectos">
      <h2 class="section-title text-glow">
        <img src="/ciberseguridad.png" alt="Logo" class="logo-icon-img" /> 
        <span class="glitch-text"> CYBERLINE</span>
      </h2>
      <p class="section-subtitle">
          PROYECTOS CIBERDEFENSA Y FORENSIS DIGITAL 
      </p>
      
      <div class="timeline-container">
        <div 
          v-for="(proyecto, index) in proyectos" 
          :key="index" 
          :class="['timeline-item', index % 2 === 0 ? 'left' : 'right']"
        >
          <div class="timeline-dot">
            <span class="pulse-glow"></span>
          </div>
          
          <div class="timeline-content">
            <span class="timeline-date">{{ proyecto.fecha }}</span>
            <h3 class="proyecto-titulo">{{ proyecto.titulo }}</h3>
            <span class="proyecto-tech-main">{{ proyecto.tecnologiaPrincipal }}</span>
            <p class="proyecto-descripcion">{{ proyecto.descripcion }}</p>
            <div class="proyecto-stack">
              <span v-for="tech in proyecto.stack" :key="tech" class="stack-tag">{{ tech }}</span>
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
  --text-color: #c9d1d9;
  --primary-color: #4c87e4;
  --secondary-text-color: #8b949e;
  --card-bg: #161b22;
  --border-color: rgba(76, 135, 228, 0.2);
  --shadow-color: rgba(76, 135, 228, 0.6);
  --light-glow: rgba(76, 135, 228, 0.1);
}

.proyectos {
  min-height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 120px 0 80px 0;
  background: radial-gradient(circle at top left, rgba(76, 135, 228, 0.1), transparent 60%),
              radial-gradient(circle at bottom right, rgba(248, 81, 73, 0.05), transparent 60%);
}

.contenedor-proyectos {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  color: var(--primary-color);
  font-size: 2.5rem;
  text-shadow: 0 0 15px var(--shadow-color);
}

.logo-icon-img {
  width: 50px;
  height: 50px;
  object-fit: contain;
  filter: drop-shadow(0 0 10px var(--shadow-color));
}

.glitch-text {
  font-family: 'Consolas', monospace;
}

.section-subtitle {
  color: var(--secondary-text-color);
  text-align: center;
  margin-bottom: 60px;
  font-size: 1.1rem;
}

.timeline-container {
  position: relative;
  max-width: 1000px;
  margin: 0 auto;
}

/* ===== NUEVA LÍNEA CENTRAL CON BRILLO Y ANIMACIÓN ===== */
.timeline-container::after {
  content: '';
  position: absolute;
  width: 3px;
  background: linear-gradient(180deg, transparent, var(--primary-color), transparent);
  box-shadow: 0 0 20px var(--primary-color);
  top: 0;
  bottom: 0;
  left: 50%;
  margin-left: -1.5px;
  animation: neonFlow 3s linear infinite;
}

@keyframes neonFlow {
  0% { box-shadow: 0 0 5px var(--primary-color); }
  50% { box-shadow: 0 0 20px var(--primary-color); }
  100% { box-shadow: 0 0 5px var(--primary-color); }
}

.timeline-item {
  padding: 10px 40px;
  position: relative;
  width: 50%;
}
.timeline-item.left { left: 0; }
.timeline-item.right { left: 50%; }

/* DOT GLOW + ANIMACIÓN */
.timeline-dot {
  position: absolute;
  width: 30px;
  height: 30px;
  right: -15px;
  background-color: var(--bg-color);
  border: 2px solid var(--primary-color);
  border-radius: 50%;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 12px var(--shadow-color);
  overflow: hidden;
}
.timeline-item.right .timeline-dot { left: -15px; right: auto; }

.pulse-glow {
  width: 10px;
  height: 10px;
  background: var(--primary-color);
  border-radius: 50%;
  box-shadow: 0 0 15px var(--primary-color);
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.8); opacity: 0.5; }
  100% { transform: scale(1); opacity: 1; }
}

.timeline-content {
  padding: 20px 25px;
  background-color: var(--card-bg);
  border-radius: 8px;
  border: 1px solid var(--border-color);
  border-left: 5px solid var(--primary-color);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s, box-shadow 0.3s;
}
.timeline-content:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 25px var(--shadow-color);
}

.timeline-date {
  color: var(--primary-color);
  font-weight: bold;
}
.proyecto-titulo {
  color: var(--text-color);
  font-size: 1.3rem;
}
.proyecto-tech-main {
  background: var(--primary-color);
  color: var(--bg-color);
  padding: 2px 8px;
  border-radius: 2px;
  font-size: 0.8rem;
  font-weight: 700;
}
.proyecto-descripcion {
  color: var(--secondary-text-color);
  margin: 10px 0;
}

.stack-tag {
  background-color: var(--light-glow);
  color: var(--primary-color);
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
  transition: all 0.3s;
}
.stack-tag:hover {
  background-color: var(--primary-color);
  color: var(--bg-color);
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
  .timeline-container::after { left: 20px; }
  .timeline-item { width: 100%; padding-left: 50px; padding-right: 15px; }
  .timeline-item.right { left: 0; }
  .timeline-dot { left: 4px; right: auto; }
  .timeline-content { border-left: 5px solid var(--primary-color); }
}
</style>
