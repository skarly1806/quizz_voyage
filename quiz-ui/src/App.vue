<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-white header">
    <div class="navbar">
      <div class="nav" style="top:3px;right:-10px;">
        <RouterLink to="/">Accueil</RouterLink>
      </div>

      <ul>
        <audio controls loop autoplay style="left:500px;top:15px;height:24px;">
          <source src="/src/assets/Daft Punk - Around The World.mp3">
        </audio>
      </ul>

      <ul>
        <div class="nav" style="top:10px;left:950px;">
          <RouterLink to="/AdminPage">Admin</RouterLink>
        </div>
      </ul>

    </div>
  </nav>
  <RouterView />
</template> 

<style scoped>
nav {
  padding-top: 0px;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 9999;
  margin-bottom: 20px;
  height: 35px;
  font-family: 'Poppins', sans-serif;
}
</style>
