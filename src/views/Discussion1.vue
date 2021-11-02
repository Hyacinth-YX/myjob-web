<template>
  <div>
    <div class="title">
      {{ industrylist[0]["name"] }}
      <q-btn
        label="+关注"
        rounded flat
        color="white"
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

    <div class="q-pa-md">
    <div class="row">
    <div v-for="post of posts" :key="post.id" class="posttitle">
      
     <div class="col-5"><a href="post" class="atitle">{{post["title"]}}</a>
      <a href="post" class="awriter" @mouseover="d" style="float:right">{{post["writer"]}}</a>
      </div>
      <font size="5" face="arial" color="black">
      <p>{{post["body"]}}</p>
      </font>
    </div>
    </div>
    </div>
    
    
    <div class="q-pa-lg flex flex-center">
    <q-pagination
      v-model="current"
      color="black"
      :max="10"
      :max-pages="6"
      boundary-numbers
    ></q-pagination>
    </div>
   <div class="q-pa-md">
   <div class="row">
      <div class="col-9">.col-9</div>
      <div class="col-4">.col-4<br>Since 9 + 4 = 13 &gt; 12, this 4-column-wide div gets wrapped onto a new line as one contiguous unit.</div>
      <div class="col-5">.col-5<br>Subsequent columns continue along the new line.</div>
    </div>
   </div>
  </div>
  
</template>


<script>
export default {
  name: "Discussion",
  computed: {
    example2: function () {
      return this.example + "222";
    },
  },
  methods: {
    successfully: function () {
      alert("关注成功！");
    },
    d:function(){
      
    }
  },
  data() {
    return {
      industrylist: [
        { name: "计算机/网络/技术类", rank: 1, average: 10000, nposts: 50 },
        { name: "销售类", rank: 2, average: 9999, nposts: 40 },
      ],
      lksdjl: [11, 2, 3, 3, 3, 4, 4],
      posts: [{ title: "post1", body: "These are the first 20 words of post1" ,writer:"one"},
      { title: "post2", body: "These are the first 20 words of post2",writer:"two" },
      { title: "post3", body: "These are the first 20 words of post3",writer:"three"}],
      current:1,
    };
  },
  mounted: function () {},
};
</script>

<style scoped>
#bcimge {
  background: url("~@/assets/discussion.jpeg");
}
/* head unit*/
.title {
  float: center;
  /* also float left so it goes next to the sidebar */
  width: 1000px;
  /* this should be the wrapper minus sidebar and padding on both */
  background-color:#F5F6F9;
  padding: 10px;
  text-align: justify;
  margin: 0px 100px 0px 100px;
  color: black;
  font-size: 40px;
}

/*links*/

a.atitle{
  color:blue;
  text-decoration:none;
}
a:hover.atitle{
  text-decoration:underline;
}
a:visited.atitle{
  color: purple;
}

a:hover.awriter{
   
}
/*post_area*/
.posttitle{
  float: center;
  /* also float left so it goes next to the sidebar */
  width: 600px;
  /* this should be the wrapper minus sidebar and padding on both */
  background-color:#F5F6F9;
  padding: 10px;
  text-align: justify;
  margin: 0px 100px 0px 200px;
  color: black;
  font-size: 30px;
  border-width:1px 1px 0px 1px;
  border-style: solid;
}


</style>

<style lang="sass" scoped>
.row > div
  padding: 10px 15px
  background: rgba(86,61,124,.15)
  border: 1px solid rgba(86,61,124,.2)
.row + .row
  margin-top: 1rem
.row
  background: rgba(255,0,0,.1)
</style>
