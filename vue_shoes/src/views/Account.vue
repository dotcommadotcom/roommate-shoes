<template>
  <div class="page-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Account</h1>
      </div>

      <div class="column is-12">
        <button v-on:click="logout()" class="button is-danger">Log out</button>
      </div>

      <hr>

      <div class="column is-12">
        <h2 class="subtitle">My orders</h2>

        <OrderSummary
          v-for="order in orders"
          v-bind:key="order.id"
          v-bind:order="order"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import OrderSummary from '@/components/OrderSummary.vue'

export default {
  name: 'Account',
  data() {
    return {
      orders: []
    }
  },
  mounted() {
    document.title = 'Account'

    this.getOrders()
  },
  components: {
    OrderSummary
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")

      this.$store.commit('removeToken')

      this.$router.push('/')

      this.$router.push("/")
        .then(() => {
          console.log('Updated route', this.$route)
        })
    },
    async getOrders() {
      this.$store.commit('setIsLoading', true)

      await axios.get('api/v1/orders')
                .then(response => {
                  this.orders = response.data
                })
                .catch(error => {
                  console.log(error)
                })
      this.$store.commit('setIsLoading', false)
    }
  },
}
</script>