<template>
  <v-app :class="{ 'pa-3': $vuetify.breakpoint.smAndUp }" :dark="true">
    <v-container>
      <h3 class="headline">Riders list!</h3>
      <p>Here should be a table of riders :(</p>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: "RidersList",
  data() {
    return {};
  },
};
</script>

<style scoped></style>
