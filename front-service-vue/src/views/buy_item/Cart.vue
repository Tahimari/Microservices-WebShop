<template>
    <div class="container">
        <div v-if="token">
            <div v-if="products.length > 0">
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
                                <td> {{ fixFloat(product.price_per_one) }} </td>
                                <td> {{ product.quantity }} </td>
                                <td> {{ fixFloat(product.total_price) }} </td>
                                <td>
                                    <b-button variant="danger" v-b-modal.delete-product-dialog
                                            v-on:click="selectProduct(product)"> Delete </b-button>
                                </td>
                            </tr>
                    </tbody>
                </table>
                <h4 align="right" class="display-5"> Total: {{ fixFloat(total_price) }} PLN</h4>
            </div>
            <b-jumbotron v-else>
                <h2 align="center" class="display-3"> Empty cart </h2>
            </b-jumbotron>  
            <div class="modal-footer">
                <b-button variant="info" to="/"> Back to shop </b-button>
                <div v-if="products.length > 0">
                    <b-button variant="success" to="/delivery"> Delivery </b-button>
                </div>   
            </div>
            <!-- Delete Product -->
            <b-modal id="delete-product-dialog" hide-footer>
                <p> Are sure do you want to delete "{{ selectedProduct.name }}"? </p>
                <div class="modal-footer">
                    <b-button variant="success" @click="hideModal('delete-product-dialog')">No</b-button>
                    <b-button variant="danger" @click="deleteProduct();hideModal('delete-product-dialog');">Yes</b-button>
                </div>
            </b-modal>
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
            order_id: 0,
            order_items: {},
            products: [],
            total_price: 0.0,
            selectedProduct: {
                id: 0,
                name: ''
            },
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
        hideModal(modalID) {
            this.$bvModal.hide(modalID);
        },
		getOrderedProducts() {
            this.total_price = 0.0;
            const path = `${process.env.VUE_APP_ORDERS_SERVICE_URL}/orders/pending`;
            axios.get(path, {
                params: {
                    token: this.token
                }
            })
            .then((res) => {
                this.order_id = res.data.data.order_id;
                this.order_items = res.data.data.order_items;
                this.prepareProductList(this.order_items);
			})
			.catch((error) => {
                if (error.response) {
                    if (error.response.status === 404) {
                        this.order_id =  0;
                        this.order_items = {};
                        this.products = [];
                        this.total_price = 0.0;
                        this.selectedProduct = {
                            id: 0,
                            name: ''
                        };
                        return;
                    }
                }
				console.error(error);
			});
        },
        deleteProduct() {
            let orderID = this.order_id;
            let productID = this.selectedProduct.id;
            const path = `${process.env.VUE_APP_ORDERS_SERVICE_URL}/orders/${orderID}/${productID}`;
            axios.delete(path, {
                data: {
                    token: this.token
                }
            })
            .then(() => {
                this.getOrderedProducts();
                this.$forceUpdate();
            })
            .catch((error) => {
				console.error(error);
			});
        },
        selectProduct(product) {
            this.selectedProduct.id = product.id;
            this.selectedProduct.name = product.name;
        },
        fixFloat(number) {
            return Number.parseFloat(number).toFixed(2);
        },
        prepareProductList(order_items) {
            this.products = [];
            
            for (var i = 0; i < order_items.length; i++) {
                let tempItem = order_items[i];
                let tempProduct = {
                    id: 0,
                    name: '',
                    category_name: '',
                    quantity: 0,
                    price_per_one: 0.0,
                    total_price: 0.0
                };
                tempProduct.quantity = tempItem.quantity;
                let productID = tempItem.product_id;
                tempProduct.id = productID;
                const path = `${process.env.VUE_APP_PRODUCTS_SERVICE_URL}/products/${productID}`;
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