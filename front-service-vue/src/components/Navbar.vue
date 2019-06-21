<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="primary">
            <b-navbar-brand to="/">WebShop</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
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
                     <b-nav-item v-if="token" to="/cart">Cart</b-nav-item>
                    <b-nav-form>
                        <b-form-input size="sm" class="mr-sm-2" placeholder="Search" 
                            v-on:keydown.enter.prevent="filterProductList()" v-model="searchString"></b-form-input>
                        <b-button size="sm" class="my-2 my-sm-0" v-on:click="filterProductList()"> Search </b-button>
                    </b-nav-form>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: 'Navbar',
        data: function() {
            return {
                token: '',
                admin: false,
                searchString: ''
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
        watch:{
            $route (){
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
            filterProductList() {
                if (this.searchString.length > 0) {
                    let queryString = this.searchString;
                    this.searchString = '';
                    this.$router.push({path: '/', query: {search: queryString}});
                }
            },
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
            }
        }
    };
</script>