<template>
  <div>
    <v-toolbar flat>
      <v-toolbar-title class="grey--text">
        {{ 'Room Details' }}
      </v-toolbar-title>
    </v-toolbar>
    <v-divider></v-divider>
    <div class="my-4">
      <room-card :data="room" :clickable="false" :can-reserve="true"></room-card>
    </div>
    <v-divider></v-divider>
    <v-data-table
        :headers="commentsHeaders"
        :items="comments"
        :items-per-page="3"
        class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Comments</v-toolbar-title>
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
                New comment
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">New Comment</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field
                          v-model="newComment.text"
                          label="Text"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field
                          v-model="newComment.rating"
                          label="Rating"
                          type="number"
                          min="0"
                          max="10"
                          hint="(min=0; max=10)"
                          persistent-hint
                      ></v-text-field>
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
                    @click="saveNewComment"
                    :disabled="
                      newComment.rating < 0 ||
                      newComment.rating > 10 ||
                      newComment.text.length < 3
                    "
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

import RoomCard from "@/components/RoomCard";
import axiosInstance from "@/utils/axios";
import {getCreatorName} from "@/utils";

export default {
  name: 'RoomDetailsView',
  components: {
    RoomCard
  },
  data() {
    return {
      room: {},
      comments: [],
      commentsHeaders: [
        { text: "#", value: "id" },
        { text: "Text", value: "text" },
        { text: "Rating", value: "rating" },
        { text: "creator", value: "creator_name" },
        { text: "created at", value: "created_at" },
      ],
      dialog: false,
      defaultComment: {
        text: "",
        rating: 0,
      },
      newComment: {
        text: "",
        rating: 0,
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
        this.newComment = Object.assign({}, this.defaultComment);
      });
    },
    saveNewComment() {
      axiosInstance
          .post(`/api/rooms/${this.$route.params.id}/comments`, this.newComment)
          .then((response) => {
            if (response) {
              this.loadComments();
              this.closeDialog();
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
    loadRoomData() {
      axiosInstance
          .get(`/api/rooms/${this.$route.params.id}`)
          .then((response) => {
            if (response.status === 200) this.room = response.data;
            else throw new Error("Error");
          })
          .catch((err) => {
            alert(`Error loading the room details, try again - ${err}`);
          });
      axiosInstance
          .get(`/api/rooms/${this.$route.params.id}/reserved`)
          .then((response) => {
            const auth_reservation = !response.data.start_date && !response.data.finish_date ? null : response.data;
            if (response.status === 200) this.room = {...this.room, auth_reservation};
            else throw new Error("Error");
          })
          .catch((err) => {
            alert(`Error loading the room details, try again - ${err}`);
          });
    },
    loadComments() {
      axiosInstance
          .get(`/api/rooms/${this.$route.params.id}/comments`)
          .then((response) => {
            if (response.status === 200) {
              this.comments = response.data.map((item) => ({
                ...item,
                creator_name: getCreatorName(item.creator),
              }));
            } else throw new Error("Error");
          })
          .catch((err) => {
            alert(`Error loading the comments, try again - ${err}`);
          });
    },
  },
  mounted() {
    this.loadRoomData();
    this.loadComments();
  },
};
</script>

<style scoped></style>
