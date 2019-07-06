<template>
    <div class="add container">
        <b-jumbotron header="Contact Us">
            <Alert v-if="alert" v-bind:message="alert"/>
            <b-form class="w-100" @submit="sendMail" method="post">
                <b-form-group id="form-email-group" label="Email:" label-for="form-email-input">
                    <b-form-input id="form-email-input" v-model="mail.email" name="Email" type="email" required
                                  autofocus placeholder="Your email">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-name-group" label="Name:" label-for="form-name-input">
                    <b-form-input id="form-name-input" v-model="mail.name" name="Name" type="text" required
                                  placeholder="Your name">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-message-group" label="Message:" label-for="form-message-input">
                    <b-form-textarea id="form-message-input" v-model="mail.message" name="Message" required
                                     placeholder="Your message">
                    </b-form-textarea>
                </b-form-group>
                <b-button type="submit" variant="primary">Submit</b-button>
            </b-form>
        </b-jumbotron>
    </div>
</template>

<script>
    import Alert from '../../components/Alert';

    export default {
        data() {
            return {
                mail: {},
                alert: ''
            }
        },
        methods: {
            sendMail(e) {
                let isEventNull = (typeof e === "undefined");
                if (!this.mail.email || !this.mail.name || !this.mail.message) {
                    this.alert = 'Please fill in all required fields';
                } else {
                    let newMail = {
                        email: this.mail.email,
                        name: this.mail.name,
                        message: this.mail.message,
                    }
                    const MAIL_URL = `${process.env.VUE_APP_USERS_SERVICE_URL}/mail`;
                    this.$http.post(MAIL_URL, newMail)
                        .then(function (response) {
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
        },
        components: {
            Alert
        }
    }

</script>