<template>
  <v-navigation-drawer app clipped>
    <v-list>
      <v-list-item
        v-for="item in this.items"
        :key="item.title"
        link
        @click="item.action"
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
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  name: 'MainMenu',

  data () {
    return {
      items: [
        { title: 'Znalezione oferty', icon: 'mdi-car-hatchback', action: () => { this.$router.push('/') } },
        { title: 'Szukaj ofert', icon: 'mdi-car-search', action: () => { this.$router.push('/add-searched-offer') } },
        { title: 'O aplikacji', icon: 'mdi-help-box', action: () => { this.$router.push('/about') } },
        { title: 'Wyloguj', icon: 'mdi-logout', action: this.logOut }
      ]
    }
  },

  methods: {
    ...mapMutations([
      'setAuthToken',
      'setUserId'
    ]),
    logOut () {
      this.setAuthToken(null)
      this.setUserId(null)
      this.$router.push('/register-and-login')
    }
  }
}
</script>
