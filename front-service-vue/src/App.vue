<template>
    <div id="app">
        <div id="nav">
            <notifications group="adminAlerts" :classes="notificationClasses" />
            <Navbar/>
        </div>
        <div class="content">
            <router-view/>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Navbar from '@/components/Navbar.vue';
    import Footer from '@/components/Footer.vue';

    export default {
        name: "App",
        components: {
            Navbar,
            Footer,
        },
        created () {
            window.eventBus.$on('successProductRelated', data => {
                this.notificationClasses = 'vue-notification success'
                this.$notify({
                  group: 'adminAlerts',
                  title: 'Success',
                  text: data
                });
            });

            window.eventBus.$on('errorProductRelated', data => {
                this.notificationClasses = 'vue-notification error'
                this.$notify({
                  group: 'adminAlerts',
                  title: 'Error',
                  text: data
                });
            });

            window.eventBus.$on('successOrderCompleted', data => {
                this.$swal({
                  type: 'success',
                  title: 'Success',
                  text: data,
              })
            });

            window.eventBus.$on('successLog', data => {
                this.$swal({
                  position: 'top-end',
                  type: 'success',
                  text: data,
                  showConfirmButton: false,
                  timer: 1500
              })
            });

        },
        data () {
            return {
                notificationClasses: null,
            }
        }
    };
</script>

<style>
    .content {
        min-height: calc(100vh - 220px);
    }

    .footer {
        height: 50px;
    }
</style>
