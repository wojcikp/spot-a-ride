import Vue from 'vue'
import VueRouter from 'vue-router'
import NewSearchForm from '../components/NewSearchForm.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
  {
    path: '/add-searched-offer',
    name: 'add-searched-offer',
    component: NewSearchForm,
    meta: { requiresAuth: true }
  },
  }
]

const router = new VueRouter({
  routes
})

export default router
