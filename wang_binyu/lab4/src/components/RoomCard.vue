<template>
  <v-card class="mx-auto" max-width="400">
    <v-img
        class="white--text align-end"
        height="200px"
        :src="getPicture(parseInt(data.type))"
    >
      <v-card-title style="background-color: rgba(0, 0, 0, 0.6)">
        Room №: {{ data.room_number }}
      </v-card-title>
    </v-img>
    <v-card-subtitle class="pb-0">
      ${{ data.price }}
    </v-card-subtitle>
    <v-card-text class="text--primary mt-2">
      <div><b>Type:</b> {{ data.type }}</div>
    </v-card-text>
    <v-card-subtitle v-if="Boolean(data.auth_reservation)" class="pt-0">
      <div>Reservation dates: {{ data.auth_reservation.start_date }} ->
        {{ data.auth_reservation.finish_date ? data.auth_reservation.finish_date : 'Unknown' }}
      </div>
    </v-card-subtitle>
    <v-card-actions>
      <v-spacer></v-spacer>
      <div v-if="canReserve">
        <v-btn v-if="Boolean(data.auth_reservation)" text color="red" @click="handleDeleteReservation">
          Delete reservation
        </v-btn>
        <v-dialog
            v-else
            v-model="dialog"
            persistent
            max-width="400px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn text color="green" v-bind="attrs" v-on="on">
              Reserve
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">Reserve room for these days:</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="12">
                    <v-menu
                        v-model="startDateMenu"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        transition="scale-transition"
                        offset-y
                        min-width="auto"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                            v-model="start_date"
                            label="Start date*"
                            prepend-icon="mdi-calendar"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                        ></v-text-field>
                      </template>
                      <v-date-picker
                          v-model="start_date"
                          :min="now_date"
                          :max="finish_date === now_date ? null : finish_date"
                          @input="startDateMenu = false"
                      ></v-date-picker>
                    </v-menu>
                  </v-col>
                  <v-col cols="12" sm="12">
                    <v-menu
                        v-model="finishDateMenu"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        transition="scale-transition"
                        offset-y
                        min-width="auto"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                            v-model="finish_date"
                            label="Finish date"
                            prepend-icon="mdi-calendar"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                        ></v-text-field>
                      </template>
                      <v-date-picker
                          v-model="finish_date"
                          :min="start_date"
                          @input="finishDateMenu = false"
                      ></v-date-picker>
                    </v-menu>
                  </v-col>
                </v-row>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDialog">
                Close
              </v-btn>
              <v-btn color="blue darken-1" text @click="saveReservation">
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
      <v-btn v-if="clickable" text color="deep-purple" link :to="`/rooms/${data.id}`">Explore</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axiosInstance from "@/utils/axios";

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
    canReserve: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      dialog: false,
      now_date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      start_date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      finish_date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      startDateMenu: false,
      finishDateMenu: false
    };
  },
  methods: {
    closeDialog() {
      this.dialog = false;
      this.$nextTick(() => {
        this.start_date = this.now_date;
        this.finish_date = this.now_date;
      });
    },
    handleDeleteReservation() {
      if (!confirm('Are you sure want to delete the reservation? This can not be undone')) return;
      alert('This will be soon!:)');
    },
    saveReservation() {
      const newReservationInputs = {
        room_id: this.$props.data.id,
        start_date: this.start_date,
        finish_date: this.finish_date
      };
      axiosInstance
          .post(`/api/reservations`, newReservationInputs)
          .then((response) => {
            if (response) {
              this.$router.push('/reservations');
            } else throw new Error("Error");
          })
          .catch((err) => {
            alert(
                `Error creating the comment, try again - ${
                    err?.response?.data ? JSON.stringify(err.response.data) : err
                }`
            );
          });
    },
    getPicture(roomType) {
      switch (roomType) {
        case 2:
          return 'https://static.independent.co.uk/2021/07/27/08/20165319-4a072180-9f19-4240-8ff1-e94279ffcace.jpg?width=1200';
        case 4:
          return 'https://www.lottehotel.com/content/dam/lotte-hotel/lotte/stpetersburg/accommodation/standard/deluxeroom/180712-1-2000-acc-stpetersburg-hotel.jpg.thumb.768.768.jpg';
        case 3:
          return 'https://www.theleela.com/prod/content/assets/styles/hero_banner_1920x980/public/2021-07/Header_21.jpg?VersionId=u2NfbE8h0.Zh08UiCmGsMyfElMQ7AKbF&itok=7j9Lph7s';
        case 1:
        default:
          return 'https://www.dmarge.com/wp-content/uploads/2018/04/hotel-room.jpg';
      }
    },
  }
};
</script>

<style scoped></style>
