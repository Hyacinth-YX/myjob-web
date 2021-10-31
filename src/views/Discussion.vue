<template background="require('@/assets/discussion.jpeg')">
  <div id="bcimge">
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


    <div v-for="post of posts" :key="post.id" class="posttitle">
      
      <a href="post" class="atitle">{{post["title"]}}</a>
      <a href="post" class="awriter" @mouseover="d" style="float:right">{{post["writer"]}}</a>
      <font size="5" face="arial" color="black">
      <p>{{post["body"]}}</p>
      </font>
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
      example: "hahahahahha",
      exampleList: { aa: "hahah", bb: "hsdkl", cc: "sdfsdfdsf" },
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
  width: 800px;
  /* this should be the wrapper minus sidebar and padding on both */
  background-color:grey;
  padding: 10px;
  text-align: justify;
  margin: 0px 100px 0px 200px;
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
  background-color:grey;
  padding: 10px;
  text-align: justify;
  margin: 0px 100px 0px 200px;
  color: black;
  font-size: 30px;
  border-width:1px 1px 0px 1px;
  border-style: solid;
}


</style>
