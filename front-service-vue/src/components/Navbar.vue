<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="primary">
            <b-navbar-brand to="/">WebShop</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item to="/">Home</b-nav-item>
                    <b-nav-item-dropdown text="Categories" right>
                        <b-dropdown-item to="/category/Shoes">Shoes</b-dropdown-item>
                        <b-dropdown-item to="/category/T-Shirts">T-Shirts</b-dropdown-item>
                        <b-dropdown-item to="/category/Jackets">Jackets</b-dropdown-item>
                        <b-dropdown-item to="/category/Trousers">Trousers</b-dropdown-item>
                        <b-dropdown-item to="/category/Shirts">Shirts</b-dropdown-item>
                    </b-nav-item-dropdown>
                    <b-nav-item to="/contact">Contact us</b-nav-item>
                    <b-nav-item to="/panel">Panel</b-nav-item>
                    <b-nav-item to="/account">My Account</b-nav-item>
                    <b-nav-item to="/login">Log in</b-nav-item>
                </b-navbar-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-form>
                        <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                    </b-nav-form>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: 'Navbar',
    };
</script>