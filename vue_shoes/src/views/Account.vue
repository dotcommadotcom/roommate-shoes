<template>
  <div class="page-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Account</h1>
      </div>

      <div class="column is-12">
        <button v-on:click="logout()" class="button is-danger">Log out</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Account',
  mounted() {
    document.title = 'Account'
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
    }
  },
}
</script>