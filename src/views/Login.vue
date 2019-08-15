<template>
  <UserLogin v-on:get-auth="getAuth" />
</template>
<script>
import UserLogin from "../components/UserLogin.vue";
export default {
  name: "login",
  components: { UserLogin },
  data() {
    return {
      info: null
    };
  },
  methods: {
    async getAuth(email, password) {
      const res = await fetch(`email=${email}password=${password}`);
      if (res.status == 404) {
        this.showAlert();
      }
      this.info = await res.json();

      // Check info.status if login is successful

      // if succesfull then execute Login method with token as param.

      // if not succesfull then send an alert that credentials is rejected.
    },
    showAlert() {
      return this.$ionic.alertController
        .create({
          header: "Enter Email",
          message: "Please enter a valid email address",
          buttons: ["OK"]
        })
        .then(a => a.present());
    },
    Login(token) {}
  }
};
</script>