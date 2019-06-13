<template>
	<div class="container">
		<div class="Home" v-if="products.length > 0">
			<hr>
			<h1 class="display-4" align="center" v-if="category !== ''">
				{{ category }}
			</h1>
			<h1 class="display-4" align="center" v-else>
				Products
			</h1>
			<hr>
			<div class="row">
				<div class="col" v-for="product in products">
					<a :href="`/show/${product.id}`">
						<img :src="product.resources.picture_file_url" width="280">
						<p>{{ product.name }}</p>
					</a>
					<p>{{ product.price }} zł</p>
				</div>
			</div>
		</div>
		<div v-else>
			<p>No items to display</p>
		</div>
	</div>
</template>
 
<script>
import axios from 'axios';

export default {
	name: 'products',
	data() {
		return {
			products: [],
			category: '',
		}
	},
	watch:{
		$route (){
			this.loadProducts();
		}
	}, 
	methods: {
		getAllProducts() {
			const path = 'http://localhost:5002/products';
			this.sendGetRequest(path, false);
		},
		getProductsFromCategory(categoryName) {
			const path = 'http://localhost:5002/products/' + String(categoryName);
			this.sendGetRequest(path, true);
		},
		sendGetRequest(path, wasCategorySelected) {
			axios.get(path)
			.then((res) => {
				this.products = res.data.data;
				if (wasCategorySelected) {
					this.category = this.products[0].category.name;
				} else {
					this.category = '';
				}
			})
			.catch((error) => {
				// eslint-disable-next-line
				console.error(error);
			});
		},
		loadProducts() {
			let categoryName = this.$route.params.name;
			if(typeof categoryName !== 'undefined' && categoryName.length > 0) {
				this.getProductsFromCategory(categoryName);
			} else {
				this.getAllProducts();
			}
		}
	},
	created() {
		this.loadProducts();
	},
}
</script>
