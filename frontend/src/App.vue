<template>
  <v-app id="spot-a-ride">
    <v-main>
      <upper-bar />
      <main-menu v-if="this.userId && this.authToken" />
      <v-progress-linear v-if="this.showProgressBar" class="spin" indeterminate color="teal" height="8" />
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'
import MainMenu from './components/MainMenu.vue'
import UpperBar from './components/UpperBar.vue'

export default {
  name: 'App',
  components: { MainMenu, UpperBar },

  computed: {
    ...mapGetters([
      'userId',
      'authToken',
      'showProgressBar'
    ])
  }
}
</script>
