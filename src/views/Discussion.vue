<template>
  <q-layout view="hHh lpR fFf">
      <div class="row">
        <div class="col">
        </div>   
        <div class="col-6" id="row_col3">
            <div class="title">
            {{industrylist[0].name}}
            <q-btn
            label="+关注"
                flat
                text-color="red"
                @click="successfully"
            ></q-btn>
            <div>
        <font size="5" face="arial" color="black">
          当前行业薪资排名{{ industrylist[0]["rank"] }}，平均薪资{{
            industrylist[0]["average"]
          }}
        </font>
        </div>
        </div>
        </div>
        <div class="col-4">
        </div>
      </div>
    
    <div v-for="post of posts" :key="post.id" class="posttitle">
     <div class="row">
         <div class="col">
         </div>
         <div class="col-6"  id="row_col3">
            <a @click="goToPost" class="atitle">{{post["title"]}}</a>
            <font size="5" face="arial" color="black">
            <p>{{post["body"]}}</p>
            </font>
         </div>
         <div class=col-4>
         </div>
     </div>
    </div>

    

    <div class="q-pa-lg flex flex-center">
    <q-pagination
      v-model="current"
      color="purple"
      :max="10"
      :max-pages="6"
      boundary-numbers
    />
  </div>

    <div class="row">
        <div class="col">
        </div>
        <div class="col-6">
            <q-input bottom-slots label-color="grey-8" bg-color="white" filled dark outlined clearable debounce="500"
                v-model="Text" label="标题" counter maxlength="20">
            </q-input>

        </div>
        <div class="col-4">
        </div>

    </div>
    

    <div class="row">
        <div class="col">
        </div>
        <div class="col-6">
            <q-input bottom-slots label-color="grey-8" bg-color="white" filled dark outlined clearable debounce="500"
                v-model="Text" label="正文" counter maxlength="200">
            </q-input>

        </div>
        <div class="col-4">
        </div>

    </div>

    <q-drawer show-if-above v-model="right" side="right" bordered>
      <!-- drawer content -->
      <heatrank/>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
        </q-toolbar-title>

        <q-btn
        icon="expand_less"
        rounded flat
        color="white"
        @click="upward"
      ></q-btn>

        <q-btn
        icon="add_circle_outline"
        rounded flat
        color="white"
        @click="add_post"
      ></q-btn>
      
      <q-btn
        icon="refresh"
        rounded flat
        color="white"
        @click="refresh"
      ></q-btn>

      <q-btn
        icon="ios_share"
        rounded flat
        color="white"
        @click="share"
      ></q-btn>
      
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
import heatrank from '../components/heatrank.vue';
export default {
   components:{
    heatrank
  },
  data () {
    return {
      current: 6,
      right: false,
      industrylist: [
        { name: "计算机/网络/技术类", rank: 1, average: 10000, nposts: 50 },
        { name: "销售类", rank: 2, average: 9999, nposts: 40 },
      ],
      posts: [{ title: "post1", body: "These are the first 20 words of post1" ,writer:"one"},
      { title: "post2", body: "These are the first 20 words of post2",writer:"two" },
      { title: "post3", body: "These are the first 20 words of post3",writer:"three"}],
    }
  },
  methods:{
      /*回到顶部*/
     upward:function(){
       document.body.scrollTop = document.documentElement.scrollTop = 0;
     },
     /*发帖子 */
      add_post:function(){
         document.body.scrollTop = document.documentElement.scrollTop = 9999;
      },
      /* 刷新 */
    refresh: function () {
      location.reload();
    },
    /* 分享 */ 
    share:function(){

    },
    /*关注成功*/
    successfully:function(){
     alert("关注成功");
    },
    goToPost(){
      this.$router.replace({name:"Post"});
    },

  }
}
</script>


<style>
.title {
  float: center;
  /* also float left so it goes next to the sidebar */
  /* this should be the wrapper minus sidebar and padding on both */
  background-color:#F5F6F9;
  padding: 5px;
  margin: 0px 80px 0px 0px;
  color: black;
  font-size: 40px;
}

/*links*/

a.atitle{
  font-size: 30px; 
  color:blue;
  text-decoration:none;
}
a:hover.atitle{
  text-decoration:underline;
}
a:visited.atitle{
  color: purple;
}
#row_col3{
  background:#F5F6F9;
  border-width:1px 1px 0px 1px;
  border-style: solid;
  padding: 20px;
}


</style>