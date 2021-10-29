<template>
  <div class="home">
    <!--      标题和logo-->
    <div>

    </div>
    <!--      搜索框部分-->
    <div class="q-ma-lg">

      <q-input bottom-slots v-model="searchText" label="搜索行业/岗位" counter maxlength="12">
        <template v-slot:before>
          <q-icon name="flight_takeoff"/>
        </template>

        <template v-slot:append>
          <q-icon v-if="searchText !== ''" name="close" @click="searchText = ''" class="cursor-pointer"/>
          <q-icon name="search"/>
        </template>

        <template v-slot:hint>
          搜索点什么吧
        </template>
      </q-input>
    </div>

    <!--    排行榜-->
    <div class="rank-container">
      <!--      排行榜框-->
      <div class="rank-container" style="width: 30%; float: left">
        <q-list bordered separator>
          <q-item clickable v-ripple >
            <q-item-section>Single line item</q-item-section>
          </q-item>


        </q-list>
      </div>
      <!--      行业信息框-->
      <div class="rank-container" style="width: 30%; float: left"></div>

    </div>


  </div>
</template>

<script>

export default {
  name: 'Home',
  components: {},
  data() {
    return {
      searchText: "",
      industry: [
        '计算机/网络/技术类', '销售类', '经营管理类',
        '电子/电器/通信技术类', '市场/公关/媒介类', '财务/审计/统计类',
        '建筑/房地产/装饰装修/物业管理类', '美术/设计/创意类', '机械/仪器仪表类',
      ]

    }
  }
}
</script>

<style scoped>
.rank-container {
  border: 1px solid;
  min-height: 400px;
}
</style>
