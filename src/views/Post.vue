<template>
  <div>
    <div class="row" >
    <div class="col">
    </div>
    <div class="col-7" style="padding:20px">
      <div style="background:white">
        <font size="5" face="arial" color="black" >
        {{posttitle}}
        </font>
      </div>
    </div>
      
      <div class="col-4">
      </div>

    </div>
    
   
    <div v-for="body of postbody" :key="body.id"> 
      <forumItem :body="body"/>
    </div>

    <div class="row">
        <div class="col">
        </div>
        <div class="col-7">
            <q-input label-color="grey-8"  bg-color="white" filled  outlined clearable debounce="500"
                v-model="sendCommentData.text" label="评论" counter type="textarea" >
            </q-input>
            <q-btn label="submit" style="float:right" @click="sendPost" ></q-btn>

        </div>
        <div class="col-4">
        </div>

    </div>

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
        icon="person"
        rounded flat
        color="white"
        @click="onlyperson"
      ></q-btn>
        
        <q-btn
        icon="message"
        rounded flat
        color="white"
        @click="reply"
      ></q-btn>
      <q-btn
        icon="stars"
        rounded flat
        color="white"
        @click="stars"
      ></q-btn>

        <q-btn
        icon="refresh"
        rounded flat
        color="white"
        @click="refresh"
        @mouseover="refresh_on"
      ></q-btn>
         <q-btn
        icon="ios_share"
        rounded flat
        color="white"
        @click="share"
      ></q-btn>
       
      </q-toolbar>
    </q-footer>

    <heatrank/>
  </div>
</template>

<script>
import forumItem from "../components/forumItem"
import heatrank from "../components/heatrank"
export default {
  name: "Post",
  components:{
    forumItem,
    heatrank
  },
  data () {
    return {
      right: false,
      sendCommentData:{
            writer:"",
            text:"",
        },
      posttitle:'上海财经大学毕业生待遇仅次于清华',
      postbody:[
        {writer:"张三",body:"答主本硕均毕业于上海财经大学，根据最新的就业报告，上财毕业生的年收入排全国第二，仅次于清华"},
        {writer:"李四",body:"上财yyds"},
        {writer:"王五",body:"上财yyds"},
        {writer:"赵六",body:"上财yyds"},
        {writer:"马七",body:"上财yyds"},
      ],
    };
    
  },
   methods: {
    /*回到顶部*/
     upward:function(){
       document.body.scrollTop = document.documentElement.scrollTop = 0;
     },

     /*只看楼主*/
     onlyperson:function(){
     },

     /* 评论 */
    reply:function(){
      document.body.scrollTop = document.documentElement.scrollTop = 9999;
    },
    /* 收藏 */  
     stars:function(){

     },
 
     /* 刷新 */
    refresh: function () {
      location.reload();
    },

    refresh_on:function(){
       
    },  
    /* 分享 */ 
    share:function(){

    },

    /*点赞 */
    thumb_up:function(){
     document.getElementById("1").color="red";
    },

    d:function(){
      
    },
    goToPost(){
      this.$router.replace({name:"Post"});
    },
  },
  
}
</script>



<style>
.heatrank{
  width:300px;
  background: #FFFFFF;
  }
a.heatrank{
  text-decoration:none;
}

a:hover.heatrank{
  color: #335EB6;
  text-decoration:underline;
}


</style>
