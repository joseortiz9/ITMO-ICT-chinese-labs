<template>
  <div>
    <v-toolbar flat>
      <v-toolbar-title class="grey--text">
        {{ 'Reservations list' }}
      </v-toolbar-title>
    </v-toolbar>
    <v-divider></v-divider>
    <v-data-table
        :headers="headers"
        :items="reservations"
        :items-per-page="5"
        class="elevation-1"
    >
      <template v-slot:item.actions="{ item }">
        <v-icon small class="ml-2" @click="handleDelete(item)">mdi-trash-can</v-icon>
      </template>
    </v-data-table>
  </div>
</template>

<script>

import axiosInstance from "@/utils/axios";

export default {
  name: 'ReservationsListView',
  data() {
    return {
      reservations: [],
      headers: [
        { text: "#", value: "id" },
        { text: "costumer", value: "costumer_id" },
        { text: "№ of room", value: "room_number_str" },
        { text: "Start date", value: "start_date" },
        { text: "Finish date", value: "finish_date" },
        { text: "Created at", value: "created_at" },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
    };
  },
  methods: {
    handleDelete(row) {
      console.log(row);
      if (!confirm('Are you sure want to delete the reservation? This can not be undone')) return;
      alert('This will be soon!:)');
      //this.$router.push(`/hotels/${row.id}`);
    },
  },
  mounted() {
    axiosInstance
        .get(`/api/reservations`)
        .then((response) => {
          if (response.status === 200) {
            this.reservations = response.data.map(item => ({...item, room_number_str: item.room.room_number}));
          } else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the reservations, try again - ${err}`);
        });
  },
};
</script>

<style scoped></style>
