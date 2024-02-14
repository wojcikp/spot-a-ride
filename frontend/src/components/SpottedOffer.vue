<template>
  <div class="pa-2 ma-2">
    <v-row class="pb-4">
      <v-col cols="3">
        <v-img
          max-width="250"
          :src="this.img"
        ></v-img>
      </v-col>
      <v-col cols="9">
        <v-row>
          <v-col class="otomoto-info"><b>Na otomoto od: </b><br>{{ getFormattedDate(this.dateSpotted) }}<br>{{ getFormattedTime(this.dateSpotted) }}</v-col>
          <v-col class="otomoto-info"><b>Nazwa na otomoto: </b><br>{{ this.otomotoTitle }}</v-col>
          <v-col class="otomoto-info"><b>Rok produkcji: </b><br>{{ this.productionYear }}</v-col>
          <v-col class="otomoto-info"><b>Przebieg: </b><br>{{ this.mileage }} km</v-col>
          <v-col class="otomoto-info"><b>Cena: </b><br>{{ this.price }} pln</v-col>
        </v-row>
        <v-row v-if="this.dateDisappeared" justify="center" align="end" style="height: 50%">
          <v-col class="otomoto-info">
            <b>Oferta zniknęła: </b><br>
            {{ getFormattedDate(this.dateDisappeared) }} {{ getFormattedTime(this.dateDisappeared) }}
          </v-col>
          <v-col class="otomoto-info">
            Była dostępna przez: <br>{{ getOfferAvailableDuration(this.dateSpotted, this.dateDisappeared) }}
          </v-col>
          <v-col>
            <v-btn @click="removeOffer">Usuń z listy</v-btn>
          </v-col>
        </v-row>
        <v-row v-else justify="center" align="end" style="height: 50%">
          <v-col cols="4"><v-btn @click="openUrlInNewTab">Idź do oferty na otomoto</v-btn></v-col>
        </v-row>
      </v-col>
    </v-row>
  <v-divider />
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'SpottedOffer',

  props: {
    offerId: Number,
    otomotoUrl: String,
    dateSpotted: String,
    dateDisappeared: String,
    otomotoTitle: String,
    img: String,
    productionYear: Number,
    mileage: Number,
    price: Number
  },

  methods: {
    ...mapActions([
      'removeSpottedOffer'
    ]),
    openUrlInNewTab () {
      window.open(this.otomotoUrl, '_blank').focus()
    },
    getFormattedDate (date) {
      const d = new Date(date)
      const day = d.getDate() < 10 ? `0${d.getDate()}` : d.getDate()
      const month = d.getMonth() < 10 ? `0${d.getMonth()}` : d.getMonth()
      return `${day}.${month}.${d.getFullYear()}`
    },
    getFormattedTime (date) {
      const d = new Date(date)
      const hours = d.getHours() < 10 ? `0${d.getHours()}` : d.getHours()
      const minutes = d.getMinutes() < 10 ? `0${d.getMinutes()}` : d.getMinutes()
      return `${hours}:${minutes}`
    },
    getOfferAvailableDuration (start, end) {
      const s = new Date(start)
      const e = new Date(end)
      const diffInMinutes = Math.trunc(Math.abs(e - s) / 1000 / 60)

      const days = Math.trunc(diffInMinutes / 1440)
      const hoursAndMinutes = diffInMinutes % 1440 / 60
      const hours = Math.trunc(hoursAndMinutes)
      const minutes = Math.round(hoursAndMinutes % 1 * 60)

      return days > 0 ? `${days} dni i ${hours}h ${minutes}min` : `${hours}h ${minutes}min`
    },
    removeOffer () {
      this.removeSpottedOffer(this.offerId)
    }
  }
}
</script>

<style scoped>
.otomoto-info{
  text-align: center;
}
</style>
