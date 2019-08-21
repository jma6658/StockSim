<template>
    <div class="home">
    <UserLogin v-on:get-auth="getAuth" />
  </div>

</template>

<script>
import UserLogin from "../components/UserLogin.vue";

export default {
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
}


</script>