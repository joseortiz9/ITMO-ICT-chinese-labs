<template>
  <div>
    <v-toolbar color="primary lighten-3" flat>
      <v-toolbar-title class="white--text">
        {{ 'Authors table' }}
      </v-toolbar-title>
    </v-toolbar>
    <v-divider></v-divider>
    <v-data-table
        :headers="headers"
        :items="authors"
        :items-per-page="5"
        class="elevation-1"
        @click:row="handleClickRow"
    >
      <template v-slot:item.actions="{ item }">
        <v-icon small class="ml-2" @click="handleClickRow(item)">mdi-eye</v-icon>
      </template>
    </v-data-table>
  </div>
</template>

<script>

import axiosInstance from "@/utils/axios";

export default {
  name: 'AuthorsListView',
  data() {
    return {
      authors: [],
      headers: [
        { text: 'Actions', value: 'actions', sortable: false },
        { text: "#", value: "id" },
        { text: "Fist name", value: "first_name" },
        { text: "Last name", value: "last_name" },
        { text: "Birthday", value: "birthday" },
      ],
    };
  },
  methods: {
    handleClickRow(row) {
      this.$router.push(`/authors/${row.id}`);
    },
  },
  mounted() {
    axiosInstance
        .get(`/library/authors`)
        .then((response) => {
          if (response.status === 200) {
            this.authors = response.data;
          } else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the authors, try again - ${err}`);
        });
  },
};
</script>

<style scoped></style>
