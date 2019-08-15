import Vue from "vue";
import {
  IonicVueRouter
} from "@ionic/vue";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue"

Vue.use(IonicVueRouter);

export default new IonicVueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [{
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/login",
      name: "login",
      component: Login
    }
  ]
});