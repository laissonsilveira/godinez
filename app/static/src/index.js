import Teste from "./teste";

new Vue({
    el: '#app',
    data: {
        message: new Teste().getName()
    }
});