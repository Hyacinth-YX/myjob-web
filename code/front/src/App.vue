<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="toolbar q-pa-sm">
        <q-toolbar-title class="q-ml-lg" style="font-family: 'Impact', fantasy">
          My Job
          <q-btn flat label="首页" class="q-ml-lg" @click="goToHome"></q-btn>
          <q-btn flat label="职业讨论" @click="goToDiscussion"></q-btn>
          <q-btn flat label="holland测试" @click="goToTest"></q-btn>
        </q-toolbar-title>

        <q-space></q-space>
        <q-btn v-if="!isLogin" flat label="Sign In" @click="goToLogin"></q-btn>
        <q-btn v-else flat label="Logout" @click="logout"></q-btn>
        <q-btn
          dense
          flat
          size="lg"
          icon="account_circle"
          @click="goToLogin"
        ></q-btn>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view></router-view>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "LayoutDefault",
  data() {
    return {
      isLogin: false,
    };
  },
  mounted: async function () {
    let res = await this.$api.user.isLogin();
    this.isLogin = res.data.data.result;
  },
  watch: {
    $route: async function () {
      let res = await this.$api.user.isLogin();
      this.isLogin = res.data.data.result;
    },
  },
  methods: {
    logout: async function () {
      await this.$api.user.logout();
      this.isLogin = false;
    },
    goToLogin() {
      this.$router.replace({ name: "Login" });
    },
    goToHome() {
      this.$router.replace({ name: "Home" });
    },
    goToDiscussion() {
      this.$router.replace({ name: "Discussion" });
    },
    goToTest() {
      this.$router.replace({ name: "test" });
    },
  },
};
</script>

<style>
body {
  background: rgb(250, 250, 250);
}
.toolbar {
  background: #2e333a;
}
</style>
