<template>
    <div class="container">
        <h1>Manage Your Account</h1>
        <h4>{{user.first_name}}</h4>
        <h4>{{user.last_name}}</h4>
        <h4 class="mt-3">Buying history: </h4>
        <table class="table" style="max-width: 500px">
            <thead>
            <tr>
                <th>Id</th>
                <th>Status</th>
                <th>Date</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="order in orders">
                <td>{{ order.order_id }}</td>
                <td>{{ order.order_status.description }}</td>
                <td>{{ order.created }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: 'account',
        data() {
            return {
                orders: [],
                user: {},
                order_price: 0,
            }
        },
        methods: {
            getUserData() {
                let token = localStorage.getItem('token');
                if (token) {
                    let headers = {
                        Authorization: 'Bearer ' + token,
                    };
                    const USERS_URL = `${process.env.VUE_APP_USERS_SERVICE_URL}/users/token`;
                    this.$http.get(USERS_URL, {headers: headers})
                        .then(function (response) {
                            this.user = response.body.data;
                        });
                }
            },
            getOrdersData() {
                let token = localStorage.getItem('token');
                if (token) {
                    const ORDERS_URL = `${process.env.VUE_APP_ORDERS_SERVICE_URL}/orders`
                        + '?token='
                        + token;
                    this.$http.get(ORDERS_URL)
                        .then(function (response) {
                            this.orders = response.body.data;
                        });
                }
            },
        },
        created: function () {
            this.getUserData();
            this.getOrdersData();
        }
    }
</script>
