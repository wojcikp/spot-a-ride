<template>
  <div>
    <v-form :disabled="disableForm" class="mt-10 pt-10">
      <v-container>
        <v-card class="pa-6">
          <v-row>
            <v-col
              cols="6"
            >
              <v-select
                :items="brands"
                v-model="brand"
                label="Marka:"
                required
              ></v-select>
            </v-col>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="model"
                label="Model:"
                hint="Podaj nazwę modelu identyczną jak na otomoto"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="productionYearFrom"
                label="Rok produkcji od:"
              ></v-text-field>
            </v-col>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="productionYearTo"
                label="Rok produkcji do:"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="mileageLimit"
                label="Przebieg do:"
              ></v-text-field>
            </v-col>
            <v-col
              cols="6"
            >
              <v-text-field
                v-model="priceLimit"
                label="Cena do:"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-btn
                v-on="this.editMode ? { click: this.editOffer } : {click: this.addOffer}"
                :disabled="this.brand === null || this.disableForm"
                color="teal darken-1"
                class="mr-3 white--text"
              >
                {{ this.editMode ? 'Edytuj' : 'Dodaj' }}
              </v-btn>
              <v-btn :disabled="this.disableForm" class="ml-3" @click="clearForm">Wyczyść</v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import { BRAND_NAMES } from '../consts'
import { mapActions, mapGetters, mapMutations } from 'vuex'

export default {
  name: 'NewSearchForm',

  data () {
    return {
      editMode: false,
      disableForm: false,
      brand: null,
      model: null,
      productionYearFrom: null,
      productionYearTo: null,
      mileageLimit: null,
      priceLimit: null,
      brands: BRAND_NAMES
    }
  },

  computed: {
    ...mapGetters([
      'searchedOfferToEdit',
      'searchedOffers'
    ])
  },

  mounted () {
    if (this.searchedOfferToEdit) {
      this.editMode = true
      const searchedOfferToEdit = this.searchedOffers.filter(offer => offer.id === this.searchedOfferToEdit)
      this.brand = searchedOfferToEdit[0].brand
      this.model = searchedOfferToEdit[0].model
      this.productionYearFrom = searchedOfferToEdit[0].production_year_from
      this.productionYearTo = searchedOfferToEdit[0].production_year_to
      this.mileageLimit = searchedOfferToEdit[0].mileage_limit
      this.priceLimit = searchedOfferToEdit[0].price_limit
    }
  },

  methods: {
    ...mapMutations([
      'setShowProgressBar'
    ]),
    ...mapActions([
      'addSearchedOffer',
      'editSearchedOffer',
      'getSearchedOffers',
      'getSpottedOffers',
      'getSpottedOffersForNewSearch'
    ]),
    async addOffer () {
      this.disableForm = true
      this.setShowProgressBar(true)
      const searchedOffer = await this.addSearchedOffer({
        brand: this.brand,
        model: this.model,
        productionYearFrom: this.productionYearFrom,
        productionYearTo: this.productionYearTo,
        mileageLimit: this.mileageLimit,
        priceLimit: this.priceLimit
      })
      await this.getSpottedOffersForNewSearch({
        searchedOfferId: searchedOffer.id,
        brand: searchedOffer.brand,
        model: searchedOffer.model,
        productionYearFrom: searchedOffer.production_year_from,
        productionYearTo: searchedOffer.production_year_to,
        mileageLimit: searchedOffer.mileage_limit,
        priceLimit: searchedOffer.price_limit
      })
      await this.getSpottedOffers()
      this.$router.push('/')
      this.setShowProgressBar(false)
      this.disableForm = false
      this.clearForm()
    },
    async editOffer () {
      this.disableForm = true
      this.setShowProgressBar(true)
      await this.editSearchedOffer({
        id: this.searchedOfferToEdit,
        brand: this.brand,
        model: this.model,
        productionYearFrom: this.productionYearFrom,
        productionYearTo: this.productionYearTo,
        mileageLimit: this.mileageLimit,
        priceLimit: this.priceLimit
      })
      this.editMode = false
      await this.getSearchedOffers()
      await this.getSpottedOffers()
      this.$router.push('/')
      this.setShowProgressBar(false)
      this.disableForm = false
      this.clearForm()
    },
    clearForm () {
      this.brand = null
      this.model = null
      this.productionYearFrom = null
      this.productionYearTo = null
      this.mileageLimit = null
      this.priceLimit = null
    }
  }
}
</script>
