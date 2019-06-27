<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="primary">
            <div class="container">
                <b-navbar-brand to="/">WebShop</b-navbar-brand>
                <b-navbar-toggle
                        target="nav-collapse"
                        :class="showCollapse ? 'collapsed' : null"
                        :aria-expanded="showCollapse ? 'true' : 'false'"
                        aria-controls="collapse-4"
                        @click="showCollapse = !showCollapse">
                </b-navbar-toggle>
                <b-collapse
                        id="nav-collapse"
                        is-nav
                        v-model="showCollapse"
                >
                    <b-navbar-nav>
                        <b-nav-item to="/">Home</b-nav-item>
                        <b-nav-item-dropdown text="Categories" right>
                            <b-dropdown-item to="/category/Shoes">Shoes</b-dropdown-item>
                            <b-dropdown-item to="/category/T-Shirts">T-Shirts</b-dropdown-item>
                            <b-dropdown-item to="/category/Jackets">Jackets</b-dropdown-item>
                            <b-dropdown-item to="/category/Trousers">Trousers</b-dropdown-item>
                            <b-dropdown-item to="/category/Shirts">Shirts</b-dropdown-item>
                        </b-nav-item-dropdown>
                        <b-nav-item to="/contact">Contact us</b-nav-item>
                        <b-nav-item v-if="token && admin === true" to="/panel">Panel</b-nav-item>
                        <b-nav-item v-if="token" to="/account">My Account</b-nav-item>
                        <b-nav-item v-if="!token" to="/login">Log in</b-nav-item>
                        <b-nav-item v-if="token" v-on:click="logout" to="/logout">Log out</b-nav-item>
                    </b-navbar-nav>
                    <b-navbar-nav class="ml-auto">
                        <b-nav-item v-if="token" to="/cart">
                            <font-awesome-icon icon="shopping-cart" class="mr-3"/>
                        </b-nav-item>
                        <autocomplete
                                :search="search"
                                placeholder="Search Products"
                                aria-label="Search Products"
                                :get-result-value="getResultValue"
                                @submit="handleSubmit"
                        ></autocomplete>
                    </b-navbar-nav>
                </b-collapse>
            </div>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: 'Navbar',
        data:
            function () {
                return {
                    token: '',
                    admin: false,
                    searchString: '',
                    showCollapse: false,
                };
            },
        mounted() {
            if (localStorage.token) {
                this.token = localStorage.token;
            }
            if (localStorage.admin) {
                this.admin = JSON.parse(localStorage.admin);
            }
        },
        watch: {
            $route() {
                if (localStorage.token) {
                    this.token = localStorage.token;
                } else {
                    this.token = '';
                }
                if (localStorage.admin) {
                    this.admin = JSON.parse(localStorage.admin);
                } else {
                    this.admin = false;
                }
            }
        },
        methods: {
            logout(e) {
                e.preventDefault();
                let data = {};
                let headers = {
                    Authorization: 'Bearer ' + this.token,
                };
                const LOGOUT_URL = `${process.env.VUE_APP_USERS_SERVICE_URL}/users/logout`;
                this.$http.post(LOGOUT_URL, data, {headers: headers})
                    .then(function () {
                        localStorage.removeItem('token');
                        localStorage.removeItem('admin');
                        this.$router.push({path: '/', query: {alert: 'Logout'}});
                    }, response => {
                        localStorage.removeItem('token');
                        this.token = '';
                        localStorage.removeItem('admin');
                        this.admin = false;
                        this.$router.push({path: '/', query: {alert: 'Logout'}});
                    });
            },
            search(input) {
                this.searchString = input;
                const url = `${
                    process.env.VUE_APP_PRODUCTS_SERVICE_URL
                    }/products?&query=${encodeURI(input)}`;

                return new Promise(resolve => {
                    if (input.length < 3) {
                        return resolve([])
                    }

                    fetch(url)
                        .then(response => response.json())
                        .then(data => {
                            resolve(data.data)
                        })
                })
            },
            getResultValue(result) {
                return result.name
            },
            handleSubmit(result) {
                this.showCollapse = false;
                if (result) {
                    this.$router.push({name: 'show', params: {product_id: result.id}});
                } else {
                    this.$router.push({name: 'home', query: {search: this.searchString}});
                }
            }
        }
    }
    ;
</script>