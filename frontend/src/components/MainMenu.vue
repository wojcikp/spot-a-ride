<template>
  <v-navigation-drawer app clipped>
    <v-list>
      <v-list-item
        v-for="item in this.items"
        :key="item.title"
        link
        @click="$router.push(item.path)"
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
export default {
  name: 'MainMenu',

  data () {
    return {
      items: [
        { title: 'Spotted offers', icon: 'mdi-view-dashboard', path: '/' },
        { title: 'Add offer', icon: 'mdi-image', path: '/add-searched-offer' },
        { title: 'About', icon: 'mdi-help-box', path: '/about' }
      ]
    }
  }
}
</script>
