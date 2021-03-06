import Vue from "vue";
import Router from "vue-router";
import Home from "./views/items/Home.vue";
import Show from "./views/items/Show.vue";
import Contact from "./views/contact/Contact.vue";
import Login from "./views/security/Login.vue";
import Register from "./views/registration/Register.vue";
import Panel from "./views/administrator_panel/List.vue";
import Account from "./views/account/Index.vue";
import Cart from "./views/buy_item/Cart.vue"
import Delivery from "./views/buy_item/Delivery.vue"

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: "/delivery",
      name: "delivery",
      component: Delivery
    },
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/category/:name",
      name: "category",
      component: Home
    },
    {
      path: "/show/:product_id",
      name: "show",
      component: Show
    },
    {
      path: "/contact",
      name: "contact",
      component: Contact
    },
    {
      path: "/login",
      name: "login",
      component: Login
    },
    {
      path: "/register",
      name: "register",
      component: Register
    },
    {
      path: "/panel",
      name: "panel",
      component: Panel
    },
    {
      path: "/account",
      name: "account",
      component: Account
    },
    {
      path: "/cart",
      name: "cart",
      component: Cart
    }
  ]
});
