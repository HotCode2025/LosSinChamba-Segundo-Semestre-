<script setup>
// Datos del perfil
const title = 'Leandro A. Orozco';
const description = 'Técnico Universitario en Programación y Ciberdefensa';
const Presentacion = 'Soy Leandro Orozco, Técnico Universitario en Programación y Ciberdefensa, apasionado por la tecnología y la ciberseguridad. Con experiencia en desarrollo de software y enseñanza, busco contribuir con soluciones innovadoras y compartir conocimientos en el campo de la programación y la seguridad informática.';
const Ubicación = 'Puerto Deseado, Santa Cruz';
const Celular = '(+54) 2974664689';
const Email = 'orozcolean@gmail.com';
const redes = [
  { nombre: 'GitHub', enlace: 'https://github.com/Lean-O', icono: '/github.png' },
  { nombre: 'LinkedIn', enlace: 'https://www.linkedin.com/in/leandro-orozco-123456789/', icono: '/linkedin.png' },
  { nombre: 'Instagram', enlace: 'https://www.instagram.com/lean.o_geek/', icono: '/instagram.png' }
];
</script>

<template>
  <section class="sobre-mi aparecer-inicio" id="acerca-de-mi">
    <div class="contenedor-perfil">
      <div class="perfil-card">
        <h1 class="text-glow">{{ title }}</h1>
        <h2 class="text-shadow">{{ description }}</h2>
        
        <div class="presentacion">
          <h3 class="data-title presentacion-title">Presentación</h3>
          <p class="presentacion-text">
            {{ Presentacion }}
          </p>
        </div>
        
        <div class="info-grid">
          <div class="datos-personales-container">
            <h3 class="data-title datos-title">Datos Personales</h3>
            <ul class="datos-lista">
              <li class="data-item">
                <img src="/ubicacion.png" alt="Icono de Ubicación" class="icon-image" />
                <strong></strong> {{ Ubicación }}
              </li>
              <li class="data-item">
                <img src="/whatsapp.png" alt="Icono de WhatsApp" class="icon-image" />
                <strong></strong> {{ Celular }}
              </li>
              <li class="data-item">
                <img src="/enviar-correo.png" alt="Icono de Correo" class="icon-image" />
                <a :href="`mailto:${Email}`" class="email-link">{{ Email }}</a>
              </li>
            </ul>
          </div>
          <div class="redes-container">
            <h3 class="data-title redes-title">Redes Sociales</h3>
            <ul class="redes-lista">
              <li v-for="(red, index) in redes" :key="index" class="red-item">
                <a :href="red.enlace" target="_blank" rel="noopener" class="red-link">
                  <img :src="red.icono" :alt="red.nombre" class="icono-red" />
                  {{ red.nombre }}
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* === VARIABLES DE COLOR Y FUENTE (del componente principal) === */
/* Usamos #0a0f17 y #06b6d4 del componente principal para consistencia */
:root {
  --bg-color: #0a0f17; 
  --text-color: #e2e8f0; 
  --primary-color: #06b6d4; /* Color turquesa/cyan */
  --secondary-text-color: #94a3b8;
  --card-bg: #161b22;
  --border-color: rgba(90, 90, 255, 0.15); /* Usado en el navbar original */
  --shadow-color: rgba(6, 182, 212, 0.3);
}

/* ======== ESTILOS GENERALES Y LAYOUT ======== */
.sobre-mi {
  min-height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 120px 0;
  /* El fondo de gradiente del componente principal */
  background: radial-gradient(circle at top left, rgba(96,165,250,0.08), transparent 60%),
              radial-gradient(circle at bottom right, rgba(225,29,72,0.1), transparent 60%);
}

.contenedor-perfil {
  width: 90%;
  max-width: 1200px;
  padding: 40px 0;
}

/* ======== EFECTO DE APARICIÓN (FADE IN Y LIGERO MOVIMIENTO) ======== */
.aparecer-inicio {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInMove 1.5s ease-out forwards;
}

@keyframes fadeInMove {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


/* ======== TARJETA PERFIL (Componente central) ======== */
.perfil-card {
  background-color: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 60px 80px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  transition: transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94),
              box-shadow 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  text-align: center;
}

.perfil-card:hover {
  /* Efecto de elevación/inclinación sutil al pasar el ratón */
  transform: perspective(1000px) rotateX(1deg) translateY(-5px);
  box-shadow: 0 15px 45px var(--shadow-color);
}


/* ======== TITULOS Y CORRECCIÓN DE ESPACIADO ======== */
h1 {
  font-family: 'Orbitron', sans-serif; /* Consistencia con el NavBar */
  color: var(--primary-color);
  font-weight: 700;
  font-size: 3.2rem;
  margin-bottom: 5px;
}

/* Efecto de resplandor para el nombre */
.text-glow {
  text-shadow: 0 0 15px var(--shadow-color), 0 0 5px rgba(255, 255, 255, 0.1);
}

h2 {
  color: var(--secondary-text-color);
  font-size: 1.4rem;
  margin-bottom: 40px;
  font-weight: 400;
}

/* Efecto de sombra sutil para la descripción */
.text-shadow {
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
}

.data-title {
  color: var(--primary-color);
  font-weight: 600;
  border-bottom: 2px solid var(--border-color);
  padding-bottom: 8px;
  font-size: 1.5rem;
  display: inline-block;
}

/* 1. ACERCA TÍTULO PRESENTACIÓN AL TEXTO */
.presentacion-title {
  margin-bottom: 10px; 
}

/* 2. SEPARA TÍTULO DATOS PERSONALES DE LA LISTA */
.datos-title {
  margin-bottom: 15px; 
}

/* 3. SEPARA TÍTULO REDES SOCIALES DE LA LISTA */
.redes-title {
  margin-bottom: 15px;
}


/* ======== DATOS PERSONALES Y REDES LAYOUT ======== */
.info-grid {
  display: flex;
  justify-content: space-around;
  gap: 40px;
  margin-bottom: 50px;
}

.datos-personales-container, .redes-container {
  flex: 1;
  min-width: 300px;
  text-align: left; 
  padding: 0 20px;
}

.datos-lista {
  list-style: none;
  padding: 0;
  /* Aseguramos que no haya un margen superior extra */
  margin: 0; 
}

.data-item {
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 0;
  color: var(--secondary-text-color);
  border-bottom: 1px dashed rgba(255, 255, 255, 0.05);
  transition: padding-left 0.3s ease, color 0.3s ease;
}

.data-item:hover {
  padding-left: 10px;
  color: var(--text-color);
}

.data-item strong {
  color: var(--text-color);
  font-weight: 600;
}

/* ESTILOS DE FONT AWESOME (MANTENIDOS) */
.icon-color {
  color: var(--primary-color);
  width: 20px;
  text-align: center;
  font-size: 1.1rem;
}

/* NUEVO ESTILO PARA LAS IMÁGENES DE UBICACIÓN Y WHATSAPP */
.icon-image {
  width: 20px; /* Ancho similar a los iconos de Font Awesome */
  height: 20px;
  object-fit: contain;
  /* Replicamos el estilo de .icon-color para mantener la alineación/espacio */
  width: 20px; 
  text-align: center;
}

.email-link {
  color: var(--primary-color);
  text-decoration: none;
  transition: color 0.3s ease;
}
.email-link:hover {
  color: #33FFC9; 
  text-decoration: underline;
}

/* ======== REDES SOCIALES (NO MODIFICADAS) ======== */
.redes-lista {
  list-style: none;
  /* Aseguramos que no haya un margen superior extra */
  margin: 0; 
  padding: 0;
  display: flex;
  justify-content: center; 
  gap: 30px; 
  flex-wrap: wrap;
  padding-top: 10px; /* Separación visual clara del título */
}

.red-item {
  transition: transform 0.3s ease;
}

.red-item:hover {
  transform: translateY(-5px); 
}

.red-link {
  color: var(--primary-color);
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 500;
  transition: color 0.3s ease;
  text-decoration: none;
}

.red-link:hover {
  color: var(--text-color);
}

.icono-red {
  width: 38px;
  height: 38px;
  object-fit: contain;
  border-radius: 6px;
  transition: filter 0.3s ease;
}

.red-link:hover .icono-red {
  filter: drop-shadow(0 0 5px var(--primary-color));
}

/* ======== PRESENTACIÓN ======== */
.presentacion {
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid var(--border-color);
  margin-bottom: 40px; /* Separación clara de la siguiente sección */
}

.presentacion-text {
  color: var(--secondary-text-color);
  font-size: 1.1rem;
  line-height: 1.8;
  text-align: center;
  max-width: 900px;
  /* Ajuste de margen para acercar el texto al título */
  margin: 15px auto 0 auto; 
}

/* ======== RESPONSIVE ======== */
@media (max-width: 992px) {
  .info-grid {
     flex-direction: column;
     gap: 30px;
    }

    .datos-personales-container, .redes-container {
      text-align: center;
      padding: 0;
    }

    .datos-lista {
      align-items: center;
    }

    .data-item {
      justify-content: center;
    }

    .perfil-card {
      padding: 40px 30px;
    }
}

@media (max-width: 576px) {
  h1 {
    font-size: 2.5rem;
  }

  h2 {
    font-size: 1.2rem;
  }
  .redes-lista {
    gap: 20px;
  }

  .data-title {
    font-size: 1.3rem;
  }
}
</style>