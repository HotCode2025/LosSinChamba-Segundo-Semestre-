<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'
import Inicio from './components/Inicio.vue'
import Equipo from './components/Equipo.vue'
import Habilidades from './components/Habilidades.vue'
import Contacto from './components/Contacto.vue'
import FondoAnimado from './components/FondoAnimado.vue'

const activeSection = ref('inicio')
</script>

<template>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
  >

  <div class="app-container">
    <FondoAnimado />
    
    <header>
      <NavBar :activeSection="activeSection" @update:activeSection="activeSection = $event" />
    </header>

    <main class="main-content">
      <section id="inicio">
        <Inicio />
      </section>

      <section id="equipo">
        <Equipo />
      </section>

      <section id="habilidades">
        <Habilidades />
      </section>

      <section id="contacto">
        <Contacto />
      </section>
    </main>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@400;600&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
  overflow-x: hidden;
  background: #020617;
  color: #f1f5f9;
}

html {
  scroll-behavior: smooth;
}

.app-container {
  min-height: 100vh;
  position: relative;
  overflow: hidden;
}

.main-content {
  position: relative;
  z-index: 10;
  padding-top: 4rem;
}
</style>