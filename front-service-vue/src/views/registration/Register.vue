<template>
    <div class="add container">
        <Alert v-if="alert" v-bind:message="alert"/>
		<b-jumbotron header="Register">
			<b-form @submit="onSubmit" class="w-100">
				<b-form-group id="form-email-group" label="Email:" label-for="form-email-input">
					<b-form-input id="form-email-input" type="email" v-model="addUserForm.email" required autofocus placeholder="Enter email">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-first-name-group" label="First Name:" label-for="form-first-name-input">
					<b-form-input id="form-first-name-input" type="text" v-model="addUserForm.first_name" required placeholder="Enter first name">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-last-name-group" label="Last Name:" label-for="form-last-name-input">
					<b-form-input id="form-last-name-input" type="text" v-model="addUserForm.last_name" required placeholder="Enter last name">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-password-group" label="Password:" label-for="form-password-input">
					<b-form-input id="form-password-input" type="password" v-model="addUserForm.password" required placeholder="Enter password">
					</b-form-input>
				</b-form-group>
				<b-button type="submit" variant="primary">Submit</b-button>
			</b-form>
		</b-jumbotron>
    </div>
</template>

<script>
    import Alert from '../../components/Alert'

    export default {
        name: 'add',
        data() {
            return {
                addUserForm: {
					email: '',
					first_name: '',
					last_name: '',
					password: '',
				},
                alert: '',
            };
        },
        methods: {
            onSubmit(evt) {
                evt.preventDefault();
                const payload = {
                    email: this.addUserForm.email,
                    first_name: this.addUserForm.first_name,
                    last_name: this.addUserForm.last_name,
                    password: this.addUserForm.password,
                };
                this.addUser(payload);
            },
            addUser(payload) {
				const path = `${process.env.VUE_APP_USERS_SERVICE_URL}/users`;
                this.$http.post(path, payload)
                .then(() => {
                    this.alert = 'Customer added!';
                    this.initForm();
                    this.triggerLogin(payload.email, payload.password);
                    this.$router.push({path: '/'});
                })
                .catch((error) => {
                    console.log(error);
                });
            },
            initForm() {
                this.addUserForm.email = '';
                this.addUserForm.first_name = '';
                this.addUserForm.last_name = '';
                this.addUserForm.password = '';
            },
            triggerLogin(email, password) {
                this.$root.$emit('triggerLogin', email, password);
            }
        },
        components: {
            Alert
        }
    }
</script>
