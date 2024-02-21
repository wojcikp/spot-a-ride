<template>
  <div>
    <upper-bar />
    <v-container class="mt-10" fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="teal darken-1">
              <v-toolbar-title
                >{{
                  isRegistered ? stateObj.login.name : stateObj.register.name
                }}
                form</v-toolbar-title
              >
            </v-toolbar>
            <v-card-text>
              <form
                ref="form"
                @submit.prevent="!isRegistered ? register() : login()"
              >
                <v-text-field
                  v-model="userName"
                  label="Login"
                  required
                ></v-text-field>

                <v-text-field
                  v-if="!isRegistered"
                  v-model="email"
                  :rules="emailRules"
                  label="E-mail"
                  required
                ></v-text-field>

                <v-text-field
                  v-model="password"
                  label="Hasło"
                  required
                ></v-text-field>

                <v-text-field
                  v-if="!isRegistered"
                  v-model="confirmPassword"
                  label="Potwierdź hasło"
                  required
                ></v-text-field>
                <div class="red--text">{{ errorMessage }}</div>
                <v-btn
                  type="submit"
                  class="mt-4"
                  color="teal darken-1"
                  dark
                  >{{
                    isRegistered ? stateObj.login.name : stateObj.register.name
                  }}</v-btn
                >
                <br>
                <v-btn
                  @click="isRegistered = !isRegistered"
                  x-small
                  color="grey lighten-2"
                  class="mt-4"
                >
                  {{ toggleMessage }}
                </v-btn>
              </form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'
import UpperBar from './UpperBar.vue'

export default {
  components: { UpperBar },
  name: 'RegisterAndLogin',

  data () {
    return {
      email: null,
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      userName: null,
      password: null,
      confirmPassword: null,
      isRegistered: true,
      errorMessage: null,
      stateObj: {
        register: {
          name: 'Register',
          message: 'Masz już konto? Zaloguj się.'
        },
        login: {
          name: 'Login',
          message: 'Nie masz konta? Zarejestruj się.'
        }
      }
    }
  },

  methods: {
    ...mapActions([
      'createAccount',
      'getAuthToken',
      'getUserId',
      'getSearchedOffers',
      'getSpottedOffers'
    ]),
    ...mapMutations([
      'setAuthToken',
      'setUserId'
    ]),
    async login () {
      const authToken = await this.getAuthToken({ username: this.userName, password: this.password })
      this.setAuthToken(authToken)
      const userId = await this.getUserId(authToken)
      this.setUserId(userId)
      if (authToken && userId) {
        await this.getSearchedOffers()
        await this.getSpottedOffers()
        this.$router.push('/')
      } else {
        this.errorMessage = 'Złe dane logowania.'
      }
    },
    async register () {
      if (this.password === this.confirmPassword) {
        this.errorMessage = null
        const res = await this.createAccount({ username: this.userName, email: this.email, password: this.password })
        if (res.status) {
          if (res.status >= 400 && res.status < 500) {
            this.errorMessage = res.data
          } else {
            this.isRegistered = true
            this.email = null
            this.userName = null
            this.password = null
          }
        }
      } else {
        this.errorMessage = 'Złe dane logowania.'
      }
    }
  },

  computed: {
    toggleMessage () {
      return this.isRegistered
        ? this.stateObj.login.message
        : this.stateObj.register.message
    }
  }
}
</script>
