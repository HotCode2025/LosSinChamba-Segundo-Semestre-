<script setup>
import AutopsyDigitalForensics from '/public/Leanjua/Autopsy Digital Forensics.png'
import AWS from '/public/Leanjua/aws.png'
import Cisco from '/public/Leanjua/cisco.png'
import CSharp from '/public/Leanjua/csharp.png'
import CSS from '/public/Leanjua/css.png'
import Docker from '/public/Leanjua/docker.png'
import Express from '/public/Leanjua/express.png'
import Flutter from '/public/Leanjua/flutter.png'
import GraphQL from '/public/Leanjua/graphql.png'
import HTML from '/public/Leanjua/html.png'
import Java from '/public/Leanjua/java.png'
import JavaScript from '/public/Leanjua/Js.png' 
import KaliLinux from '/public/Leanjua/Kali, Linux.png'
import TypeScript from '/public/Leanjua/mecanografiado.png' 
import MongoDB from '/public/Leanjua/mongodb.png'
import MySQL from '/public/Leanjua/mysql.png'
import NodeJS from '/public/Leanjua/nodejs.png'
import OrangeWhile from '/public/Leanjua/orangewhile.png'
import Python from '/public/Leanjua/piton.png'
import PostgreSQL from '/public/Leanjua/postgresql.png'
import React from '/public/Leanjua/react_.png'
import RedHat from '/public/Leanjua/redhat_.png'
import TailwindCSS from '/public/Leanjua/tailwindcss.png'
import VisualStudio from '/public/Leanjua/visual-basico.png'
import VueJS from '/public/Leanjua/vuejs.png'


import { ref } from 'vue'

const skills = ref([
  { name: 'Autopsy Digital Forensics', img: AutopsyDigitalForensics },
  { name: 'AWS', img: AWS },
  { name: 'Cisco', img: Cisco },
  { name: 'C#', img: CSharp },
  { name: 'CSS', img: CSS },
  { name: 'Docker', img: Docker },
  { name: 'Express', img: Express },
  { name: 'Flutter', img: Flutter },
  { name: 'GraphQL', img: GraphQL },
  { name: 'HTML', img: HTML },
  { name: 'Java', img: Java },
  { name: 'JavaScript', img: JavaScript },
  { name: 'Kali Linux', img: KaliLinux },
  { name: 'TypeScript', img: TypeScript },
  { name: 'MongoDB', img: MongoDB },
  { name: 'MySQL', img: MySQL },
  { name: 'Node.js', img: NodeJS },
  { name: 'OrangeWhile', img: OrangeWhile },
  { name: 'Python', img: Python },
  { name: 'PostgreSQL', img: PostgreSQL },
  { name: 'React', img: React },
  { name: 'Red Hat', img: RedHat },
  { name: 'Tailwind CSS', img: TailwindCSS },
  { name: 'Visual Studio', img: VisualStudio },
  { name: 'Vue.js', img: VueJS }
])
</script>

<template>
  <div class="habilidades-section">
    <div class="habilidades-container">
      <h2 class="section-title">Tecnologías</h2>
      <div class="skills-container">
        <div
          v-for="(skill, index) in skills"
          :key="index"
          class="skill-card"
        >
          <img 
            :src="skill.img" 
            :alt="skill.name"
            class="skill-icon"
          />
          <span class="skill-name">{{ skill.name }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.habilidades-section {
  min-height: 100vh;
  padding: 5rem 1rem;
}

.habilidades-container {
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

.skills-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 2rem;
  justify-items: center;
}

.skill-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 1.5rem;
  background: rgba(15, 23, 42, 0.5);
  backdrop-filter: blur(20px);
  border-radius: 1rem;
  border: 1px solid #1e293b;
  transition: all 0.3s;
  cursor: pointer;
  width: 140px;
  height: 140px;
}

.skill-card:hover {
  transform: translateY(-8px) scale(1.05);
  border-color: rgba(6, 182, 212, 0.5);
  box-shadow: 0 8px 32px rgba(6, 182, 212, 0.2);
}

.skill-icon {
  width: 60px;
  height: 60px;
  object-fit: contain;
  transition: transform 0.3s;
}

.skill-card:hover .skill-icon {
  transform: scale(1.1);
}

.skill-name {
  font-size: 0.75rem;
  color: #cbd5e1;
  text-align: center;
  font-weight: 500;
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }
  
  .skills-container {
    grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
    gap: 1.5rem;
  }
  
  .skill-card {
    width: 110px;
    height: 110px;
    padding: 1rem;
  }
  
  .skill-icon {
    width: 50px;
    height: 50px;
  }
  
  .skill-name {
    font-size: 0.65rem;
  }
}
</style>