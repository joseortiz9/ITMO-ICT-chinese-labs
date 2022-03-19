<template>
  <div id="app">
    <v-app>
      <v-app-bar color="deep-purple accent-4" class="flex-grow-0" dark extended flat>
        <v-app-bar-nav-icon @click.stop="sidebar = !sidebar"></v-app-bar-nav-icon>
        <v-toolbar-title>Hotels system</v-toolbar-title>
        <v-spacer></v-spacer>
        <div v-if="logged">
          <v-btn v-for="item in menuItems" :key="item.path" :to="item.path" link text>
            {{ item.title }}
          </v-btn>
          <v-btn text @click="onLogout">
            Logout
          </v-btn>
        </div>
        <div v-else>
          <v-btn to="/auth" link text>
            Auth
          </v-btn>
        </div>
      </v-app-bar>
      <v-main>
        <v-card
            class="mx-auto"
            max-width="900"
            style="margin-top: -64px;"
        >
          <router-view></router-view>
        </v-card>
      </v-main>

      <v-navigation-drawer v-model="sidebar" absolute bottom temporary>
        <v-list nav dense>
          <v-list-item-group
              v-if="logged"
              v-model="groupLinks"
              active-class="deep-purple--text text--accent-4"
          >
            <v-list-item v-for="item in menuItems" :key="item.path" :to="item.path" link>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
            <v-list-item @click="onLogout">
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item>
          </v-list-item-group>
          <v-list-item-group
              v-else
              v-model="groupLinks"
              active-class="deep-purple--text text--accent-4"
          >
            <v-list-item to="/auth" link>
              <v-list-item-title>Auth</v-list-item-title>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </v-app>
  </div>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      logged: false,
      sidebar: false,
      groupLinks: null,
      menuItems: [
        {title: 'Home', path: '/', icon: 'home'},
        {title: 'Hotels', path: '/hotels', icon: 'face'},
        {title: 'Reservations', path: '/reservations', icon: 'lock_open'}
      ]
    };
  },
  watch: {
    group() {
      this.sidebar = false
    },
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
}
</style>
