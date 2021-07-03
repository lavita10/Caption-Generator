import Vue from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

Vue.config.productionTip = false;

new Vue({
  router,
  //bootstrap,
  render: (h) => h(App),
}).$mount('#app');
