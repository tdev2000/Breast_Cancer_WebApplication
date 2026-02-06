<template>
  <nav class="navbar" v-if="isLoggedIn">
    <div class="side">
      <!--Image logo -->
      <img src="@/assets/logo.png" class="logo" @click="goHome"/>

      <span class="brand">Breast Cancer AI</span>
    </div>

    <!-- Right: Tab buttons -->
    <div class="right">
      <span class="tab" @click="$router.push('/dashboard')">Dashboard</span>
      <span class="tab" @click="$router.push('/upload')">Upload</span>
      <span class="tab" @click="$router.push('/patients')">Patient Details</span>
      <span class="tab" @click="$router.push('/logout')">Logout</span>
    </div>
  </nav>
</template>

<script>
import { computed } from 'vue';

export default {
    computed :{
      isLoggedIn() {
        return localStorage.getItem("isLoggedIn") === "true";
      }
    },
    methods: {    
      goHome() {
        this.$router.push('/');
      },
      logout() {
        localStorage.removeItem("isLoggedIn");
        this.$router.push('/');
      }
  }
};
</script>

<style scoped>
.navbar {
  position: relative;
  display: flex;
  align-items: center;
  padding: 15px 40px;
  background: #F4BCDA;
  border-bottom: 1px solid #E1E6EC;
}

/* Left empty space */
.side {
  width: 60px;
}

/* Centered brand */
.center {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
}

.brand {
  font-weight: bold;
  font-size: 20px;
  color: #B7087A;
}

.logo {
  height: 34px;
  margin-right: 10px;
  cursor: pointer;
}

/* Right tabs */
.right {
  margin-left: auto;
}

.tab {
  margin-left: 20px;
  cursor: pointer;
  font-weight: 600;
  color: #B7087A;
}

.logout {
  color: #8B0000;
}
</style>
