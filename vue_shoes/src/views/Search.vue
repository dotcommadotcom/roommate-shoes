<template>
  <div class="page-category">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Search</h1>

        <h2 class="is-size-5 has-text-crey">Search term: "{{ query }}"</h2>
      </div>

      <ProductBox
        v-for="product in products"
        v-bind:key="product.id"
        v-bind:product="product" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import ProductBox from '@/components/ProductBox.vue'

export default {
  name: 'Search',
  data() {
    return {
      products: [],
      query: ''
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getSearch()
  },
  methods: {
    getSearch() {
      let uri = window.location.search.substring(1)
      let params = new URLSearchParams(uri)

      if (params.get('query')) {
        this.query = params.get('query')

        this.performSearch()
      }
    },
    async performSearch() {
      this.$store.commit('setIsLoading', true)

      await axios.post('api/v1/products/search/', {'query': this.query })
          .then(response => {
            this.products = response.data

            document.title = this.query + ' - Search results'
          })
          .catch(error => {
            console.log(error)

            toast({
              message: 'Something went wrong. Please try again.',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })
          })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>