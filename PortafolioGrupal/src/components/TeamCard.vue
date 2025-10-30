<script setup>
defineProps({
  member: Object,
  index: Number
})

const getInitials = (name) => {
  return name.split(' ').map(n => n[0]).join('')
}

const hasCustomImage = (name) => {
  const nameLower = name.toLowerCase()
  return (nameLower.includes('leandro') && nameLower.includes('orozco')) || 
         nameLower.includes('lautaro') ||
         nameLower.includes('mariano') ||
         nameLower.includes('kevin') ||
         nameLower.includes('gabriel') ||
         nameLower.includes('gabi') ||
         nameLower.includes('ezequiel') ||
         nameLower.includes('eze')
}

const getProfileImage = (name) => {
  const nameLower = name.toLowerCase()
  
  if (nameLower.includes('leandro') && nameLower.includes('orozco')) {
    return '/perfilLean.png'
  }
  if (nameLower.includes('lautaro')) {
    return '/perfilLauti.jpg'
  }
  if (nameLower.includes('mariano')) {
    return '/perfilMariano.jpg'
  }
  if (nameLower.includes('kevin')) {
    return '/perfilKevin.jpg'
  }
  if (nameLower.includes('gabriel') || nameLower.includes('gabi')) {
    return '/perfilGabi.jpg'
  }
  if (nameLower.includes('ezequiel') || nameLower.includes('eze')) {
    return '/perfilEze.jpg'
  }
  
  return null
}

const getCustomRole = (name) => {
  const nameLower = name.toLowerCase()
  if (nameLower.includes('leandro') && nameLower.includes('orozco')) {
    return 'Docente y Ciberdefenza'
  }
  if (nameLower.includes('lautaro')) {
    return 'Desarrollador de Inteligencia Artificial'
  }
  // Gabriel ya no tiene rol custom, se eliminó "Backend Engineer"
  return null
}

const getLinks = (name) => {
  const nameLower = name.toLowerCase()
  
  // Leandro Orozco
  if (nameLower.includes('leandro') && nameLower.includes('orozco')) {
    return {
      github: 'https://github.com/Lean-O',
      website: 'https://leandro-orozco.netlify.app/'
    }
  }
  
  // Lautaro Martinez
  if (nameLower.includes('lautaro')) {
    return {
      github: 'https://github.com/Lautaro50',
      website: 'https://lautaromartinez.netlify.app/#'
    }
  }
  
  // Gabriel (Gabi)
  if (nameLower.includes('gabriel') || nameLower.includes('gabi')) {
    return {
      github: 'https://github.com/hgmaculus',
      website: null
    }
  }
  
  // Ezequiel (Eze)
  if (nameLower.includes('ezequiel') || nameLower.includes('eze')) {
    return {
      github: 'https://github.com/ezediaz08',
      website: 'https://ezequeildiaz-vuejs.netlify.app'
    }
  }
  
  // Mariano
  if (nameLower.includes('mariano')) {
    return {
      github: 'https://github.com/mariannorasg',
      website: 'https://mariannorasgido.netlify.app/'
    }
  }
  
  // Kevin
  if (nameLower.includes('kevin')) {
    return {
      github: 'https://github.com/kevincastilla4050',
      website: 'https://portafoliokevincastilla.netlify.app/'
    }
  }
  
  return {
    github: null,
    website: null
  }
}

const nameLower = (name) => name.toLowerCase()
</script>

<template>
  <div class="team-card">
    <div class="card-glow" :style="{ background: `${member.color}20` }" />
    <div class="card-content">
      <div class="avatar" :style="{ background: `${member.color}30`, color: member.color }">
        <img 
          v-if="hasCustomImage(member.name)" 
          :src="getProfileImage(member.name)" 
          :alt="member.name"
          class="avatar-image"
        />
        <span v-else>{{ getInitials(member.name) }}</span>
      </div>
      <h3 class="member-name" :style="{ color: member.color }">
        {{ member.name }}
      </h3>
      <p v-if="nameLower(member.name).includes('gabriel') || nameLower(member.name).includes('gabi')" class="member-tech">
        Java, C, C++, Pascal, SQL
      </p>
      <p v-if="getCustomRole(member.name)" class="member-role">{{ getCustomRole(member.name) }}</p>
      <p v-else-if="!(nameLower(member.name).includes('gabriel') || nameLower(member.name).includes('gabi'))" class="member-role">{{ member.role }}</p>
      
      <div class="links-container">
        <a 
          v-if="getLinks(member.name).website" 
          :href="getLinks(member.name).website"
          target="_blank"
          rel="noopener noreferrer"
          class="social-link"
          title="Sitio Web"
        >
          <img src="/web.png" alt="Sitio Web" class="social-icon" />
        </a>
        
        <a 
          v-if="getLinks(member.name).github" 
          :href="getLinks(member.name).github"
          target="_blank"
          rel="noopener noreferrer"
          class="social-link"
          title="GitHub"
        >
          <img src="/Git.png" alt="GitHub" class="social-icon" />
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.team-card {
  position: relative;
  background: rgba(15, 23, 42, 0.5);
  backdrop-filter: blur(20px);
  border-radius: 1rem;
  padding: 2rem;
  border: 1px solid #1e293b;
  transition: all 0.3s;
}

.team-card:hover {
  transform: scale(1.05);
  border-color: rgba(6, 182, 212, 0.5);
}

.card-glow {
  position: absolute;
  inset: 0;
  border-radius: 1rem;
  opacity: 0;
  transition: opacity 0.3s;
  filter: blur(40px);
}

.team-card:hover .card-glow {
  opacity: 1;
}

.card-content {
  position: relative;
  z-index: 1;
}

.avatar {
  width: 5rem;
  height: 5rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 1rem;
  overflow: hidden;
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

.member-name {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.member-tech {
  color: #94a3b8;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  letter-spacing: 0.05em;
}

.member-role {
  color: #94a3b8;
  margin-bottom: 1rem;
}

.links-container {
  display: flex;
  gap: 0.75rem;
  margin-top: 1rem;
  justify-content: flex-start;
}

.social-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem;
  border-radius: 0.5rem;
  background: rgba(255, 255, 255, 0.05);
  transition: all 0.3s;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.social-link:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(6, 182, 212, 0.3);
}

.social-icon {
  width: 2rem;
  height: 2rem;
  filter: brightness(0) invert(1);
  transition: filter 0.3s;
}

.social-link:hover .social-icon {
  filter: brightness(0) invert(1) drop-shadow(0 0 8px rgba(6, 182, 212, 0.8));
}
</style>