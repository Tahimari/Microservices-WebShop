<template>
    <div class="container">
        <b-jumbotron header="Please sign in">
            <Alert v-if="alert" v-bind:message="alert"/>
            <form v-on:submit="login" class="form-signin" method="post">
                <label for="inputEmail" class="sr-only">Email address</label>
                <input type="email" value="" name="email" id="inputEmail" class="form-control"
                       placeholder="Email address" required autofocus v-model="pass.email">
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" name="password" id="inputPassword" class="form-control"
                       placeholder="Password" v-model="pass.password">
    <!--            <div class="checkbox mb-3">-->
    <!--                <label>-->
    <!--                    <input type="checkbox" name="_remember_me"> Remember me-->
    <!--                </label>-->
    <!--            </div>-->
                <button type="submit" class="btn btn-primary">Log in!</button>
             </form>
            <router-link to="/register">Don't have account? Sign up!</router-link>
        </b-jumbotron>
    </div>
</template>

<script>
    import Alert from '../../components/Alert';;

    export default {
        data() {
            return {
                pass: {},
                alert: ''
            }
        },
        methods: {
            login(e) {
                if (!this.pass.email || !this.pass.password) {
                    this.alert = 'Please fill in all required fields';
                } else {
                    let newPass = {
                        email: this.pass.email,
                        password: this.pass.password,
                    }
                    const LOGIN_URL = `${process.env.VUE_APP_USERS_SERVICE_URL}/users/login`;
                    this.$http.post(LOGIN_URL, newPass)
                        .then(function (response) {
                            localStorage.setItem('token', response.body.token);
                            this.$router.push({path: '/', query: {alert: 'Login'}});
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