<template>
    <div class="container">
        <div v-if="token">
            <div v-if="products">
                <h3 align="center" class="display-4"> Cart </h3>
                <table class="table">
                    <thead>
                        <tr>
                            <th> No. </th>
                            <th> Name </th>
                            <th> Category </th>
                            <th> Price per one </th>
                            <th> Quantity </th>
                            <th> Price </th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                            <tr v-for="(product, index) in products">
                                <td> {{ index + 1 }} </td>
                                <td> {{ product.name }} </td>
                                <td> {{ product.category_name }} </td>
                                <td> {{ product.price_per_one }} </td>
                                <td> {{ product.quantity }} </td>
                                <td> {{ product.total_price }} </td>
                                <td>
                                    <b-button variant="danger" > Delete </b-button>
                                </td>
                            </tr>
                    </tbody>
                </table>
                <h4 align="right" class="display-5"> Total: {{ total_price }} zł</h4>
            </div>
            <b-jumbotron v-else>
                <h2 align="center" class="display-3"> Empty cart </h2>
            </b-jumbotron>  
            <div class="modal-footer">
                <b-button variant="info" to="/"> Back to shop </b-button>
                <div v-if="products">
                    <b-button variant="success" to="/delivery"> Delivery </b-button>
                </div>   
            </div>
        </div>
        <div v-else>
            <b-jumbotron>
                <h2 align="center" class="display-3"> Please log in to use from cart! </h2>
            </b-jumbotron> 
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
            order_items: {},
            products: '',
            total_price: 0.0,
            token: ''
		}
    },
    mounted() {
        if (localStorage.token) {
            this.token = localStorage.token;
            this.getOrderedProducts();
        }
    },
	watch:{
		$route (to, from){
            if (localStorage.token) {
                this.token = localStorage.token;
                this.getOrderedProducts();
            } else {
                this.token = '';
            }
		}
	}, 
	methods: {
		getOrderedProducts() {
            const path = 'http://localhost:5003/orders/pending';
            const payload = {
                token: this.token
            };
            axios.get(path, {
                params: {
                    token: this.token
                }
            })
            .then((res) => {
                this.order_items = res.data.data.order_items;
                this.prepareProductList(this.order_items);
			})
			.catch((error) => {
				console.error(error);
			});
        },
        prepareProductList(order_items) {
            this.products = [];
            
            for (var i = 0; i < order_items.length; i++) {
                let tempItem = order_items[i];
                let tempProduct = {
                    name: '',
                    category_name: '',
                    quantity: 0,
                    price_per_one: 0.0,
                    total_price: 0.0
                };
                tempProduct.quantity = tempItem.quantity;

                let productID = tempItem.product_id;
                
                const path = 'http://localhost:5002/products/' + String(productID);
                axios.get(path)
                .then((res) => {
                    let responseData = res.data.data;
                    tempProduct.name = responseData.name;
                    tempProduct.category_name = responseData.category.name;
                    tempProduct.price_per_one = responseData.price;
                    tempProduct.total_price = tempProduct.quantity * tempProduct.price_per_one;
                    this.products.push(tempProduct);
                    this.total_price += tempProduct.total_price;
                })
                .catch((error) => {
                    console.error(error);
                });
            }
        }
	}
}
</script>