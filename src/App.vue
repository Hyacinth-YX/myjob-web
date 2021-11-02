<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated >
      <q-toolbar class="toolbar q-pa-sm">
        <q-toolbar-title class="q-ml-lg" style="font-family: 'Impact',fantasy;">
          My Job
        </q-toolbar-title>
        <router-link to="/" class="text-white">Home</router-link> |
        <router-link to="/discussion" class="text-white">Discussion</router-link> |
        <router-link to="/post" class="text-white">Post</router-link> |
        <q-space></q-space>
        <q-btn dense flat size="lg" icon="account_circle"></q-btn>
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

  components: {
  },

  data () {
    return {
      leftDrawerOpen: false
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
body.post{
  background: white;
}
</style>
