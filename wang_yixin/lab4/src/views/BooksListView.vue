<template>
  <div>
    <v-toolbar color="primary lighten-3" flat>
      <v-toolbar-title class="white--text">
        {{ 'Books table' }}
      </v-toolbar-title>
    </v-toolbar>
    <v-divider></v-divider>
    <v-data-table
        :headers="headers"
        :items="books"
        :items-per-page="5"
        class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>

import axiosInstance from "@/utils/axios";
import {getCreatorName} from "@/utils";

export default {
  name: 'BooksListView',
  data() {
    return {
      books: [],
      headers: [
        { text: "#", value: "id" },
        { text: "Name", value: "book_name" },
        { text: "Type", value: "Type" },
        { text: "Published at", value: "year_of_pub" },
        { text: "Author", value: "author_name" },
      ],
    };
  },
  methods: {},
  mounted() {
    axiosInstance
        .get(`/library/books`)
        .then((response) => {
          if (response.status === 200) {
            this.books = response.data.books.map(item => ({...item, author_name: getCreatorName(item.author)}));
          } else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the books, try again - ${err}`);
        });
  },
};
</script>

<style scoped></style>
