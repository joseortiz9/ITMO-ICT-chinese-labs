import Vue from 'vue';
import VueRouter from 'vue-router';
import UserAuthView from "@/views/UserAuthView";
import BooksListView from "@/views/BooksListView";
import AuthorsListView from "@/views/AuthorsListView";
import ReadersListView from "@/views/ReadersListView";

Vue.use(VueRouter);

const routes = [
  {
    path: '/books',
    name: 'BooksList',
    component: BooksListView,
  },
  {
    path: '/authors',
    name: 'AuthorsList',
    component: AuthorsListView,
  },
  {
    path: '/readers',
    name: 'ReadersList',
    component: ReadersListView,
  },
  // {
  //   path: '/books/:id',
  //   name: 'BookDetails',
  //   component: BookDetailsView,
  // },
  // {
  //   path: '/readers/create',
  //   name: 'ReaderCreate',
  //   component: ReaderCreateView,
  // },
  // {
  //   path: '/readers/:id',
  //   name: 'ReaderDetails',
  //   component: ReaderDetailsView,
  // },
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
