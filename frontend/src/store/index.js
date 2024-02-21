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
    createAccount ({ commit }, { username, email, password }) {
      return axios.post('/api/users/', {
        username: username,
        email: email,
        password: password
      })
        .catch(err => {
          console.error(err)
          return err.response
        })
    },

    getAuthToken ({ commit }, { username, password }) {
      return axios.post('/api-token-auth/', {
        username: username,
        password: password
      })
        .then(response => response.data)
        .then(data => {
          return data.token
        })
        .catch(err => {
          console.error(err)
        })
    },

    getUserId ({ commit, state }, authToken) {
      return axios.get('/user-id/', {
        headers: {
          Authorization: `Token ${authToken}`
        }
      })
        .then(response => response.data)
        .then(data => {
          return data.userId
        })
        .catch(err => {
          return err
        })
    },

    getSearchedOffers ({ commit, state }) {
      return axios.get('/api/searched-offers/', {
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
      return axios.post('/api/searched-offers/', {
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
      return axios.get('/api/spotted-offers/', {
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
