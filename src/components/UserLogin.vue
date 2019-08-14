<template>
  <ion-card>
    <form @submit="submitLogin">
      <ion-card-header>
        <ion-card-title>Login</ion-card-title>
      </ion-card-header>

      <ion-card-content>
        <ion-item>
          <ion-label position="stacked">EMAIL</ion-label>
          <ion-input
            type="email"
            :value="email"
            @input="email=$event.target.value"
            placeholder="example@domain.com"
          ></ion-input>
        </ion-item>
        <ion-item>
          <ion-label position="stacked">PASSWORD</ion-label>
          <ion-input type="password" :value="password" @input="password=$event.target.value"></ion-input>
        </ion-item>

        <ion-button
          class="button button-outline"
          style="margin-top: 20px"
          type="submit"
          expand="block"
        >Sign-in</ion-button>
      </ion-card-content>
    </form>
  </ion-card>
</template>

<script>
export default {
  name: "UserLogin",
  data() {
    return {
      email: "",
      password: ""
    };
  },
  components: {},
  methods: {
    submitLogin(e) {
      e.preventDefault();

      // Email Regex
      // eslint-disable-next-line
      var isValidEmail = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
        String(this.email).toLowerCase()
      );

      // Test for valid Email
      if (!isValidEmail) {
        this.showAlert();
        this.email = "";
        this.password = "";
      } else {
        this.$emit("get-auth", this.email, this.password);
        this.email = "";
        this.password = "";
      }
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