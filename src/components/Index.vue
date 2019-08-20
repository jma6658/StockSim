<template>
  <ion-grid>
    <ion-row>
      <ion-list>
        <ion-label>NETFLIX</ion-label>
        <ion-icon name="md-arrow-dropup"></ion-icon>
        <ion-item>
          <ion-label>Item 2</ion-label>
        </ion-item>
        <ion-item>
          <ion-label>Item 3</ion-label>
        </ion-item>
        <ion-item>
          <ion-label>Item 4</ion-label>
        </ion-item>
        <ion-item>
          <ion-label>Item 5</ion-label>
        </ion-item>
      </ion-list>

      <ion-infinite-scroll threshold="100px" id="infinite-scroll">
        <ion-infinite-scroll-content loading-spinner="bubbles" loading-text="Loading more data..."></ion-infinite-scroll-content>
      </ion-infinite-scroll>
    </ion-row>
  </ion-grid>
</template>

<script>
export default {};
</script>