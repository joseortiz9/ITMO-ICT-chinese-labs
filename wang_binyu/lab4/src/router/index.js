import Vue from 'vue';
import VueRouter from 'vue-router';
import UserAuthView from '@/views/UserAuthView';
import HotelsListView from "@/views/HotelsListView";
import HotelDetailsView from "@/views/HotelDetailsView";
import RoomDetailsView from "@/views/RoomDetailsView";
import ReservationsListView from "@/views/ReservationsListView";

Vue.use(VueRouter);

const routes = [
  {
    path: '/hotels',
    name: 'HotelsList',
    component: HotelsListView,
  },
  {
    path: '/hotels/:id',
    name: 'HotelDetails',
    component: HotelDetailsView,
  },
  {
    path: '/rooms/:id',
    name: 'RoomDetails',
    component: RoomDetailsView,
  },
  {
    path: '/reservations',
    name: 'ReservationsList',
    component: ReservationsListView,
  },
  {
    path: '/auth',
    name: 'UserAuth',
    component: UserAuthView,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
    next();
  } else {
    next('/auth');
  }
});

export default router;
