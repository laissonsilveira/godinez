import Vue from "vue"
import Router from "vue-router"
import home from "@/views/home/home"
import issues from "@/views/issues/issues"

Vue.use(Router)

export default new Router({
  routes: [
    { path: "/", component: home, name: "Home" },
    { path: "/issues", component: issues, name: "Issues" }
  ]
})
