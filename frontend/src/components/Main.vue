<template>
  <v-app id="spot-a-ride">
    <upper-bar />
    <main-menu />

    <div class="first-search-btn" v-if="!this.searchedOffers.length">
      <v-btn @click="$router.push('/add-searched-offer')">Dodaj swój pierwszy samochód do śledzenia</v-btn>
    </div>

    <searched-offer v-for="(offer, index) in this.searchedOffers" :key="index"
      :id="offer.id"
      :brand="offer.brand"
      :model="offer.model"
      :mileageLimit="offer.mileage_limit"
      :priceLimit="offer.price_limit"
      :productionYearFrom="offer.production_year_from"
      :productionYearTo="offer.production_year_to"
    />

    <snack-bar />
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MainMenu from './MainMenu.vue'
import SearchedOffer from './SearchedOffer.vue'
import UpperBar from './UpperBar.vue'
import SnackBar from './SnackBar.vue'

export default {
  components: { MainMenu, SearchedOffer, UpperBar, SnackBar },
  name: 'MainPage',

  computed: {
    ...mapGetters([
      'searchedOffers',
      'authToken',
      'userId'
    ])
  },

  mounted () {
    if (this.authToken && this.userId) {
      setInterval(() => {
        const date = new Date()
        if (date.getMinutes() === 10) {
          this.getSearchedOffers()
          this.getSpottedOffers()
        }
      }, 1000 * 60)
    } else {
      this.$router.push('/register-and-login')
    }
  },

  methods: {
    ...mapActions([
      'getSearchedOffers',
      'getSpottedOffers'
    ])
  }
}
</script>

<style>
.toolbar-title{
  margin-left: 20%;
}
.first-search-btn{
  margin-top: 100px;
  margin-left: auto;
  margin-right: auto;
}
</style>
