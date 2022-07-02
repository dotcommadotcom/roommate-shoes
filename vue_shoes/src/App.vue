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
        <div class="navbar-end">
          <router-link to="/adidas" class="navbar-item">Adidas</router-link>
          <router-link to="/nike" class="navbar-item">Nike</router-link>
          
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-dark">Log in</router-link>
              <router-link to="/cart" class="button is-dark">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>{{ cartTotalLength }}</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer has-background-white">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mobileMenuVisible: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },  
  methods: {
    toggleMobileMenu() {
      this.mobileMenuVisible = !this.mobileMenuVisible
    }
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      // this.cart.items.forEach(function addQuantity(item) {
      //   totalLength += item.quantity
      // })

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
