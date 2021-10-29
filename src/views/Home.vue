<template>
  <div class="home">
    <!--      标题和logo-->
    <div>

    </div>
    <!--      搜索框部分-->
    <div class="q-ma-lg">

      <q-input bottom-slots v-model="text" label="Label" counter maxlength="12" :dense="dense">
        <template v-slot:before>
          <q-icon name="flight_takeoff" />
        </template>

        <template v-slot:append>
          <q-icon v-if="text !== ''" name="close" @click="text = ''" class="cursor-pointer" />
          <q-icon name="search" />
        </template>

        <template v-slot:hint>
          Field hint
        </template>
      </q-input>
    </div>

<!--    排行榜-->
    <div>

    </div>


  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {

  },
  data(){
    return{

    }
  }
}
</script>
