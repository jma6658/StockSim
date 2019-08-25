import Vue from "vue";
import Vuex from "vuex";
import App from "./App.vue";
import router from "./router";
import Ionic from "@ionic/vue";
import "@ionic/core/css/ionic.bundle.css";
import {
  store
} from "./store/store";

Vue.use(Ionic);
Vue.use(Vuex);

Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.loggedIn) {
      next({
        name: 'login',
      })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.requiresVisitor)) {
    if (store.getters.loggedIn) {
      next({
        name: 'home',
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store: store,
  render: h => h(App)
}).$mount("#app");