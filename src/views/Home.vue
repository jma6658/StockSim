<template>
  <div class="home">
    <Navigation />
    <!-- <UserLogin v-on:get-auth="getAuth" /> -->
  </div>
</template>

<script>
// @ is an alias to /src
//import UserLogin from "../components/UserLogin.vue";
import Navigation from "../components/Navigation.vue";

export default {
  name: "home",
  components: {
    // UserLogin,
    Navigation
  },
  methods: {
    async getAuth(email, password) {
      //console.log(email + " " + password);
      // const res = await fetch(`url`);
      // if (res.status == 404) {
      //   this.showAlert();
      // }
      // const info = res.json();
    }
  }
};
</script>
