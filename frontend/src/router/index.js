import Vue from 'vue'
import VueRouter from 'vue-router'
import RegisterAndLogin from '../components/RegisterAndLogin.vue'
import MainPage from '../components/Main.vue'
import NewSearchForm from '../components/NewSearchForm.vue'
import AboutPage from '../components/AboutPage.vue'
import store from '../store'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainPage,
    meta: { requiresAuth: true }
  },
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
  {
    path: '/about',
    name: 'about',
    component: AboutPage
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    const token = store.state.authToken
    if (token) {
      next()
    } else {
      next('/register-and-login')
    }
  } else {
    next()
  }
})

export default router
