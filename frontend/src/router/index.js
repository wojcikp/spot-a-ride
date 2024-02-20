import Vue from 'vue'
import VueRouter from 'vue-router'
import RegisterAndLogin from '../components/RegisterAndLogin.vue'
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
  {
    path: '/register-and-login',
    name: 'register-and-login',
    component: RegisterAndLogin
  },
  }
]

const router = new VueRouter({
  routes
})

export default router
