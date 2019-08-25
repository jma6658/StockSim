<template>
<<<<<<< HEAD
  <UserLogin v-on:get-auth="login" />
</template>
=======
    <div class="home">
    <UserLogin v-on:get-auth="getAuth" />
  </div>

</template>

>>>>>>> 45f3200e922f54ec731e1bf98443ccc2c1395f8e
<script>
import UserLogin from "../components/UserLogin.vue";

export default {
<<<<<<< HEAD
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
=======
    name: "login",
    components: { UserLogin },
    methods: {
    // createCORSRequest(method, url) {
    //   var xhr = new XMLHttpRequest();
    //   if ("withCredentials" in xhr) {

    //     // Check if the XMLHttpRequest object has a "withCredentials" property.
    //     // "withCredentials" only exists on XMLHTTPRequest2 objects.
    //     xhr.open(method, url, true);

    //   } else if (typeof XDomainRequest != "undefined") {

    //     // Otherwise, check if XDomainRequest.
    //     // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
    //     xhr = new XDomainRequest();
    //     xhr.open(method, url);

    //   } else {

    //     // Otherwise, CORS is not supported by the browser.
    //     xhr = null;

    //   }
    //   return xhr;
    // },
    async getAuth(email, password) {
      console.log(email + " " + password);
      // const proxyurl = "https://cors-anywhere.herokuapp.com/";
      // var xhr = createCORSRequest('GET', url);
      // xhr.send();
      const res = await fetch(`http://localhost:8000/login/username=${email}&password=${password}`);
      if (res.status == 404) {
        this.showAlert();
      }
      const info = res.json();
      console.log(info);
    },
     clearInfo() {
       this.info = null;
>>>>>>> 45f3200e922f54ec731e1bf98443ccc2c1395f8e
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
<<<<<<< HEAD
};
=======
}


>>>>>>> 45f3200e922f54ec731e1bf98443ccc2c1395f8e
</script>