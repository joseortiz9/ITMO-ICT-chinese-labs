<template>
  <div id="app">
    <nav v-if="logged">
      <router-link to="/races">Races</router-link> |
      <router-link to="/riders">Riders</router-link> |
      <a role="button" @click="onLogout">Logout</a>
    </nav>
    <router-view />
  </div>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      logged: false,
    };
  },
  mounted() {
    if (sessionStorage.getItem("authToken")) {
      this.logged = true;
    }
  },
  methods: {
    onLogout() {
      if (!confirm("Are u sure to logout?")) return;
      axiosInstance
        .post("/auth/token/logout/")
        .then(() => {
          sessionStorage.removeItem("authToken");
          sessionStorage.removeItem("username");
          window.location.href = "/auth";
        })
        .catch((err) => {
          if (err?.response?.data) alert(JSON.stringify(err.response.data));
        });
    },
  },
};
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
