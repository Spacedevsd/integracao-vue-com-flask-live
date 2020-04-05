import Vue from "vue";
import VueRouter from "vue-router";
import Contact from "./components/Contact";

Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    {
      path: "/contacts",
      name: "contacts",
      component: Contact,
    },
  ],
});

export default router;
