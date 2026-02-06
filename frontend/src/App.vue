<template>
  <!--Navebar only after login-->
  <Navbar v-if="isLoggedIn"/>
   <router-view/>
  </template>
  
  <script>
  import Navbar from './components/Navbar.vue';

  export default {
    components: { Navbar},
    computed: {
      isLoggedIn() {
        return localStorage.getItem("isLoggedIn") === "true";
      }
    }
  };
</script>
  <style>
  body {
    margin: 0;
    }

  #app {
    min-height: 100vh;
  }
  </style>