<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated >
      <q-toolbar>
        <q-toolbar-title>
          Myjob
        </q-toolbar-title>

        <q-btn dense flat size="lg" icon="account_circle"></q-btn>
      </q-toolbar>
      <q-toolbar inset>
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
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
</style>
