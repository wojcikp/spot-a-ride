<template>
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
    <v-spacer />
  </v-app-bar>
</template>

<script>
export default {
  name: 'UpperBar'
}
</script>

<style scoped>
.toolbar-title{
  margin-left: 20%;
}
</style>
