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
                    <p>{{ product.price }} zł</p>
                    <button class="btn btn-lg btn-primary btn-block"
                            id="add-to-cart" v-on:click="addProductToCart" v-b-modal.add-product-modal>Add to cart</button>
                </div>
            </div>
            <!-- Modal -->
            <b-modal id="add-product-modal" title-tag="h2" title="Notifications" hide-footer>
                    <!-- Modal content -->
                <img :src="product.resources.picture_file_url" width="200">
                <p>{{ product.name }}</p>
                <p>{{ product.price }} zł</p>
                <p>Product has been added to cart.</p>
                <div class="modal-footer">
                    <b-button variant="info" href="/"> Back to shop</b-button>
                    <b-button variant="primary" href="buy/details"> Go to check-in </b-button>
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
		}
	},
	watch:{
		$route (to, from){
			this.loadProduct();
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
				// eslint-disable-next-line
				console.error(error);
			});
        },
        loadProduct() {
            let productID = this.$route.params.product_id;
            this.getProduct(productID);
        },
        addProductToCart() {
            alert("TODO -> Dorobić funkcję dodawania produktów do koszyka! (potrzebne są tokeny)");
        }
	},
	created() {
		this.loadProduct();
	},
}

 
 /*
 {
            "category": {
                "id": 1,
                "name": "Shoes"
            },
            "id": 2,
            "name": "Redblock Ventylator Athletic M49267",
            "price": 99,
            "resources": {
                "picture_file_url": "https://b.allegroimg.com/s1440/03c560/8f70e73140cf8735769626b783ab",
                "product_description": "\n\tObuwie dla każdej osoby, która chce poczuć się modnie i wygodnie.\n\tSeria Ventilator charakteryzuje się rewelacyjnym systemem wentylacji, dzięki czemu stopa pozostaje w świeżości przez długi okres czasu.\n\tCholewka została wykonana z elementów naturalnej skóry zamszowej oraz siatki, która dodatkowo poprawia wentylację.\n\t"
            }
        }
 */


 </script>

