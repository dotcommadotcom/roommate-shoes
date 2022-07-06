<template>
  <div class="page-signup">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Log in</h1>

        <form @submit.prevent="submitLogin">
          <div class="field">
            <label>Username</label>
            <div class="control">
              <input type="text" class="input" v-model="username">
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password">
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div> 

          <div class="field">
            <div class="control">
              <button class="button is-dark">Log in</button>
            </div>
          </div>

          <hr>

          Or <router-link to="/signup">click here</router-link> to sign up.
        </form>
      </div>
    </div>

  </div>
  
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  }, 
  mounted() {
    document.title = 'Log in'
  },
  methods: {
    async submitLogin() {
      axios.defaults.headers.common['Authorization'] = ""
      localStorage.removeItem("token")

      const userData = {
        username: this.username,
        password: this.password
      }

      axios.post("/api/v1/token/login/", userData)
          .then(response => {
            const token = response.data.auth_token

            this.$store.commit('setToken', token)
            axios.defaults.headers.common['Authorization'] = "Token " + token
            localStorage.setItem("token", token)

            this.$router.push(this.$route.query.to || '/cart')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push('Something went wrong. Please try again.')
              
              console.log(JSON.stringify(error))
            }
          })
    }
  }
}
</script>