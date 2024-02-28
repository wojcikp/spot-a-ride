<template>
  <v-card class="offer">
    <v-card-title class="otomoto-brand justify-center">{{ this.getPrettyBrandName(this.brand) }}</v-card-title>
    <v-card-subtitle class="otomoto-model font-weight-bold">Model: {{ this.model }}</v-card-subtitle>
    <v-card-text>
      <v-row>
        <v-col class="otmoto-params"><b>Rok produkcji od: </b>{{ this.productionYearFrom }}</v-col>
        <v-col class="otmoto-params"><b>Rok produkcji do: </b>{{ this.productionYearTo }}</v-col>
        <v-col class="otmoto-params"><b>Przebieg do: </b>{{ this.mileageLimit }} km</v-col>
        <v-col class="otmoto-params"><b>Cena do: </b>{{ this.priceLimit }} pln</v-col>
      </v-row>
    </v-card-text>
    <div v-if="this.showSpottedOffers">
      <spotted-offer v-for="(offer, index) in this.getSpottedOffersForSearchedParams" :key="index"
        :offerId="offer.id"
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
      class="mt-6 mb-4"
      v-if="this.showSpottedOffers && this.getSpottedOffersLength > 10"
      v-model="spottedOffersPage"
      :length="Math.ceil(this.getSpottedOffersLength / 10)"
      total-visible="10"
    />
    <v-btn @click="this.editOffer" x-small class="ma-3">Edytuj</v-btn>
    <v-btn @click="this.deleteOffer" x-small class="ma-3" color="grey lighten-1">Usuń</v-btn>
    <v-btn @click="this.toggleSpottedOffersVisibility" block>
      Znalezione oferty ({{ this.getSpottedOffersLength }})
      <v-icon>
        {{ this.getSpottedOffersButtonIcon }}
      </v-icon>
    </v-btn>
  </v-card>
</template>

<script>
import { BRAND_NAMES } from '../consts'
import { mapActions, mapGetters, mapMutations } from 'vuex'
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
      const filteredOffers = this.spottedOffers.filter(offer => offer.searched_offer === this.id)
      return filteredOffers.length > 10
        ? filteredOffers.slice((this.spottedOffersPage - 1) * offersPerPage, this.spottedOffersPage * offersPerPage)
        : filteredOffers
    },
    getSpottedOffersLength () {
      return this.spottedOffers.filter(offer => offer.searched_offer === this.id).length
    },
    getPagesAmount () {
      return this.getSpottedOffersLength / 10
    },
    getSpottedOffersButtonIcon () {
      return this.showSpottedOffers ? 'mdi-menu-up' : 'mdi-menu-down'
    }
  },

  methods: {
    ...mapActions([
      'removeSearchedOffer',
      'getSearchedOffers',
      'getSpottedOffers',
      'getSpottedOffersForNewSearch'
    ]),
    ...mapMutations([
      'setSearchedOfferToEdit'
    ]),
    toggleSpottedOffersVisibility () {
      this.showSpottedOffers = !this.showSpottedOffers
    },
    editOffer () {
      this.setSearchedOfferToEdit(this.id)
      this.$router.push('/add-searched-offer')
    },
    async deleteOffer () {
      await this.removeSearchedOffer(this.id)
      await this.getSearchedOffers()
      await this.getSpottedOffers()
      this.$router.push('/')
    },
    getPrettyBrandName (brandName) {
      const name = BRAND_NAMES.find(item => item.value === brandName)
      if (name) return name.text
      else return brandName
    }
  }
}
</script>

<style scoped>
.offer{
  width: 70%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 50px;
}
.otomoto-brand{
  font-size: 22px;
}
.otomoto-model{
  font-size: 18px;
}
.otmoto-params{
  font-size: 16px;
}
</style>
