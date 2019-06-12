<template>
    <div class="container">
        <a href="{{}}" class="btn btn-primary pull-right">
            Create <span class="fa fa-plus-circle"></span>
        </a>
        <h1>All Products</h1> 

        <table class="table">
            <thead>
                <tr>
                    <th>Name</th>
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
                            <b-button variant="warning" v-b-modal.edit-product-dialog v-on:click="select(product)"> Edit </b-button>
                        </td>
                        <td>
                            <b-button variant="danger" v-b-modal.delete-product-dialog v-on:click="select(product)"> Delete </b-button>
                        </td>
                    </tr>
            </tbody>
        </table>
        <b-modal id="delete-product-dialog" hide-footer>
            <p> Are sure do you want to delete "{{ selectedProduct.name }}"? </p>
            <div class="modal-footer">
                <b-button variant="success" @click="hideModal('delete-product-dialog')">No</b-button>
                <b-button variant="danger" @click="deleteProduct();hideModal('delete-product-dialog');">Yes</b-button>
            </div>
        </b-modal>
        <b-modal id="edit-product-dialog" title-tag="h2" title="Edit product" hide-footer>
            <b-form @submit="onSubmit" @reset="hideModal('edit-product-dialog')" class="w-100">
                <!-- Product name -->
				<b-form-group id="form-name-group" label="Name:" label-for="form-name-input">
					<b-form-input id="form-name-input" type="text" v-model="selectedProduct.name" required autofocus placeholder="Enter product name">		
                    </b-form-input>
				</b-form-group>
                <!-- Product price -->
				<b-form-group id="form-price-group" label="Price:" label-for="form-price-input">
					<b-form-input id="form-price-input" type="number" step="0.01" min="0" v-model="selectedProduct.price" required autofocus placeholder="Enter product price">		
                    </b-form-input>
				</b-form-group>
                <!-- Product picture URL -->
				<b-form-group id="form-picture-url-group" label="Picture URL:" label-for="form-picture-url-input">
					<b-form-input id="form-picture-url-input" type="url" v-model="selectedProduct.picture_file_url" required autofocus placeholder="Enter picture URL">		
                    </b-form-input>
				</b-form-group>
                <!-- Product description -->
				<b-form-group id="form-description-group" label="Product description:" label-for="form-description-input">
					<b-form-textarea oninput='this.style.height = ""; this.style.height = this.scrollHeight + "px"'
                    spellcheck="false"
                    id="form-description-input" v-model="selectedProduct.description" required autofocus placeholder="Product description" rows="12">
					</b-form-textarea>
				</b-form-group>
                <!-- Buttons -->
                <div class="modal-footer">
                    <b-button type="reset" variant="danger"> Cancel </b-button>
                    <b-button type="submit" variant="success"> Edit </b-button>
                </div>
            </b-form>
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
            selectedProduct: {
                id: 0,
                name: '',
                price: 0.0,
                picture_file_url: '',
                description: '',
            },
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
        select(product) {
            this.selectedProduct.id = product.id;
            this.selectedProduct.name = product.name;
            this.selectedProduct.price = product.price;
            this.selectedProduct.picture_file_url = product.resources.picture_file_url;
            this.selectedProduct.description = product.resources.product_description;
        },
        hideModal(modalID) {
            this.$bvModal.hide(modalID);
        },
        deleteProduct() {
            let product_id = this.selectedProduct.id;
            const path = 'http://localhost:5002/products/' + String(product_id);
            axios.delete(path)
            .then((res) => {
                this.products = this.products.filter(obj => obj.id !== product_id);
                this.selectedProduct = {};
            })
            .catch((error) => {
				console.error(error);
			});
        },
        editProduct() {
            console.log("Product edited!")
        },
        onSubmit(evt) {
            alert("Product edited!");
        },
	},
	created() {
		this.getAllProducts();
    }
}

/*
{
    "name": "KURTKA MĘSKA T-01",
    "price": 109.99,
    "picture_file_url": "https://e.allegroimg.com/s1024/01777a/2c22bc874e4185ad344c0d8d4c0e",
    "product_description": "\n\tNowa, oryginalnie zapakowana z kompletem metek.\n\tWykonana z wysokiej jakości matreriałów\n\tProsta kurtka z zapięciem na zamek błyskawiczny.\n\tPosiada dwie kieszenie boczne\n\tW środku wykończona jest materiałową podszewką.\n\tAbsolutny bestseller tego sezonu.\n\t"
}
*/
</script>