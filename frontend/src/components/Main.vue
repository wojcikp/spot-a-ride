<template>
<v-app id="spot-a-ride">

    <v-app-bar
      app
      clipped-left
      flat
      dark
      shrink-on-scroll
      src="../assets/muscle.jpg"
    >
    <template v-slot:img="{ props }">
      <v-img
        v-bind="props"
        gradient="to top right, rgba(19,84,122,.5), rgba(128,208,199,.8)"
      ></v-img>
    </template>
      <v-toolbar-title class="toolbar-title">Spot a ride</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-navigation-drawer app clipped>
      <v-list>
        <v-list-item
              v-for="item in this.items"
              :key="item.title"
              link
            >
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
      </v-list>
    </v-navigation-drawer>

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
import SearchedOffer from './SearchedOffer.vue'
export default {
  components: { SearchedOffer },
  name: 'MainPage',

  data () {
    return {
      items: [
        { title: 'Spotted offers', icon: 'mdi-view-dashboard' },
        { title: 'Add offer', icon: 'mdi-image' },
        { title: 'About', icon: 'mdi-help-box' }
      ],
      right: null
    }
  },

  computed: {
    ...mapGetters([
      'searchedOffers'
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
  }
}
</script>

<style>
.toolbar-title{
  margin-left: 20%;
}
</style>
