import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Account from '../views/Account.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUp
  },
  {
    path: '/login',
    name: 'login',
    component: LogIn
  },
  {
    path: '/account',
    name: 'account',
    component: Account,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: Product
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin && !store.state.isAuthenticated)) {
    next({name: 'LogIn', query: { to: to.path }})
  } else {
    next()
  }
})

export default router
