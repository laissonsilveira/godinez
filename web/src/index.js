import VueRouter from '../dist/lib/vue-router/dist/vue-router';
import App from './components/App.vue';
import ComponentA from './components/ComponentA.vue';
import ComponentB from './components/ComponentA.vue';

Vue.use(VueRouter)  

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'component-a',
      component: ComponentA
    }
  ]
});

new Vue({  
  el: 'body',
  components: { 
  	App 
  }
});