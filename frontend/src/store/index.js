import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
axios.defaults.baseURL = process.env.VUE_APP_API_URL

export default new Vuex.Store({
  state: {
    authToken: null,
    userId: null,
    searchedOffers: [],
    spottedOffers: []
  },
  getters: {
    authToken: state => { return state.authToken },
    userId: state => { return state.userId },
    searchedOffers: state => { return state.searchedOffers },
    spottedOffers: state => { return state.spottedOffers }
  },
  mutations: {
    setAuthToken (state, payload) {
      state.authToken = payload
    },
    setUserId (state, payload) {
      state.userId = payload
    },
    setSearchedOffers (state, payload) {
      state.searchedOffers = payload
    },
    setSpottedOffers (state, payload) {
      state.spottedOffers = payload
    }
  },
  actions: {
    createAccount ({ commit }, { username, password }) {
      axios.post('/api/users/', {
        username: username,
        password: password
      })
        .catch(err => {
          console.error(err)
        })
    },

    getAuthToken ({ commit }, { username, password }) {
      axios.post('/api-token-auth/', {
        username: username,
        password: password
      })
        .then(response => response.data)
        .then(data => {
          commit('setAuthToken', data.token)
        })
        .catch(err => {
          console.error(err)
        })
    },

    getUserId ({ commit, state }) {
      axios.get('/user-id/', {
        headers: {
          Authorization: `Token ${state.authToken}`
        }
      })
        .then(response => response.data)
        .then(data => {
          commit('setUserId', data.userId)
        })
        .catch(err => {
          console.error(err)
        })
    },

    getSearchedOffers ({ commit, state }) {
      axios.get('/api/searched-offers/', {
        headers: {
          Authorization: `Token ${state.authToken}`
        }
      })
        .then(response => response.data)
        .then(data => {
          commit('setSearchedOffers', data)
        })
        .catch(err => {
          console.error(err)
        })
    },

    addSearchedOffer ({ commit, state },
      {
        brand,
        model,
        productionYearFrom,
        productionYearTo,
        mileageLimit,
        priceLimit
      }) {
      axios.post('/api/searched-offers/', {
        user: state.userId,
        brand: brand,
        model: model,
        production_year_from: productionYearFrom,
        production_year_to: productionYearTo,
        mileage_limit: mileageLimit,
        price_limit: priceLimit
      }, {
        headers: {
          Authorization: `Token ${state.authToken}`
        }
      })
        .then(response => response.data)
        .then(data => {
          commit('setSearchedOffers', data)
        })
        .catch(err => {
          console.error(err)
        })
    },

    getSpottedOffers ({ commit, state }) {
      axios.get('/api/spotted-offers/', {
        headers: {
          Authorization: `Token ${state.authToken}`
        }
      })
        .then(response => response.data)
        .then(data => {
          commit('setSpottedOffers', data)
        })
        .catch(err => {
          console.error(err)
        })
    },

    removeSpottedOffer ({ commit, state }, offerId) {
      axios.delete(`/api/spotted-offers/${offerId}/`, {
        headers: {
          Authorization: `Token ${state.authToken}`
        }
      })
        .then(response => response.data)
        .then(data => {
          console.log(data)
          const offers = state.spottedOffers.filter(offer => {
            return offer.id !== offerId
          })
          commit('setSpottedOffers', offers)
        })
        .catch(err => {
          console.error(err)
        })
    }
  }
})
