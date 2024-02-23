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
</style>
