<script setup>
const descripcion = `
Educador Especializado en Tecnología y Ciberdefensa con dos años de experiencia impartiendo formación esencial para adolescentes y adultos.
Actualmente, me desempeño como docente en la Escuela Industrial N°3 "Oscar Smith" de Puerto Deseado y en la Universidad ISALUD de Caleta Olivia. 
Esta doble función me permite diseñar y ejecutar programas educativos que combinan una sólida base técnica (Escuela Industrial) con una perspectiva profesional y avanzada (Universidad).
Mi principal contribución es el desarrollo de habilidades cruciales en alfabetización tecnológica avanzada y prácticas de ciberseguridad, 
asegurando que tanto jóvenes como adultos estén capacitados para enfrentar los desafíos y las amenazas del entorno digital actual.
`;
</script>

<template>
  <section class="perfil-section aparecer-inicio" id="perfil">
    <div class="perfil-container">
      <div class="perfil-text">
        <h2 class="perfil-title text-glow">
          <span class="glitch-text">DOCENTE & CIBERDEFENSA</span>
        </h2>
        <p class="perfil-description">{{ descripcion }}</p>
      </div>

      <!-- Zona para cargar nuevos trabajos -->
      <div class="perfil-upload">
        <div class="upload-box">
          <img src="/upload-icon.png" alt="Subir" class="upload-icon" />
          <p class="upload-text">Cargar nuevo trabajo o proyecto</p>
          <button class="upload-btn">+ Añadir</button>
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
  --glow-light: rgba(76, 135, 228, 0.15);
}

/* 🔹 Sección principal */
.perfil-section {
  min-height: 100vh;
  width: 100vw;
  background: var(--bg-color);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 100px 20px;
  background: radial-gradient(circle at 10% 10%, rgba(76, 135, 228, 0.1), transparent 60%),
              radial-gradient(circle at 90% 90%, rgba(248, 81, 73, 0.05), transparent 70%);
}

.perfil-container {
  width: 90%;
  max-width: 1100px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 50px;
  text-align: center;
}

/* 🔹 Texto descriptivo */
.perfil-text {
  max-width: 800px;
}

.perfil-title {
  color: var(--primary-color);
  font-size: 2.4rem;
  text-shadow: 0 0 10px var(--shadow-color);
  margin-bottom: 20px;
}

.perfil-description {
  color: var(--text-color);
  font-size: 1.05rem;
  line-height: 1.8;
  background: var(--card-bg);
  padding: 25px 35px;
  border-radius: 15px;
  box-shadow: 0 0 20px var(--glow-light);
  border: 1px solid rgba(76, 135, 228, 0.15);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.perfil-description:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 30px var(--shadow-color);
}

/* 🔹 Zona de carga */
.perfil-upload {
  width: 100%;
  display: flex;
  justify-content: center;
}

.upload-box {
  background: var(--card-bg);
  border: 2px dashed rgba(76, 135, 228, 0.3);
  border-radius: 15px;
  padding: 50px 40px;
  width: 80%;
  max-width: 600px;
  text-align: center;
  transition: border-color 0.3s ease, transform 0.3s ease;
}
.upload-box:hover {
  border-color: var(--primary-color);
  transform: scale(1.02);
  box-shadow: 0 0 20px var(--glow-light);
}

.upload-icon {
  width: 70px;
  opacity: 0.8;
  margin-bottom: 15px;
}

.upload-text {
  color: var(--secondary-text);
  margin-bottom: 10px;
  font-size: 1rem;
}

.upload-btn {
  background: var(--primary-color);
  color: var(--bg-color);
  border: none;
  padding: 10px 25px;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;
}
.upload-btn:hover {
  background: #5d99f4;
  box-shadow: 0 0 15px var(--shadow-color);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .perfil-description {
    font-size: 0.95rem;
    padding: 20px;
  }
  .upload-box {
    width: 100%;
    padding: 40px 20px;
  }
}
</style>
