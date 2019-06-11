<template>
    <div class="container">
        <a href="{{}}" class="btn btn-primary pull-right">
            Create <span class="fa fa-plus-circle"></span>
        </a>
        <h1>All Products</h1>

        <table class="table">
            <thead>
                <tr>
                    <th>Title</th>
                    <th class="d-none d-md-table-cell">Description</th>
                    <th>Category</th>
                    <th>Price</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                    <tr v-for="product in products">
                        <td>{{ product.name }}</td>
                        <td class="d-none d-md-table-cell" style="white-space: pre-line">{{ product.resources.product_description }}</td>
                        <td>{{ product.category.name }}</td>
                        <td>{{ product.price }}</td>
                        <td>
                            <b-button variant="warning" > Edit </b-button>
                        </td>
                        <td>
                            <b-button variant="danger" v-b-modal.delete-product-dialog v-on:click="selectProduct(product)"> Delete </b-button>
                        </td>
                    </tr>
            </tbody>
        </table>
        <b-modal id="delete-product-dialog" hide-footer>
            <!-- Modal content -->
            <p> Are sure do you want to delete "{{ productToDelete.name }}"? </p>
            <div class="modal-footer">
                <b-button variant="success" @click="hideModal">No</b-button>
                <b-button variant="danger" @click="deleteProduct();hideModal();">Yes</b-button>
            </div>
        </b-modal> 
    </div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'products',
	data() {
		return {
            products: [],
            productToDelete: {},
		}
	},
	methods: {
		getAllProducts() {
			const path = 'http://localhost:5002/products';
			axios.get(path)
			.then((res) => {
				this.products = res.data.data;
			})
			.catch((error) => {
				console.error(error);
			});
        },
        selectProduct(product) {
            this.productToDelete = product;
        },
        hideModal() {
            this.$bvModal.hide("delete-product-dialog")
        },
        deleteProduct() {
            let product_id = this.productToDelete.id;
            const path = 'http://localhost:5002/products/' + String(product_id);
            axios.delete(path)
            .then((res) => {
                this.products = this.products.filter(obj => obj.id !== product_id);
                this.productToDelete = {};
            })
            .catch((error) => {
				console.error(error);
			});
        }
	},
	created() {
		this.getAllProducts();
    }
}
</script>