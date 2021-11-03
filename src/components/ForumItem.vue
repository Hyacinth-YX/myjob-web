<template>
  <q-item>
    <q-item-section avatar>
      <q-avatar>
        <img src="https://cdn.quasar.dev/img/boy-avatar.png">
      </q-avatar>
      <a class="text-blue cursor-pointer q-ml-xs">{{body.writer}}</a>
    </q-item-section>

    <q-item-section>
      <q-item-label class="text-body1">
        {{ body.body }}
      </q-item-label>
    </q-item-section>

    <q-item-section side top >
      <q-item-label caption>5 min ago</q-item-label>
      <span><q-btn icon="thumb_up_alt" dense flat size="sm">123</q-btn><q-btn icon="thumb_down_alt" dense flat size="sm"> 23</q-btn></span>
    </q-item-section>
  </q-item>
<!--  <div>-->
<!--    <div class="row">-->
<!--      <div class="col-4 row_col1">-->
<!--        <img :src="require('@/assets/writer.jpeg')" class="profile"/>-->
<!--      </div>-->
<!--      <div class="col-8 row_col1">-->
<!--        {{ body.body }}-->
<!--      </div>-->
<!--    </div>-->

<!--    <div class="row">-->
<!--      <div class="col-4 row_col2" style="text-align:center">-->
<!--        {{ body.writer }}-->
<!--      </div>-->
<!--      <div class="col-8 row_col2" style="text-align:right">-->
<!--        <q-btn-->
<!--            id="1"-->
<!--            icon="thumb_up_alt"-->
<!--            rounded flat-->
<!--            color="black"-->
<!--            @click="thumb_up"-->
<!--        ></q-btn>-->
<!--        <q-btn-->
<!--            icon="thumb_down_alt"-->
<!--            rounded flat-->
<!--            color="black"-->
<!--            @click="refresh"-->
<!--        ></q-btn>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
</template>


<script>
export default {
  name: 'ForumItem',
  props: {
    body: Object
  }
}
</script>

<style>

</style>
