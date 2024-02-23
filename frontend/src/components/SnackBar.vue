<template>
  <v-snackbar v-model="show" color="red" timeout="3000" outlined shaped>
    Coś poszło źle. Spróbuj ponownie.
      <v-btn color="blue" text @click="show = false">Ok</v-btn>
  </v-snackbar>
</template>

<script>

export default {
  computed: {
    show: {
      get () {
        return this.$store.state.showSnackBar
      },
      set (value) {
        this.$store.commit('setShowSnackBar', value)
      }
    }
  }
}
</script>
