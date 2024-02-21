<template>
  <v-navigation-drawer app clipped>
    <v-list>
      <v-list-item
        v-for="item in this.items"
        :key="item.title"
        :class="{ activeMenuItem: $router.currentRoute.path === item.path }"
        :to="item.path"
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
        { title: 'Znalezione oferty', path: '/', icon: 'mdi-car-hatchback', action: () => {} },
        { title: 'Szukaj ofert', path: '/add-searched-offer', icon: 'mdi-car-search', action: () => {} },
        { title: 'O aplikacji', path: '/about', icon: 'mdi-help-box', action: () => {} },
        { title: 'Wyloguj', path: null, icon: 'mdi-logout', action: () => { this.logOut() } }
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

<style scoped>
.activeMenuItem::before {
  background-color: #00897b;
  border-radius: 5px;
  margin-left: 5px;
  margin-right: 5px;
}
</style>
