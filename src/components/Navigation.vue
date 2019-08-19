<template>
  <div>
    <ion-menu side="start" menuId="first">
      <ion-header translucent>
        <ion-toolbar>
          <ion-title>Menu</ion-title>
        </ion-toolbar>
      </ion-header>
      <ion-content fullscreen>
        <ion-list>
          <ion-item v-bind:key="item.id" v-for="item in items">
            <ion-icon slot="start" :name="item.icon" :style="{color: item.color}"></ion-icon>
            <ion-label>
              <h3>{{item.title}}</h3>
            </ion-label>
          </ion-item>
          <router-link :to="{ name: 'logout' }">
            <ion-item v-if="loggedIn">
              <ion-icon slot="start" name="log-out" style="color: #444"></ion-icon>
              <ion-label>
                <h3>Logout</h3>
              </ion-label>
            </ion-item>
          </router-link>
        </ion-list>
      </ion-content>
    </ion-menu>
    <div class="ion-page" main>
      <ion-header>
        <ion-toolbar>
          <ion-buttons slot="start">
            <ion-menu-button></ion-menu-button>
          </ion-buttons>
          <ion-title>Home</ion-title>
        </ion-toolbar>
      </ion-header>
      <ion-content></ion-content>
    </div>
    <ion-menu-controller></ion-menu-controller>
  </div>
</template>

<script>
export default {
  name: "navigation",
  components: {},
  computed: {
    loggedIn() {
      return this.$store.getters.loggedIn;
    }
  },
  data() {
    return {
      items: [
        {
          id: 1,
          title: "MyStocks",
          icon: "trending-up",
          color: "#F2AB27"
        },
        {
          id: 2,
          title: "Market",
          icon: "stats",
          color: "#F28705"
        },
        {
          id: 3,
          title: "MyAccount",
          icon: "person",
          color: "#261419"
        }
      ]
    };
  },
  methods: {
    openMenu() {
      document.querySelector("ion-menu-controller").open();
    }
  }
};
</script>