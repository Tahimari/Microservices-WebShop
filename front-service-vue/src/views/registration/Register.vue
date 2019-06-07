<template>
    <div class="add container">
        <Alert v-if="alert" v-bind:message="alert"/>
        <h1 class="page-header">Register</h1>
        
        <b-form @submit="onSubmit" class="w-100">
			<!-- Email -->
			<b-form-group id="form-email-group" label="Email:" label-for="form-email-input">
				<b-form-input id="form-email-input" type="email" v-model="addUserForm.email" required autofocus placeholder="Enter email">
				</b-form-input>
			</b-form-group>
			
			<!-- First Name -->
			<b-form-group id="form-first-name-group" label="First Name:" label-for="form-first-name-input">
				<b-form-input id="form-first-name-input" type="text" v-model="addUserForm.first_name" required placeholder="Enter first name">
				</b-form-input>
			</b-form-group>
			
            <!-- Last Name -->
			<b-form-group id="form-last-name-group" label="Last Name:" label-for="form-last-name-input">
				<b-form-input id="form-last-name-input" type="text" v-model="addUserForm.last_name" required placeholder="Enter last name">
				</b-form-input>
			</b-form-group>

            <!-- Password -->
			<b-form-group id="form-password-group" label="Password:" label-for="form-password-input">
				<b-form-input id="form-password-input" type="password" v-model="addUserForm.password" required placeholder="Enter password">
				</b-form-input>
			</b-form-group>

            <!-- Submit button -->
			<b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
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
                this.initForm();
            },
            addUser(payload) {
                const path = 'http://localhost:5001/users';
                this.$http.post(path, payload)
                .then(() => {
                    this.alert = 'Customer added!';
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
        },
        components: {
            Alert
        }
    }
</script>
