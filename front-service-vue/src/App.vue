<template>
    <div id="app">
        <notifications group="foo" :classes="notificationClasses" />
        <div id="nav">
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
            Footer
        },
        created () {
            window.eventBus.$on('successProductAdded', data => {
                this.notificationClasses = 'vue-notification success'
                this.$notify({
                  group: 'foo',
                  title: 'Success',
                  text: data
                });
            });

            window.eventBus.$on('errorProductNotAdded', data => {
                this.notificationClasses = 'vue-notification error'
                this.$notify({
                  group: 'foo',
                  title: 'Error',
                  text: data
                });
            });

            // window.eventBus.$on('successProductEdited', data => {
            //     //this.$swal('Heading', data, 'OK');
            //     this.$swal({
            //       type: 'success',
            //       title: 'Oops...',
            //       text: 'Something went wrong!',
            //   })
            // });

            window.eventBus.$on('successProductEdited', data => {
                this.notificationClasses = 'vue-notification success'
                this.$notify({
                  group: 'foo',
                  title: 'Success',
                  text: data
                });
            });

            window.eventBus.$on('errorProductNotEdited', data => {
                this.notificationClasses = 'vue-notification error'
                this.$notify({
                  group: 'foo',
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
