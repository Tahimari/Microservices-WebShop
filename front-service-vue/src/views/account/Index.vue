<template>
    <div class="container">
        <h1>Manage Your Account</h1>
        <h4>{{}}</h4>
        <h4>{{}}</h4>
        <h4 class="mt-3">Styles:</h4>
        <form method="POST">
            <div class="form-check">
                <label class="form-check-label">
                    <input type="radio" class="form-check-input" name="optradio"/>
                </label>
            </div>
            <div class="form-check">
                <label class="form-check-label">
                    <input type="radio" class="form-check-input" name="optradio"/>
                </label>
            </div>
            <a><button type="submit" class="btn btn-primary">Save</button></a>
        </form>

        <h4 class="mt-3">Buying history: </h4>
        <table class="table" style="max-width: 500px">
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Date</th>
                    <th>Price</th>
                    <th>Invoice</th>
                </tr>
            </thead>
            <tbody>
                    <tr v-for="user in users">
                        <td>{{ user.first_name }}</td>
                        <td>{{ user.last_name }}</td>
                        <td>{{  }}zł</td>
                        <td>
                            <a target="_blank" href="">
                                <i class="fas fa-angle-double-right"></i>
                            </a>
                        </td>
                    </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: 'account',
        data () {
            return {
                users: []
            }
        },
        methods: {
            fetchCustomers() {
                const USERS_URL = `${process.env.VUE_APP_USERS_SERVICE_URL}/users`;
                this.$http.get(USERS_URL)
                    .then(function (response) {
                        this.users = response.body['users'];
                    });
            }
        },
        created: function () {
            this.fetchCustomers();
        }
    }
</script>
