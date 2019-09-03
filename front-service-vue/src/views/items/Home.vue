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
				<div class="col-sm-6 col-md-4" v-for="product in products">
					<a :href="`/show/${product.id}`">
						<img class="img-fluid" :src="product.resources.picture_file_url" >
						<p>{{ product.name }}</p>
					</a>
					<p>{{ product.price }} zł</p>	
				</div>
			</div>


			<div>
				<b-pagination size="md" align="center" :total-rows="numberOfItems" v-model="currentPage" :per-page="itemsPerPage" @input="loadProducts()">
        		</b-pagination>
        		<p class="mt-3" align="center">Current Page: {{ currentPage }}</p>
			</div>
        	

		</div>
		<div v-else>
			<h2 align="center" class="display-3" style="margin-top: 25px;"> No items to display! </h2>
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
	      	currentPage: 1,
	      	numberOfItems: 0,
	      	itemsPerPage: 0,
	      	paginate: 'a',	
	      	queryStringTemp: '',	
	      }
	},
	watch:{
		$route (){
			this.currentPage = 1;
			this.loadProducts();
		}
	}, 
	methods: {
		getAllProducts(currentPage) {
			const path = `${process.env.VUE_APP_PRODUCTS_SERVICE_URL}/products?page=` + this.currentPage;
			this.sendGetRequest(path, false);
			window.scrollTo({
			  top: 0,
			  behavior: 'smooth',
			}) 
		},
		getProductsFromCategory(categoryName) {
			const path = `${process.env.VUE_APP_PRODUCTS_SERVICE_URL}/products/${categoryName}?page=` + this.currentPage;
			this.sendGetRequest(path, true);
		},
		getProductsFilteredByQuery(queryString, currentPage) {
			queryString = queryString.toLowerCase();
			if(this.$route.query.search)
				this.queryStringTemp = this.$route.query.search
			
			const path = `${process.env.VUE_APP_PRODUCTS_SERVICE_URL}/products?&query=${encodeURI(this.queryStringTemp)}&paginate=${encodeURI(this.paginate)}&page=` +this.currentPage;
			axios.get(path)
			.then((res) => {
				let tempInputProducts = res.data.data;
				let tempOutputProducts = [];

				for (var i = 0; i < tempInputProducts.length; i++) {
					let product = tempInputProducts[i];
					let productName = product.name.toLowerCase();
					if (productName.includes(queryString)) {
						tempOutputProducts.push(product);
					}
				}
				this.products = tempOutputProducts;
				this.category = '';
				this.numberOfItems= res.data.allItemsQuantity;
                this.itemsPerPage = res.data.numberOfItemsPerPage;
			})
			.catch((error) => {
				// eslint-disable-next-line
				console.error(error);
			});
		},
		sendGetRequest(path, wasCategorySelected) {
			axios.get(path)
			.then((res) => {
				this.products = res.data.data;
				this.numberOfItems= res.data.allItemsQuantity;
                this.itemsPerPage = res.data.numberOfItemsPerPage;
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
			} else if (this.$route.query.search) {
				let queryString = this.$route.query.search;
				if(this.$route.query.search)
					this.getProductsFilteredByQuery(queryString);
				else
					this.getProductsFilteredByQuery(queryStringTemp);
			} else {
				this.getAllProducts();
			}
		},
	},
	created() {
		this.loadProducts();
	},
}
</script>
