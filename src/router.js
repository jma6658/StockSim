import Vue from "vue";
import {
  IonicVueRouter
} from "@ionic/vue";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
<<<<<<< HEAD
import Logout from "./views/Logout.vue";
=======
>>>>>>> 45f3200e922f54ec731e1bf98443ccc2c1395f8e

Vue.use(IonicVueRouter);

export default new IonicVueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [{
      path: "/",
      name: "home",
<<<<<<< HEAD
      component: Home,
      meta: {
        requiresAuth: true,
      }
=======
      component: Home
>>>>>>> 45f3200e922f54ec731e1bf98443ccc2c1395f8e
    },
    {
      path: "/login",
      name: "login",
<<<<<<< HEAD
      component: Login,
      meta: {
        requiresVisitor: true,
      }
    },
    {
      path: "/logout",
      name: "logout",
      component: Logout
=======
      component: Login
>>>>>>> 45f3200e922f54ec731e1bf98443ccc2c1395f8e
    }
  ]
});