import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vueResource from 'vue-resource';
import BootstrapVue from 'bootstrap-vue';
import Autocomplete from '@trevoreyre/autocomplete-vue'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import '@trevoreyre/autocomplete-vue/dist/style.css'
import { library } from '@fortawesome/fontawesome-svg-core';
import { faShoppingCart } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import Notifications from 'vue-notification';
import VueSweetalert2 from 'vue-sweetalert2';

library.add(faShoppingCart);

Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(vueResource);
Vue.use(Autocomplete)
Vue.use(Notifications)
Vue.use(VueSweetalert2);

window.eventBus = new Vue({});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
