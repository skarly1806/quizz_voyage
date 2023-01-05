<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-white header">
    <div class="navbar-collapse">
      <div class="nav" style="right:-10px;">
        <RouterLink to="/">Accueil</RouterLink>
      </div>

      <ul class="collapse navbar-collapse justify-content-end">
        <div class="nav" style="top:10px;right:10px;">
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

.login_inp {
  right: 10%;
}

.login_text {}

.login {
  margin-left: 525px;
  left: 15%;
  top: -42%;
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
