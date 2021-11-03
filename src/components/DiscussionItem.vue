<template>
  <q-item>
    <q-item-section>
      <q-item-label @click="goToPost" class="text-h5 cursor-pointer">{{ postData["title"] }}</q-item-label>
      <q-item-label class="text-body1">
        {{ postData["body"] }}
      </q-item-label>
    </q-item-section>

    <q-item-section side top>
      <q-item-label caption>5 min ago</q-item-label>
      <span><q-btn icon="thumb_up_alt" dense flat size="sm">123</q-btn><q-btn icon="thumb_down_alt" dense flat size="sm"> 23</q-btn></span>
      <span><q-icon name="visibility" size="sm" />123</span>
    </q-item-section>
  </q-item>
</template>

<script>
export default {
  name: "DiscussionItem",
  props: {
    postData: Object
  },
  methods:{
    goToPost(){
      this.$router.replace({name:"Post"})
    }
  },
  data() {
    return {}
  }
}
</script>

<style scoped>

</style>
