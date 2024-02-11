<template>
  <v-card class="offer">
    <v-card-title class="justify-center">{{ this.brand }}</v-card-title>
    <v-card-subtitle class="font-weight-bold">Model: {{ this.model }}</v-card-subtitle>
    <v-card-text>
      <v-row>
        <v-col>Rok produkcji od: {{ this.productionYearFrom }}</v-col>
        <v-col>Rok produkcji do: {{ this.productionYearTo }}</v-col>
        <v-col>Przebieg do: {{ this.mileageLimit }} km</v-col>
        <v-col>Cena do: {{ this.priceLimit }} pln</v-col>
      </v-row>
    </v-card-text>
    <div v-if="this.showSpottedOffers">
      <spotted-offer v-for="(offer, index) in this.getSpottedOffersForSearchedParams" :key="index"
        :otomotoUrl="offer.otomoto_url"
        :dateSpotted="offer.date_spotted"
        :dateDisappeared="offer.date_disappeared"
        :otomotoTitle="offer.otomoto_title"
        :img="offer.img"
        :productionYear="offer.production_year"
        :mileage="offer.mileage"
        :price="offer.price"
      />
    </div>
    <v-pagination
      v-if="this.showSpottedOffers && this.getSpottedOffersLength > 10"
      v-model="spottedOffersPage"
      :length="this.getSpottedOffersLength / 10"
    ></v-pagination>
    <v-btn @click="this.toggleSpottedOffersVisibility" block>
      Znalezione oferty
      <v-icon>
        {{ this.getSpottedOffersButtonIcon }}
      </v-icon>
    </v-btn>
  </v-card>
</template>

<script>
import { mapGetters } from 'vuex'
import SpottedOffer from './SpottedOffer.vue'
export default {
  name: 'SearchedOffer',
  components: { SpottedOffer },

  props: {
    id: Number,
    brand: String,
    model: String,
    productionYearFrom: Number,
    productionYearTo: Number,
    mileageLimit: Number,
    priceLimit: Number
  },

  data () {
    return {
      showSpottedOffers: false,
      spottedOffersPage: 1
    }
  },

  computed: {
    ...mapGetters([
      'spottedOffers'
    ]),

    getSpottedOffersForSearchedParams () {
      const offersPerPage = 10
      const filteredOffers = this.spottedOffers.filter(offer => {
        return offer.searched_offer === this.id
      })
      return filteredOffers.length > 10
        ? filteredOffers.slice(this.spottedOffersPage - 1, this.spottedOffersPage - 1 + offersPerPage)
        : filteredOffers
    },

    getSpottedOffersLength () {
      return this.spottedOffers.filter(offer => {
        return offer.searched_offer === this.id
      }).length
    },

    getSpottedOffersButtonIcon () {
      return this.showSpottedOffers ? 'mdi-menu-up' : 'mdi-menu-down'
    }
  },

  methods: {
    toggleSpottedOffersVisibility () {
      this.showSpottedOffers = !this.showSpottedOffers
    }
  }
}
</script>

<style>
.offer{
  width: 70%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 50px;
}
</style>
