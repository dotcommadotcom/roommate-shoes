<template>
  <div class="box mb-4">
    <h3 class="is-size-4 mb-6">Order #{{ order.id }}</h3>

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
        <tr
          v-for="item in order.items"
          v-bind:key="item.product.id"
        >
          <td>{{ item.product.name }}</td>
          <td>${{ item.product.price }}</td>
          <td>{{ item.quantity }}</td>
          <td>${{ getItemTotal(item).toFixed(2) }}</td>
        </tr>
      </tbody>

      <tfoot>
        <tr>
          <td colspan="2">Order Total</td>
          <td>{{ orderTotalLength }}</td>
          <td>${{ orderTotalPrice.toFixed(2) }}</td>
        </tr>
      </tfoot>
    </table>
  </div>
</template>

<script>
export default {
  name: 'OrderSummary',
  props: {
    order: Object
  }, 
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
  },
  computed: {
    orderTotalLength() {
      return this.order.items.reduce((acc, currentItem) => {
        return acc += currentItem.quantity
      }, 0)
    },
    orderTotalPrice() {
      return this.order.items.reduce((acc, currentItem) => {
        return acc += currentItem.product.price * currentItem.quantity
      }, 0)
    }
  }
}
</script>