<template>
  <!--Navebar only after login-->
  <Navbar v-if="showNavbar"/>
   <router-view/>
  </template>
  
  <script>
  import Navbar from './components/Navbar.vue';

  export default {
    components: { Navbar},
    computed: {
      showNavbar() {
        const isLoggedIn = localStorage.getItem("isLoggedIn") === "true";

        //Hide navbar on auth pages
        const hiddenPages = ['/', '/login', '/register'];

        return isLoggedIn && !hiddenPages.includes(this.$route.path);
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