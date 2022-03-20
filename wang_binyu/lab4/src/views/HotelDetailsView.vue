<template>
  <div>
    <v-toolbar flat>
      <v-toolbar-title class="grey--text">
        {{ 'Hotel Details' }}
      </v-toolbar-title>
    </v-toolbar>
    <v-divider></v-divider>
    <v-container>
      <h3 class="text--primary">Hotel: {{ hotel.name }}</h3>
      <h4 class="text--primary">Owner: {{ hotel.owner.username }}</h4>
      <h5 class="text--secondary">№ of rooms: {{ rooms.length }}</h5>
      <v-divider></v-divider>
      <v-row class="mt-4">
        <v-col v-for="room in rooms" :key="room.id" cols="12" sm="4">
          <room-card :data="room"></room-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>

import axiosInstance from "@/utils/axios";
import RoomCard from "@/components/RoomCard";

export default {
  name: 'HotelDetailsView',
  components: {
    RoomCard
  },
  data() {
    return {
      hotel: {},
      rooms: []
    };
  },
  methods: {},
  mounted() {
    axiosInstance
        .get(`/api/hotels/${this.$route.params.id}`)
        .then((response) => {
          if (response.status === 200) this.hotel = response.data;
          else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the hotel data, try again - ${err}`);
        });
    axiosInstance
        .get(`/api/hotels/${this.$route.params.id}/rooms`)
        .then((response) => {
          if (response.status === 200) this.rooms = response.data;
          else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the rooms, try again - ${err}`);
        });
  },
};
</script>

<style scoped></style>
