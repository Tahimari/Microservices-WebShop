<template>
    <div class="container">
        <h1 style="margin-top: 20px;">
            All Products
            <b-button variant="info" v-b-modal.add-product-dialog class="float-right"> Create New</b-button>
        </h1>
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
                <td class="d-none d-md-table-cell" style="white-space: pre-line">{{
                    product.resources.product_description }}
                </td>
                <td>{{ product.category.name }}</td>
                <td>{{ product.price }}</td>
                <td>
                    <b-button variant="warning" v-b-modal.edit-product-dialog v-on:click="select(product)"> Edit
                    </b-button>
                </td>
                <td>
                    <b-button variant="danger" v-b-modal.delete-product-dialog v-on:click="select(product)"> Delete
                    </b-button>
                </td>
            </tr>
            </tbody>
        </table>
        <!-- Add Product -->
        <b-modal id="add-product-dialog" title-tag="h2" title="Add product" hide-footer>
            <b-form @submit="onAddSubmit" @reset="hideModal('add-product-dialog'); clearAddFormObject();" class="w-100">
                <!-- Product category -->
                <b-form-group id="form-category-group" label="Name:" label-for="form-category-input">
                    <b-form-select id="form-category-input" v-model="addProductForm.category_id"
                                   :options="category_options">
                    </b-form-select>
                </b-form-group>
                <!-- Product name -->
                <b-form-group id="form-product-name-group" label="Name:" label-for="form-product-name-input">
                    <b-form-input id="form-product-name-input" type="text" v-model="addProductForm.name" required
                                  autofocus placeholder="Enter product name">
                    </b-form-input>
                </b-form-group>
                <!-- Product price -->
                <b-form-group id="form-product-price-group" label="Price (PLN):" label-for="form-product-price-input">
                    <b-form-input id="form-product-price-input" type="number" step="0.01" min="0"
                                  v-model="addProductForm.price" required autofocus placeholder="Enter product price">
                    </b-form-input>
                </b-form-group>
                <!-- Product picture URL -->
                <b-form-group id="form-url-group" label="Picture URL:" label-for="form-url-input">
                    <b-form-input id="form-url-input" type="url" v-model="addProductForm.picture_file_url" required
                                  autofocus placeholder="Enter picture URL">
                    </b-form-input>
                </b-form-group>
                <!-- Product description -->
                <b-form-group id="form-product-description-group" label="Product description:"
                              label-for="form-product-description-input">
                    <b-form-textarea oninput='this.style.height = ""; this.style.height = this.scrollHeight + "px"'
                                     spellcheck="false" id="form-product-description-input"
                                     v-model="addProductForm.description"
                                     required autofocus placeholder="Product description" rows="5">
                    </b-form-textarea>
                </b-form-group>
                <!-- Buttons -->
                <div class="modal-footer">
                    <b-button type="reset" variant="danger">Cancel</b-button>
                    <b-button type="submit" variant="success">Add Product</b-button>
                </div>
            </b-form>
        </b-modal>
        <!-- Delete Product -->
        <b-modal id="delete-product-dialog" hide-footer>
            <p> Are sure do you want to delete "{{ selectedProduct.name }}"? </p>
            <div class="modal-footer">
                <b-button variant="success" @click="hideModal('delete-product-dialog')">No</b-button>
                <b-button variant="danger" @click="deleteProduct();hideModal('delete-product-dialog');">Yes</b-button>
            </div>
        </b-modal>
        <!-- Edit Product -->
        <b-modal id="edit-product-dialog" title-tag="h2" title="Edit product" hide-footer>
            <b-form @submit="onEditSubmit" @reset="hideModal('edit-product-dialog')" class="w-100">
                <!-- Product name -->
                <b-form-group id="form-name-group" label="Name:" label-for="form-name-input">
                    <b-form-input id="form-name-input" type="text" v-model="selectedProduct.name" required autofocus
                                  placeholder="Enter product name">
                    </b-form-input>
                </b-form-group>
                <!-- Product price -->
                <b-form-group id="form-price-group" label="Price (PLN):" label-for="form-price-input">
                    <b-form-input id="form-price-input" type="number" step="0.01" min="0"
                                  v-model="selectedProduct.price" required autofocus placeholder="Enter product price">
                    </b-form-input>
                </b-form-group>
                <!-- Product picture URL -->
                <b-form-group id="form-picture-url-group" label="Picture URL:" label-for="form-picture-url-input">
                    <b-form-input id="form-picture-url-input" type="url" v-model="selectedProduct.picture_file_url"
                                  required autofocus placeholder="Enter picture URL">
                    </b-form-input>
                </b-form-group>
                <!-- Product description -->
                <b-form-group id="form-description-group" label="Product description:"
                              label-for="form-description-input">
                    <b-form-textarea oninput='this.style.height = ""; this.style.height = this.scrollHeight + "px"'
                                     spellcheck="false"
                                     id="form-description-input" v-model="selectedProduct.description" required
                                     autofocus placeholder="Product description" rows="12">
                    </b-form-textarea>
                </b-form-group>
                <!-- Buttons -->
                <div class="modal-footer">
                    <b-button type="reset" variant="danger"> Cancel</b-button>
                    <b-button type="submit" variant="success"> Edit</b-button>
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
                addProductForm: {
                    category_id: 0,
                    name: '',
                    price: 0.0,
                    picture_file_url: '',
                    description: '',
                },
                productCategories: [],
                category_options: [],
            }
        },
        methods: {
            setCategoryOptions() {
                let defaultOption = {value: 0, text: 'Select category', disabled: true};
                this.category_options.push(defaultOption);
                for (var i = 0; i < this.productCategories.length; i++) {
                    let category = this.productCategories[i];
                    let tempOption = {value: category.id, text: category.name};
                    this.category_options.push(tempOption);
                }
            },
            getProductCategories() {
                const path = 'http://localhost:5002/products/categories';
                axios.get(path)
                    .then((res) => {
                        this.productCategories = res.data.data;
                        this.setCategoryOptions();
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            },
            getAllProducts() {
                this.getProductCategories();
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
            editProduct(productID, requestJSON) {
                const path = 'http://localhost:5002/products/' + String(productID);
                axios.put(path, requestJSON)
                    .then(() => {
                        this.getAllProducts();
                    })
                    .catch((error) => {
                        console.error(error);
                        this.getAllProducts();
                    });
            },
            onEditSubmit(evt) {
                evt.preventDefault();
                this.hideModal("edit-product-dialog");
                const productID = this.selectedProduct.id;
                const requestJSON = {
                    name: this.selectedProduct.name,
                    price: this.selectedProduct.price,
                    picture_file_url: this.selectedProduct.picture_file_url,
                    product_description: this.selectedProduct.description,
                };
                this.editProduct(productID, requestJSON);
            },
            clearAddFormObject() {
                this.addProductForm.category_id = 0;
                this.addProductForm.name = '';
                this.addProductForm.price = 0.0;
                this.addProductForm.picture_file_url = '';
                this.addProductForm.description = '';
            },
            addProduct(categoryID, requestJSON) {
                const path = 'http://localhost:5002/products/' + String(categoryID);
                axios.post(path, requestJSON)
                    .then(() => {
                        this.getAllProducts();
                    })
                    .catch((error) => {
                        console.error(error);
                        this.getAllProducts();
                    });
            },
            onAddSubmit(evt) {
                evt.preventDefault();
                const categoryID = this.addProductForm.category_id;
                const requestJSON = {
                    name: this.addProductForm.name,
                    price: this.addProductForm.price,
                    picture_file_url: this.addProductForm.picture_file_url,
                    product_description: this.addProductForm.description,
                };
                this.addProduct(categoryID, requestJSON);
                this.hideModal("add-product-dialog");
                this.clearAddFormObject();
            }
        },
        created() {
            this.getAllProducts();
        }
    }
</script>