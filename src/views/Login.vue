<template>
  <UserLogin v-on:get-auth="login" />
</template>
<script>
import UserLogin from "../components/UserLogin.vue";

export default {
  name: "login",
  components: { UserLogin },
  data() {
    return {
      email: "",
      password: ""
    };
  },
  methods: {
    login(email, password) {
      this.$store
        .dispatch("retrieveToken", {
          email: email,
          password: password
        })
        .then(response => {
          this.$router.push({ name: "home" });
        });
    },
    showAlert() {
      return this.$ionic.alertController
        .create({
          header: "Enter Email",
          message: "Please enter a valid email address",
          buttons: ["OK"]
        })
        .then(a => a.present());
    }
  }
};
</script>