<template>
    <div class="add container">
        <Alert v-if="alert" v-bind:message="alert"/>
        <h1 class="page-header">Register</h1>
        <form v-on:submit="addUser">
            <label for="inputEmail" class="sr-only">Email address</label>
            <input type="email" value="" name="email" id="inputEmail" class="form-control" placeholder="Email address"
                   required autofocus>
            <label for="inputFirstName" class="sr-only">First name</label>
            <input type="text" value="" name="firstName" id="inputFirstName" class="form-control"
                   placeholder="First name" required autofocus>
            <label for="inputLastName" class="sr-only">Last name</label>
            <input type="text" value="" name="lastName" id="inputLastName" class="form-control"
                   placeholder="Last name" required autofocus>
            <label for="inputPassword" class="sr-only">Password</label>
            <input type="text" value="" name="password" id="inputPassword" class="form-control"
                   placeholder="Password" required autofocus>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>


<script>
    import Alert from '../../components/Alert'

    export default {
        name: 'add',
        data() {
            return {
                customer: {},
                alert: ''
            }
        },
        methods: {
            addCustomer(e) {
                if (!this.customer.first_name || !this.customer.last_name || !this.customer.email) {
                    this.alert = 'Please fill in all required fields';
                } else {
                    let newCustomer = {
                        first_name: this.customer.first_name,
                        last_name: this.customer.last_name,
                        phone: this.customer.phone,
                        email: this.customer.email,
                        address: this.customer.address,
                        city: this.customer.city,
                        state: this.customer.state
                    }

                    this.$http.post('http://slimapp/api/customer/add', newCustomer)
                        .then(function (response) {
                            this.$router.push({path: '/', query: {alert: 'Customer Added'}});
                        });

                    e.preventDefault();
                }
                e.preventDefault();
            }
        },
        components: {
            Alert
        }
    }
</script>