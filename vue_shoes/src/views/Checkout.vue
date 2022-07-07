<template>
  <div class="page-checkout">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Checkout</h1>
      </div>

      <div class="column is-12 box">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="item in cart.items" v-bind:key="item.product.id">
              <td>{{ item.product.name }}</td>
              <td>${{ item.product.price }}</td>
              <td>{{ item.quantity }}</td>
              <td>${{ getItemTotal(item).toFixed(2) }}</td>
            </tr>
          </tbody>

          <tfoot>
            <tr>
              <td colspan="2">Total</td>
              <td>{{ cartTotalLength }}</td>
              <td>${{ cartTotalPrice.toFixed(2) }}</td>
            </tr>
          </tfoot>
        </table>
      </div>

      <div class="column is-12 box">
        <h2 class="subtitle">Shipping details</h2>
        <p class="has-text-grey mb-4">All fields are required.</p>

        <div class="columns is-multiline">
          <div class="column is-6">
            <div class="field">
              <label>First name</label>
              <div class="control">
                <input type="text" class="input" v-model="first_name">
              </div>
            </div>

            <div class="field">
              <label>Email</label>
              <div class="control">
                <input type="email" class="input" v-model="email">
              </div>
            </div>
          </div>

          <div class="column is-6">
            <div class="field">
              <label>Last name</label>
              <div class="control">
                <input type="text" class="input" v-model="last_name">
              </div>
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div> 

          <div class="column is-12">
            <hr>

            <div id="card-element" class="mb-5"></div>

            <template v-if="cartTotalLength">
              <hr>

              <button class="button is-dark" @click="submitOrder">Order now!</button>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Checkout',
  data() {
    return {
      cart: {
        items: []
      },
      first_name: '',
      last_name: '',
      email: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Checkout'

    this.cart = this.$store.state.cart
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    submitOrder() {
      this.errors = []

      if (this.first_name === '') {
        this.errors.push('You forgot your first name.')
      }

      if (this.last_name === '') {
        this.errors.push('You forgot your last name.')
      }

      if (this.email === '') {
        this.errors.push('You forgot your email address.')
      }
    }
  }, 
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, currentItem) => {
        return acc += currentItem.quantity
      }, 0)
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, currentItem) => {
        return acc += currentItem.product.price * currentItem.quantity
      }, 0)
    }
  }
}
</script>