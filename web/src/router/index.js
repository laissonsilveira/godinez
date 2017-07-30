import Vue from "vue"
import Router from "vue-router"
import Home from "@/components/Home"
import Issues from "@/components/issues/issues"

Vue.use(Router)

export default new Router({
  routes: [
    { path: "/", component: Home, name: "Home" },
    { path: "/issues", component: Issues, name: "Issues" }
  ]
})
