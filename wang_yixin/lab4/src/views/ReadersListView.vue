<template>
  <div>
    <v-toolbar color="primary lighten-3" flat>
      <v-toolbar-title class="white--text">
        {{ 'Readers list' }}
      </v-toolbar-title>
    </v-toolbar>
    <v-divider></v-divider>
    <v-container>
      <v-row class="mt-2">
        <v-col v-for="reader in readers" :key="reader.id" cols="12" sm="12">
          <v-card color="primary lighten-4">
            <div class="d-flex flex-no-wrap justify-space-between">
              <div>
                <v-card-title class="text-h5" v-text="`${reader.first_name} ${reader.last_name}`"></v-card-title>
                <v-card-subtitle v-text="`Sex: ${reader.sex}`" class="pb-1"></v-card-subtitle>
                <v-card-text v-text="`Birthday: ${reader.birthday}`" class="py-1"></v-card-text>
                <v-card-actions>
                  <v-btn class="ml-2 mt-1" outlined rounded small>
                    GIVE LIKE
                  </v-btn>
                </v-card-actions>
              </div>

              <v-avatar class="ma-3" size="125" tile>
                <v-img src="https://thumbs.dreamstime.com/b/hungry-knowledge-29448772.jpg"></v-img>
              </v-avatar>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>

import axiosInstance from "@/utils/axios";

export default {
  name: 'ReadersListView',
  data() {
    return {
      readers: [],
    };
  },
  methods: {},
  mounted() {
    axiosInstance
        .get(`/library/readers`)
        .then((response) => {
          if (response.status === 200) {
            this.readers = response.data.readers;
          } else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the readers, try again - ${err}`);
        });
  },
};
</script>

<style scoped></style>
