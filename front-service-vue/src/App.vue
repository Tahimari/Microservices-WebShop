<template>
    <div id="app">
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
