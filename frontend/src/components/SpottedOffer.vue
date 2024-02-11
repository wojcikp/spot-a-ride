<template>
  <v-card>
    <v-row>
      <v-col>
        <v-img
          max-width="250"
          :src="this.img"
        ></v-img>
      </v-col>
      <v-col>dateSpotted: {{ this.dateSpotted }}</v-col>
      <v-col>dateDisappeared: {{ this.dateDisappeared }}</v-col>
      <v-col>otomotoTitle: {{ this.otomotoTitle }}</v-col>
      <v-col>productionYear: {{ this.productionYear }}</v-col>
      <v-col>mileage: {{ this.mileage }}</v-col>
      <v-col>price: {{ this.price }}</v-col>
    </v-row>
    <v-row>
      <v-col>otomotoUrl: {{ this.otomotoUrl }}</v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: 'SpottedOffer',

  props: {
    otomotoUrl: String,
    dateSpotted: String,
    dateDisappeared: String,
    otomotoTitle: String,
    img: String,
    productionYear: Number,
    mileage: Number,
    price: Number
  }
}
</script>

<style>

</style>
