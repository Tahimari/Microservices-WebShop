<template>
    <div class="container">
        <b-jumbotron header="Please sign in">
            <Alert v-if="alert" v-bind:message="alert"/>
            <!-- Login form -->        
            <b-form @submit="login" class="w-100" method="post">
                <!-- Email -->
				<b-form-group id="form-email-group" label="Email:" label-for="form-email-input">
					<b-form-input id="form-email-input" type="email" v-model="pass.email" required autofocus placeholder="Enter email">
					</b-form-input>
				</b-form-group>
                <!-- Password -->
				<b-form-group id="form-password-group" label="Password:" label-for="form-password-input">
					<b-form-input id="form-password-input" type="password" v-model="pass.password" required placeholder="Enter password">
					</b-form-input>
				</b-form-group>
                <!-- Submit button -->
				<b-button type="submit" variant="primary">Log in!</b-button>
            </b-form>
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