import Vue from "vue"
import app from "./app"
import router from "./router"
import VueResource from "vue-resource"

Vue.config.productionTip = true;
Vue.use(VueResource);

// estudar se eh melhor solucao
export const bus = new Vue({});

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  template: "<app/>",
  components: { app }
})
