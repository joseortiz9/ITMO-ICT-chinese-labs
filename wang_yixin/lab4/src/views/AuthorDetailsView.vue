<template>
  <div>
    <v-toolbar color="primary lighten-3" flat>
      <v-toolbar-title class="white--text">
        {{ 'Author Details' }}
      </v-toolbar-title>
    </v-toolbar>
    <v-divider></v-divider>
    <v-container>
      <h3 class="text--primary">{{ author.first_name }} {{ author.last_name }}</h3>
      <h4 class="text--primary">Birthday: {{ author.birthday }}</h4>
      <h5 class="text--secondary">№ of books written: {{ books.length }}</h5>
    </v-container>
    <v-divider></v-divider>
    <v-data-table
        :headers="bookHeaders"
        :items="books"
        :items-per-page="5"
        class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Author books</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                  color="primary"
                  dark
                  class="mb-2"
                  v-bind="attrs"
                  v-on="on"
              >
                New Book
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">New Book</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="12">
                      <v-text-field v-model="newBook.book_name" label="Name"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="12">
                      <v-select
                          v-model="newBook.Type"
                          :items="typeOptions"
                          item-text="name"
                          item-value="id"
                          label="Type"
                      ></v-select>
                    </v-col>
                    <v-col cols="12" sm="12">
                      <v-menu
                          v-model="publishDateMenu"
                          :close-on-content-click="false"
                          :nudge-right="40"
                          transition="scale-transition"
                          offset-y
                          min-width="auto"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                              v-model="newBook.year_of_pub"
                              label="Publish date"
                              prepend-icon="mdi-calendar"
                              readonly
                              v-bind="attrs"
                              v-on="on"
                          ></v-text-field>
                        </template>
                        <v-date-picker
                            v-model="newBook.year_of_pub"
                            :max="now_date"
                            @input="publishDateMenu = false"
                        ></v-date-picker>
                      </v-menu>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDialog">
                  Cancel
                </v-btn>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="saveNewBook"
                    :disabled="newBook.Type === null || newBook.book_name.length < 3"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
    </v-data-table>
  </div>
</template>

<script>

import axiosInstance from "@/utils/axios";

export default {
  name: 'AuthorDetailsView',
  components: {},
  data() {
    return {
      author: {},
      books: [],
      bookHeaders: [
        { text: "#", value: "id" },
        { text: "Name", value: "book_name" },
        { text: "Type", value: "Type" },
        { text: "Published at", value: "year_of_pub" },
      ],
      typeOptions: [
        { id: "n", name: "novel" },
        { id: "m", name: "magazine" },
        { id: "t", name: "tools" },
      ],
      now_date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      publishDateMenu: false,
      dialog: false,
      defaultBook: {
        book_name: "",
        year_of_pub: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
        Type: null,
      },
      newBook: {
        book_name: "",
        year_of_pub: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
        Type: null,
      },
    };
  },
  watch: {
    dialog(val) {
      val || this.closeDialog();
    },
  },
  methods: {
    closeDialog() {
      this.dialog = false;
      this.$nextTick(() => {
        this.newBook = Object.assign({}, this.defaultBook);
      });
    },
    saveNewBook() {
      const input = {...this.newBook, author: this.$route.params.id};
      axiosInstance
          .post(`/library/books/create/`, input)
          .then((response) => {
            if (response) {
              this.loadAuthorBooks();
              this.closeDialog();
            } else throw new Error("Error");
          })
          .catch((err) => {
            alert(
                `Error creating the book, try again - ${
                    err?.response?.data ? JSON.stringify(err.response.data) : err
                }`
            );
          });
    },
    loadAuthorBooks() {
      axiosInstance
          .get(`/library/authors/${this.$route.params.id}/books`)
          .then((response) => {
            if (response.status === 200) this.books = response.data;
            else throw new Error("Error");
          })
          .catch((err) => {
            alert(`Error loading the books from author, try again - ${err}`);
          });
    }
  },
  mounted() {
    axiosInstance
        .get(`/library/authors/${this.$route.params.id}`)
        .then((response) => {
          if (response.status === 200) this.author = response.data;
          else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the author data, try again - ${err}`);
        });
    this.loadAuthorBooks();
  },
};
</script>

<style scoped></style>
