<template>
  <div class="contacto-section">
    <div class="contacto-container">
      <h2 class="section-title">Contacto</h2>
      <div class="contacto-card">
        <p class="contacto-text">
          ¿Tienes un proyecto en mente? Nos encantaría trabajar contigo.
        </p>
        <div class="contacto-links">
          <a href="https://github.com/HotCode2025/LosSinChamba-Segundo-Semestre-" target="_blank" rel="noopener noreferrer" class="contact-link github-link">
            <i class="fab fa-github"></i>
            <span>GitHub</span>
          </a>
        </div>
      </div>
      <p class="footer-text">
        © 2025 LosSinChamba. Todos los derechos reservados.
      </p>
    </div>
  </div>
</template>

<style scoped>
.contacto-section {
  min-height: 100vh;
  padding: 5rem 1rem;
  display: flex;
  align-items: center;
}

.contacto-container {
  max-width: 64rem;
  margin: 0 auto;
  width: 100%;
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

.contacto-card {
  background: rgba(15, 23, 42, 0.5);
  backdrop-filter: blur(20px);
  border-radius: 1rem;
  padding: 2rem;
  border: 1px solid #1e293b;
}

.contacto-text {
  text-align: center;
  color: #cbd5e1;
  font-size: 1.125rem;
  margin-bottom: 2rem;
}

.contacto-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 9999px;
  text-decoration: none;
  transition: all 0.3s;
  font-weight: 600;
}

.github-link {
  background: rgba(168, 85, 247, 0.2);
  border: 1px solid rgba(168, 85, 247, 0.5);
  color: #a855f7;
}

.github-link:hover {
  background: rgba(168, 85, 247, 0.3);
}

.footer-text {
  text-align: center;
  color: #64748b;
  margin-top: 3rem;
}
</style>