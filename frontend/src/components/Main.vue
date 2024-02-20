<template>
<v-app id="spot-a-ride">
  <upper-bar />
  <main-menu />

  <searched-offer v-for="(offer, index) in this.searchedOffers" :key="index"
    :id="offer.id"
    :brand="offer.brand"
    :model="offer.model"
    :mileageLimit="offer.mileage_limit"
    :priceLimit="offer.price_limit"
    :productionYearFrom="offer.production_year_from"
    :productionYearTo="offer.production_year_to"
  />

    <v-btn @click="this.getToken">GET TOKEN</v-btn>
    <v-btn @click="this.setUser">SET USER</v-btn>
    <v-btn @click="this.getSpotted">getSpotted</v-btn>
    <v-btn @click="this.getSearched">getSearched</v-btn>
    <v-btn @click="this.test">CLICK</v-btn>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MainMenu from './MainMenu.vue'
import SearchedOffer from './SearchedOffer.vue'
import UpperBar from './UpperBar.vue'

export default {
  components: { MainMenu, SearchedOffer, UpperBar },
  name: 'MainPage',

  computed: {
    ...mapGetters([
      'searchedOffers',
      'authToken',
      'userId'
    ])
  },

  methods: {
    ...mapActions([
      'createAccount',
      'getAuthToken',
      'getUserId',
      'getSearchedOffers',
      'addSearchedOffer',
      'getSpottedOffers'
    ]),
    getToken () {
      this.getAuthToken({ username: 'test', password: 'test' })
    },
    setUser () {
      this.getUserId()
    },
    getSearched () {
      this.getSearchedOffers()
    },
    getSpotted () {
      this.getSpottedOffers()
    },
    test () {
      // this.createAccount({ username: 'test2', password: 'test2' })
      // this.getAuthToken({ username: 'test', password: 'test' })
      // this.getUserId()
      // this.getSearchedOffers()

      this.addSearchedOffer({
        brand: 'Mazda',
        model: '3',
        productionYearFrom: '2014',
        productionYearTo: '2018',
        mileageLimit: '120000',
        priceLimit: '70000'
      })
      // this.getSpottedOffers()
    }
  },

  mounted: () => {
    this.$nextTick(() => {
      if (this.authToken && this.userId) {
        setInterval(() => {
          this.getSearchedOffers()
          this.getSpottedOffers()
        }, 1000 * 60)
      } else {
        this.$router.push('/register-and-login')
      }
    })
  }
}
</script>

<style>
.toolbar-title{
  margin-left: 20%;
}
</style>
