<template>
  <div id="wrapper">
    <nav class="navbar is-transparent">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item is-size-4 is-italic"><strong>Help me sell my roommate's shoes</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="toggleMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': mobileMenuVisible}">
        <div class="navbar-start">

          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="What are you looking for?" name="query">
                </div>

                <div class="control">
                  <button to="/search" class="button is-dark">
                    <span class="icon"><i class="fas fa-search"></i></span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        
        <div class="navbar-end">
          <router-link to="/adidas" class="navbar-item">Adidas</router-link>
          <router-link to="/nike" class="navbar-item">Nike</router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/account" class="button is-dark">My Account</router-link>
              </template>

              <template v-else>
                <router-link to="/login" class="button is-dark">Log in</router-link>
              </template>

              <router-link to="/cart" class="button is-dark">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>{{ cartTotalLength }}</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': this.$store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer has-background-white">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      mobileMenuVisible: false,
      cart: {
        items: []
      },
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  methods: {
    toggleMobileMenu() {
      this.mobileMenuVisible = !this.mobileMenuVisible
    },
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, currentItem) => {
        return acc += currentItem.quantity
      }, 0)
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
