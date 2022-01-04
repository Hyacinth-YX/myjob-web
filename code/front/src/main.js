import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./quasar";
import api from "./service/api";

Vue.prototype.$api = api;
Vue.config.productionTip = false;
Vue.filter("number", function (data) {
  return data.toFixed(2);
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
