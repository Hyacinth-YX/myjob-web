<template>
      <q-page-container style="margin-top:50px">
        
        <q-page padding >
          <div class="heatrank">热度榜</div> 
          <div v-for="rank of ranks" :key="rank.id" class="heatrank">
          <a @click="goToPost" class="heatrank">
            {{rank.rank}}.{{rank.title}}
          </a>
          <div>累计阅读：{{rank.heat}}</div>
          </div>
        </q-page>
      </q-page-container>
</template>

<style>
.heatrank{
  width:300px;
  background: #FFFFFF;
  }
</style>

<script>
export default {
  name: 'heatrank',
  data() {
    return{
      ranks:[{rank:1,title:"上海财经大学毕业生待遇仅次于清华",heat:9999},
      {rank:2,title:"上财校友入职阿里经验分享",heat:9998},
      {rank:3,title:"上财校友入职字节经验分享",heat:9997},
      {rank:4,title:"上财校友入职腾讯经验分享",heat:9996},
      {rank:5,title:"上财校友入职美团经验分享",heat:9995},
      {rank:6,title:"上财校友入职拼多多经验分享",heat:9994},
      {rank:7,title:"上财校友加入私募基金一年的变化",heat:9993},
      {rank:8,title:"上财校友创业有感",heat:9992},
      {rank:9,title:"上财校友校友会",heat:9991},],
    }
  },
  methods:{
    goToPost(){
      this.$router.replace({name:"Post"});
    },
  }
}
</script>