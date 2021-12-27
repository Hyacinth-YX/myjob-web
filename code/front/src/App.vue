<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated >
      <q-toolbar class="toolbar q-pa-sm">
        <q-toolbar-title class="q-ml-lg" style="font-family: 'Impact',fantasy;">
          My Job
          <q-btn flat label="首页" class="q-ml-lg" @click="goToHome"></q-btn>
          <q-btn flat label="职业讨论" @click="goToDiscussion"></q-btn>
        </q-toolbar-title>

        <q-space></q-space>
        <q-btn flat label="Sign In" @click="goToLogin"></q-btn>
        <q-btn dense flat size="lg" icon="account_circle" @click="goToLogin"></q-btn>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view></router-view>
    </q-page-container>
  </q-layout>
</template>

<script>

export default {
  name: 'LayoutDefault',
  data () {
    return {
    }
  },
  methods:{
    goToLogin(){
      this.$router.replace({name:"Login"})
    },
    goToHome(){
      this.$router.replace({name:"Home"})
    },
    goToDiscussion(){
      this.$router.replace({name:"Discussion"})
    }
  }
}
</script>

<style>
body{
  background: rgb(250, 250, 250);
}
.toolbar{
  background: #2E333A;
}


</style>
