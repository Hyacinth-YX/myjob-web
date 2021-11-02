<template>
  <q-page>
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
            <a @click="goToPost" class="atitle cursor-pointer">{{post["title"]}}</a>
            <font size="5" face="arial" color="black">
            <p>{{post["body"]}}</p>
            </font>
         </div>
         <div class=col-4>
         </div>
     </div>
    </div>
     <div class="row">
        <div class="col">
        </div>   
        <div class="col-6" id="row_col3">
            <div class="q-pa-lg flex flex-center">
            <q-pagination
            v-model="current"
            color="blue"
            :max="10"
            :max-pages="6"
            boundary-numbers
            />
            </div>
        </div>
         <div class=col-4>
         </div>
  </div>

    <div class="row">
        <div class="col">
        </div>
        <div class="col-6">
            <q-input  bottom-slots label-color="grey-8" bg-color="white" filled outlined clearable debounce="500"
                v-model="sendPostData.title" label="标题" counter maxlength="20">
            </q-input>

        </div>
        <div class="col-4">
        </div>

    </div>
    

    <div class="row">
        <div class="col">
        </div>
        <div class="col-6">
            <q-input label-color="grey-8"  bg-color="white" filled  outlined clearable debounce="500"
                v-model="sendPostData.text" label="正文" counter type="textarea" >
            </q-input>
            <q-btn label="submit" style="float:right" @click="sendPost" ></q-btn>

        </div>
        <div class="col-4">
        </div>

    </div>

    <heatrank />
    <q-page-sticky position="top-right" :offset="[35, 250]">
      <q-btn
        icon="expand_less"
        rounded
        color="blue"
        @click="upward"
        @mouseover="overToChangeTextStatus('upward')"
        v-if="!buttonTextStatus.upward"
      ></q-btn>
      <q-btn
        label="顶部"
        rounded 
        color="grey"
        @click="upward"
        @mouseout="overToChangeTextStatus('upward')"
        v-else
      ></q-btn>
    </q-page-sticky>

    <q-page-sticky position="top-right" :offset="[35, 300]">
      <q-btn
        icon="add_circle_outline"
        rounded
        color="blue"
        @click="add_post"
        @mouseover="overToChangeTextStatus('addpost')"
        v-if="!buttonTextStatus.addpost"
      ></q-btn>
      <q-btn
        label="发帖"
        rounded
        color="grey"
        @click="add_post"
        @mouseout="overToChangeTextStatus('addpost')"
        v-else
      ></q-btn>
    </q-page-sticky>

     <q-page-sticky position="top-right" :offset="[35, 350]">
      <q-btn
        icon="refresh"
        rounded
        color="blue"
        @click="refresh"
        @mouseover="overToChangeTextStatus('refresh')"
        v-if="!buttonTextStatus.refresh"
      ></q-btn>
      <q-btn
        label="刷新"
        rounded
        color="grey"
        @click="refresh"
        @mouseout="overToChangeTextStatus('refresh')"
        v-else
      ></q-btn>
    </q-page-sticky>

    <q-page-sticky position="top-right" :offset="[35, 400]">
      <q-btn
        icon="ios_share"
        rounded
        color="blue"
        @click="share"
        @mouseover="overToChangeTextStatus('share')"
        v-if="!buttonTextStatus.share"
      ></q-btn>
      <q-btn
        label="分享"
        rounded
        color="grey"
        @click="share"
        @mouseout="overToChangeTextStatus('share')"
        v-else
      ></q-btn>
    </q-page-sticky>
    

  </q-page>
</template>

<script>
import heatrank from '../components/heatrank.vue';
export default {
   components:{
    heatrank
  },
  data () {
    return {
        sendPostData:{
            title:"",
            text:"",
        },
        buttonTextStatus:{
            upward:false,
            addpost:false,
            refresh:false,
            share:false,

        },
      current: 6,
      right: false,
      industrylist: [
        { name: "计算机/网络/技术类", rank: 1, average: 10000, nposts: 50 },
        { name: "销售类", rank: 2, average: 9999, nposts: 40 },
      ],
      posts: [{ title: "post1", body: "These are the first 20 words of post1 These are the first 20 words of post1" ,writer:"one"},
      { title: "post2", body: "These are the first 20 words of post2 These are the first 20 words of post2",writer:"two" },
      { title: "post3", body: "These are the first 20 words of post3 These are the first 20 words of post3",writer:"three"},
      {title: "post4", body: "These are the first 20 words of post4 These are the first 20 words of post4",writer:"three"},
      {title: "post5", body: "These are the first 20 words of post5 These are the first 20 words of post5",writer:"three"}]
    }
  },
  methods:{
      overToChangeTextStatus(buttonName){
        this.buttonTextStatus[buttonName] = !this.buttonTextStatus[buttonName]
      },
      sendPost:function(){
        console.log(this.sendPostData.text)
      },
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
  border-color: #DCDFE5;
  padding: 20px;
}


</style>