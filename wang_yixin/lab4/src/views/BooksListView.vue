<template>
  <div>
    <v-toolbar flat>
      <v-toolbar-title class="grey--text">
        {{ 'Books list' }}
      </v-toolbar-title>
    </v-toolbar>
    <v-divider></v-divider>
    <v-data-table
        :headers="headers"
        :items="hotels"
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
import {getCreatorName} from "@/utils";

export default {
  name: 'BooksListView',
  data() {
    return {
      hotels: [],
      headers: [
        { text: 'Actions', value: 'actions', sortable: false },
        { text: "#", value: "id" },
        { text: "Name", value: "name" },
        { text: "Owner", value: "creator_name" },
        { text: "Created at", value: "created_at" },
      ],
    };
  },
  methods: {
    handleClickRow(row) {
      this.$router.push(`/hotels/${row.id}`);
    },
  },
  mounted() {
    axiosInstance
        .get(`/api/hotels`)
        .then((response) => {
          if (response.status === 200) {
            this.hotels = response.data.map((item) => ({...item, creator_name: getCreatorName(item.owner)}));
          } else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the hotels, try again - ${err}`);
        });
  },
};
</script>

<style scoped></style>
