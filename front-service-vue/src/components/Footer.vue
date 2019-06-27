<template>
    <div class="footer">
        <b-navbar toggleable="lg" type="dark" variant="primary">
            <div class="container footer-white">
                <b-navbar-nav>
                    <b-nav-item to="/">Home</b-nav-item>
                    <b-nav-item to="/contact">Contact us</b-nav-item>
                    <b-nav-item v-if="!token" to="/login">Log in</b-nav-item>
                    <b-nav-item v-if="token" v-on:click="logout" to="/logout">Log out</b-nav-item>
                </b-navbar-nav>
                <ul class="footer-right">
                    <li>COPYRIGHT WebShop 2019</li>
                    <li>WEB DESIGN & DEVELOPMENT:</li>
                    <li>Kamil Misiak</li>
                    <li>Grzegorz Galios</li>
                    <li>Sebastian Kania</li>
                </ul>
            </div>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        data:
            function () {
                return {
                    token: '',
                    admin: false,
                };
            }
        ,
        mounted() {
            if (localStorage.token) {
                this.token = localStorage.token;
            }
            if (localStorage.admin) {
                this.admin = JSON.parse(localStorage.admin);
            }
        }
        ,
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
        }
        ,
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
        }
    }
</script>

<style scoped>
    .footer-right {
        color: #fff;
        list-style: none;
        font-size: 12px;
    }

    @media screen and (max-width: 600px) {
        footer-right {
            margin-right: auto;
        }
    }
</style>