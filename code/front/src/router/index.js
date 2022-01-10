import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/discussion",
    name: "Discussion",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Discussion"),
  },
  {
    path: "/test",
    name: "test",
    component: () => import(/* webpackChunkName: "about" */ "../views/test"),
  },
  {
    path: "/post",
    name: "Post",
    component: () => import(/* webpackChunkName: "about" */ "../views/Post"),
  },
  {
    path: "/industry",
    name: "Industry",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Industry"),
  },
  {
    path: "/job",
    name: "Job",
    component: () => import(/* webpackChunkName: "about" */ "../views/Job"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import(/* webpackChunkName: "about" */ "../views/Login"),
  },
  {
    path: "/register",
    name: "Register",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Register"),
  },
  {
    path: "/testResult",
    name: "TestResult",
    component: () => import("../views/TestResult"),
  },
];

const router = new VueRouter({
  mode: "hash",
  base: process.env.BASE_URL,
  routes,
});

export default router;
