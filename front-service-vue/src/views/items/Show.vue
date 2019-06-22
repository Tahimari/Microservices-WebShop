<template>
    <div class="container">
        <div v-if="Object.keys(product).length === 0">
            <p>No product to display, go back to home page</p>
        </div>
        <div v-else>
            <hr>
            <h1 class="display-4" align="center">
                {{ product.name }}
            </h1>
            <hr>
            <div class="row">
                <div class="col-md">
                    <img :src="product.resources.picture_file_url" width="500" class="img-fluid">
                </div>
                <div class="col-md">
                    <p>{{ product.name }}</p>
                    <p style="white-space: pre-line">{{ product.resources.product_description }}</p>
                    <p>Cena: {{ product.price }} zł</p>
                    <div v-if="token">
                        <b-form-group id="form-quantity-group">
                            Ile sztuk: {{ quantity }}
                            <b-form-input id="form-quantity-input" type="range" step="1" min="1" max="20"
                                          v-model="quantity">
                            </b-form-input>
                        </b-form-group>
                        <button class="btn btn-lg btn-primary btn-block"
                                id="add-to-cart" v-on:click="addProductToCart" v-b-modal.add-product-modal>Add to cart
                        </button>
                    </div>
                    <div v-if="!token">
                        <b-alert variant="warning" show> Zaloguj się, aby dodać do koszyka!</b-alert>
                    </div>
                </div>
            </div>
            <!-- Modal -->
            <b-modal id="add-product-modal" title-tag="h2" title="Notifications" hide-footer>
                <!-- Modal content -->
                <img :src="product.resources.picture_file_url" width="200">
                <p>{{ product.name }}</p>
                <p>Cena: {{ product.price }}zł</p>
                <p>Ile sztuk: {{ quantity }}</p>
                <p>Product has been added to cart.</p>
                <div class="modal-footer">
                    <b-button @click="$bvModal.hide('add-product-modal')">Back to shop</b-button>
                    <b-button variant="primary" href="/cart">Go to check-in</b-button>
                </div>
            </b-modal>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'show-product',
        data() {
            return {
                product: {},
                quantity: 1,
                token: ''
            }
        },
        mounted() {
            if (localStorage.token) {
                this.token = localStorage.token;
            }
        },
        watch: {
            $route() {
                this.loadProduct();
                if (localStorage.token) {
                    this.token = localStorage.token;
                } else {
                    this.token = '';
                }
            }
        },
        methods: {
            getProduct(productID) {
                const path = 'http://localhost:5002/products/' + String(productID);
                axios.get(path)
                    .then((res) => {
                        this.product = res.data.data;
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            },
            loadProduct() {
                let productID = this.$route.params.product_id;
                this.getProduct(productID);
            },
            addProductToCart() {
                const path = 'http://localhost:5003/orders';
                const payload = {
                    token: this.token,
                    product_id: this.product.id,
                    quantity: this.quantity
                }
                axios.post(path, payload)
                    .catch((error) => {
                        console.error(error);
                    });
            }
        },
        created() {
            this.loadProduct();
        },
    }
</script>

