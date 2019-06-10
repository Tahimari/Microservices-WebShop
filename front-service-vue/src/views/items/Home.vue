<template>
  <div class="container">
    <div class="Home" v-if="items">
      <hr>
      <p v-if="category">
        {{ category }}
      </p>
      <p v-else>
        ITEMS
      </p>
      <hr>
      <div class="row" v-for="item in items">
        <div class="col">
          <a :href=" item.id ">
            <img :src=" item.imageUrl " width="280">
            <p>{{ item.title }}</p>
          </a>
          <p>{{ item.price }} zł</p>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No items to display</p>
    </div>
  </div>
</template>

<script>
</script>
