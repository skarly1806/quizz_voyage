<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <!-- <nav class="navbar navbar-expand-lg navbar-light bg-light header">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown"
      aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <div class="nav-link">
            <RouterLink to="/">Home</RouterLink>
          </div>
        </li>
      </ul>
      <ul class="collapse navbar-collapse justify-content-end">
        <li class="nav-item">
          <div class="nav-link" v-if="logged == false" :key="logged">
            <RouterLink to="/Login">Login</RouterLink>
          </div>
          <div class="nav-link" v-else>
            <RouterLink to="/AdminPage">Gestion Admin </RouterLink>
          </div>
        </li>
      </ul>
    </div>
  </nav> -->
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
}

/*header {
  line-height: 1.5;
  max-height: 100vh;

}

.logo {
  display: block;
  margin: auto;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: left;
    top: 1px;
    left: 1px;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    top: 1px;
    left: 1px;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -10rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}*/
</style>
