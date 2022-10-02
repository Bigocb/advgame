import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";
// import "primeflex/primeflex.css";
import "primevue/resources/themes/lara-light-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
import InputText from 'primevue/inputtext';
// import Vue3EasyDataTable from 'vue3-easy-data-table';
// import 'vue3-easy-data-table/dist/style.css';
import PrimeVue from 'primevue/config';
import Button from 'primevue/button/sfc';

import ArgonDashboard from "./argon-dashboard";

const appInstance = createApp(App);
appInstance.use(store);
appInstance.use(router);
appInstance.use(ArgonDashboard);
appInstance.mount("#app");
appInstance.use(PrimeVue);
appInstance.component('Button', Button);
appInstance.component('InputText', InputText);
// appInstance.component('EasyDataTable', Vue3EasyDataTable);