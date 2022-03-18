<template>
  <v-card
    class="mx-auto"
    max-width="400"
    :to="clickable ? `races/${data.id}` : ''"
    :link="clickable"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
    >
      <v-card-title>{{ data.name }}</v-card-title>
    </v-img>
    <v-card-subtitle class="pb-0">
      {{ data.description }}
    </v-card-subtitle>
    <v-card-text class="text--primary mt-2">
      <div><b>Start time:</b> {{ data.start_time || "---" }}</div>
      <div><b>Start time:</b> {{ data.finish_time || "---" }}</div>
      <div><b>Winner:</b> {{ data.winner ? data.winner.name : "---" }}</div>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        text
        :color="
          data.start_time && !data.winner
            ? 'green'
            : !data.start_time && !data.winner
            ? 'red'
            : 'blue'
        "
      >
        Status:
        {{
          data.start_time && !data.winner
            ? "In Progress"
            : !data.start_time && !data.winner
            ? "Not started"
            : "Finished"
        }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    data: {
      type: Object,
      default: () => ({}),
    },
    clickable: {
      type: Boolean,
      default: true,
    },
  },
};
</script>

<style scoped></style>
