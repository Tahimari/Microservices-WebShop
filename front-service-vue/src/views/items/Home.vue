<template>
	<div class="Home" v-if="products.length > 0">
		<hr>
		<p v-if="category !== ''">
			{{ category }}
		</p>
		<p v-else>
			ITEMS
		</p>
		<hr>
		<div class="row" v-for="product in products">
			<div class="col">
				<a :href=" product.id ">
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
</template>
 
<script>
import axios from 'axios';

export default {
	name: 'products',
	data() {
		return {
			products: [],
			category: '',
			message: '',
			showMessage: false,
		}
	},
	watch:{
		$route (to, from){
			this.loadProducts();
		}
	}, 
	methods: {
		getAllProducts() {
			const path = 'http://localhost:5002/products';
			this.sendGetRequest(path);
			this.category = ''
		},
		getProductsFromCategory(categoryID) {
			const path = 'http://localhost:5002/products/' + String(categoryID);
			this.sendGetRequest(path);
			this.category = this.products[0].category.name
		},
		sendGetRequest(path) {
			axios.get(path)
			.then((res) => {
				this.products = res.data.data;
			})
			.catch((error) => {
				// eslint-disable-next-line
				console.error(error);
			});
		},
		loadProducts() {
			let category_id = this.$route.params.id;
			if(!isNaN(category_id)){
				this.getProductsFromCategory(category_id);
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
