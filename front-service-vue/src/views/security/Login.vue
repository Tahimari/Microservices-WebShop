<template>
    <div class="container">
        <b-jumbotron header="Please sign in">
            <Alert v-if="alert" v-bind:message="alert"/>
            <b-form @submit="login" class="w-100" method="post">
				<b-form-group id="form-email-group" label="Email:" label-for="form-email-input">
					<b-form-input id="form-email-input" type="email" v-model="pass.email" required autofocus placeholder="Enter email">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-password-group" label="Password:" label-for="form-password-input">
					<b-form-input id="form-password-input" type="password" v-model="pass.password" required placeholder="Enter password">
					</b-form-input>
				</b-form-group>
				<b-button type="submit" variant="primary">Log in!</b-button>
            </b-form>
            <router-link to="/register">Don't have account? Sign up!</router-link>
        </b-jumbotron>
    </div>
</template>

<script>
    import Alert from '../../components/Alert';

    export default {
        data() {
            return {
                pass: {},
                alert: ''
            }
        },
        methods: {
            login(e) {
                let isEventNull = (typeof e === "undefined");
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
                            localStorage.setItem('admin', response.body.admin);
                            this.$router.push({path: '/', query: {alert: 'Login'}});
                        }, response => {
                            this.alert = response.body.message;
                        });
                    if (!isEventNull) {
                        e.preventDefault();
                    }
                }
                if (!isEventNull) {
                    e.preventDefault();
                }
            },
            loginAfterRegister(email, password) {
                this.pass['email'] = email;
                this.pass['password'] = password;
                this.login();
            }
        },
        mounted() {
            this.$root.$on('triggerLogin', (email, password) => {
                this.loginAfterRegister(email, password);
            });
        },
        components: {
            Alert
        }
    }
</script>