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
                <td class="d-none d-md-table-cell" style="white-space: pre-line">
                    {{ product.resources.product_description }}
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
        <b-modal id="add-product-dialog" title-tag="h2" title="Add product" hide-footer>
            <b-form @submit="onAddSubmit" @reset="hideModal('add-product-dialog'); clearAddFormObject();" class="w-100"
                    enctype="multipart/form-data">
                <b-form-group id="form-category-group" label="Name:" label-for="form-category-input">
                    <b-form-select id="form-category-input" v-model="addProductForm.category_id"
                                   :options="category_options">
                    </b-form-select>
                </b-form-group>
                <b-form-group id="form-product-name-group" label="Name:" label-for="form-product-name-input">
                    <b-form-input id="form-product-name-input" type="text" v-model="addProductForm.name" required
                                  autofocus placeholder="Enter product name">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-product-price-group" label="Price (PLN):" label-for="form-product-price-input">
                    <b-form-input id="form-product-price-input" type="number" step="0.01" min="0"
                                  v-model="addProductForm.price" required autofocus placeholder="Enter product price">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-product-image-group" label="Image:">
                    <b-form-file
                            v-model="file"
                            :state="Boolean(file)"
                            placeholder="Choose a file..."
                            drop-placeholder="Drop file here..."
                    ></b-form-file>
                </b-form-group>
                <b-form-group id="form-product-description-group" label="Product description:"
                              label-for="form-product-description-input">
                    <b-form-textarea oninput='this.style.height = ""; this.style.height = this.scrollHeight + "px"'
                                     spellcheck="false" id="form-product-description-input"
                                     v-model="addProductForm.description"
                                     required autofocus placeholder="Product description" rows="5">
                    </b-form-textarea>
                </b-form-group>
                <div class="modal-footer">
                    <b-button type="reset" variant="danger">Cancel</b-button>
                    <b-button type="submit" variant="success">Add Product</b-button>
                </div>
            </b-form>
        </b-modal>
        <b-modal id="delete-product-dialog" hide-footer>
            <p> Are sure do you want to delete "{{ selectedProduct.name }}"? </p>
            <div class="modal-footer">
                <b-button variant="success" @click="hideModal('delete-product-dialog')">No</b-button>
                <b-button variant="danger" @click="deleteProduct();hideModal('delete-product-dialog');">Yes</b-button>
            </div>
        </b-modal>
        <b-modal id="edit-product-dialog" title-tag="h2" title="Edit product" hide-footer>
            <b-form @submit="onEditSubmit" @reset="hideModal('edit-product-dialog')" class="w-100"
                    enctype="multipart/form-data">
                <b-form-group id="form-name-group" label="Name:" label-for="form-name-input">
                    <b-form-input id="form-name-input" type="text" v-model="selectedProduct.name" required autofocus
                                  placeholder="Enter product name">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-price-group" label="Price (PLN):" label-for="form-price-input">
                    <b-form-input id="form-price-input" type="number" step="0.01" min="0"
                                  v-model="selectedProduct.price" required autofocus placeholder="Enter product price">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-image-group" label="Image:">
                    <b-form-file
                            v-model="file"
                            :state="Boolean(file)"
                            placeholder="Choose a file..."
                            drop-placeholder="Drop file here..."
                    ></b-form-file>
                </b-form-group>
                <b-form-group id="form-description-group" label="Product description:"
                              label-for="form-description-input">
                    <b-form-textarea oninput='this.style.height = ""; this.style.height = this.scrollHeight + "px"'
                                     spellcheck="false"
                                     id="form-description-input" v-model="selectedProduct.description" required
                                     autofocus placeholder="Product description" rows="12">
                    </b-form-textarea>
                </b-form-group>
                <div class="modal-footer">
                    <b-button type="reset" variant="danger">Cancel</b-button>
                    <b-button type="submit" variant="success">Edit</b-button>
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
                    description: '',
                },
                addProductForm: {
                    category_id: 0,
                    name: '',
                    price: 0.0,
                    description: '',
                },
                productCategories: [],
                category_options: [],
                file: "",
            }
        },
        methods: {
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
            setCategoryOptions() {
                let defaultOption = {value: 0, text: 'Select category', disabled: true};
                this.category_options.push(defaultOption);
                for (var i = 0; i < this.productCategories.length; i++) {
                    let category = this.productCategories[i];
                    let tempOption = {value: category.id, text: category.name};
                    this.category_options.push(tempOption);
                }
            },
            select(product) {
                this.selectedProduct.id = product.id;
                this.selectedProduct.name = product.name;
                this.selectedProduct.price = product.price;
                this.selectedProduct.picture_file_url = product.resources.picture_file_url;
                this.selectedProduct.description = product.resources.product_description;
            },
            validate(file) {
                const allowedTypes = ["image/jpeg", "image/png", "image/gif"];
                const MAX_SIZE = 200000;
                const tooLarge = file.size > MAX_SIZE;
                if (allowedTypes.includes(file.type) && !tooLarge) {
                    return true;
                } else {
                    return false;
                }
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
            onEditSubmit(evt) {
                evt.preventDefault();
                this.hideModal("edit-product-dialog");
                const formData = new FormData();
                const productID = this.selectedProduct.id;
                formData.append('name', this.selectedProduct.name);
                formData.append('price', this.selectedProduct.price);
                formData.append('file', this.file);
                formData.append('product_description', this.selectedProduct.description);
                this.editProduct(productID, formData);
                this.file = "";
            },
            editProduct(productID, formData) {
                const PRODUCT_URL = `${process.env.VUE_APP_PRODUCTS_SERVICE_URL}/products/edit/${productID}`;
                axios.post(PRODUCT_URL, formData)
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
                if (this.validate(this.file)) {
                    const categoryID = this.addProductForm.category_id;
                    const formData = new FormData();
                    formData.append('name', this.addProductForm.name);
                    formData.append('price', this.addProductForm.price);
                    formData.append('file', this.file);
                    formData.append('product_description', this.addProductForm.description);
                    this.addProduct(categoryID, formData);
                    this.hideModal("add-product-dialog");
                    this.clearAddFormObject();
                }
            },
            addProduct(categoryID, formData) {
                const PRODUCT_URL = `${process.env.VUE_APP_PRODUCTS_SERVICE_URL}/products/${categoryID}`;
                axios.post(PRODUCT_URL, formData)
                    .then(() => {
                        this.getAllProducts();
                    })
                    .catch((error) => {
                        console.error(error);
                        this.getAllProducts();
                    });
            },
            clearFormObject() {
                this.addProductForm.category_id = 0;
                this.addProductForm.name = '';
                this.addProductForm.price = 0.0;
                this.addProductForm.picture_file_url = '';
                this.addProductForm.description = '';
                this.file = "";
            },
        },
        created() {
            this.getAllProducts();
        }
    }
</script>