<template>
  <div>
    <upper-bar />
    <main-menu v-if="this.userId && this.authToken" />

    <v-card
      class="mx-auto mt-12"
      max-width="400"
    >
      <v-img
        class="white--text align-end"
        height="200px"
        src="../assets/alfa.jpg"
      >
        <v-card-title>O aplikacji</v-card-title>
      </v-img>

      <v-card-text class="text--primary">
        <div>
          Dzięki Spot a ride możesz w jednym miejscu śledzić oferty z otomoto.
          Aplikacja śledzi interesujące Cię marki i modele w podanym zakresie lat produkcji, przebiegu i ceny.
          Z czasem działania zobaczysz pojawiające się oferty,
          które mogą Cię zainteresować oraz po jakim czasie oferty na dane samochody zniknęły
          i jaka była ostateczna cena w momencie wygaśnięcia oferty.
        </div>
      </v-card-text>

      <v-card-actions>
        <v-btn
          v-if="!this.userId && !this.authToken"
          @click="$router.push('/register-and-login')"
          color="teal darken-1"
          text
        >
          Zaloguj się
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import MainMenu from './MainMenu.vue'
import UpperBar from './UpperBar.vue'

export default {
  components: { MainMenu, UpperBar },
  name: 'AboutPage',

  computed: {
    ...mapGetters([
      'authToken',
      'userId'
    ])
  }
}
</script>

<style>
</style>
