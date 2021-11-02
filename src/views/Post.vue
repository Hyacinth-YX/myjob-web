<template>
  <div>
    <div class="row">
      <!--      帖子内容与楼层-->
      <div class="col-8  q-ml-xl" >
        <!--        标题-->
        <div style="background:#F5F6F9" class="q-pa-md">
          <div class="text-h5 text-bold" style="font-family: 'Microsoft Yahei', sans-serif">
            标题：{{ posttitle }}
          </div>
        </div>
        <div v-for="body of postbody" :key="body.id">
          <forumItem :body="body"/>
        </div>
      </div>
      <div class="col-3 q-ma-sm">
        <heatrank style="position: sticky"/>
      </div>
    </div>

    <div class="row">
      <div class="col-8 q-ml-xl q-mt-md">
        <q-input   label-color="grey-8" bg-color="white" color="grey-3" debounce="500"
                 v-model="sendCommentData.text"  label="评论" counter type="textarea" outlined>
        </q-input>
        <q-btn class="q-ma-md" label="回复本帖" color="blue" style="float:right" @click="sendPost"></q-btn>
      </div>
      <div class="col-3">
      </div>
    </div>

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
          icon="message"
          rounded
          color="blue"
          @click="comment"
          @mouseover="overToChangeTextStatus('comment')"
          v-if="!buttonTextStatus.comment"
      ></q-btn>
      <q-btn
          label="评论"
          rounded
          color="grey"
          @click="comment"
          @mouseout="overToChangeTextStatus('comment')"
          v-else
      ></q-btn>
    </q-page-sticky>

    <q-page-sticky position="top-right" :offset="[35, 350]">
      <q-btn
          icon="stars"
          rounded
          color="blue"
          @click="stars"
          @mouseover="overToChangeTextStatus('stars')"
          v-if="!buttonTextStatus.stars"
      ></q-btn>
      <q-btn
          label="收藏"
          rounded
          color="grey"
          @click="stars"
          @mouseout="overToChangeTextStatus('stars')"
          v-else
      ></q-btn>
    </q-page-sticky>

    <q-page-sticky position="top-right" :offset="[35, 400]">
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

    <q-page-sticky position="top-right" :offset="[35, 450]">
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

  </div>
</template>

<script>
import forumItem from "../components/forumItem"
import heatrank from "../components/heatrank"

export default {
  name: "Post",
  components: {
    forumItem,
    heatrank
  },
  data() {
    return {
      right: false,
      sendCommentData: {
        writer: "",
        text: "",
      },

      buttonTextStatus: {
        upward: false,
        comment: false,
        stars: false,
        refresh: false,
        share: false,

      },

      posttitle: '上海财经大学毕业生待遇仅次于清华',
      postbody: [
        {writer: "张三", body: "答主本硕均毕业于上海财经大学，根据最新的就业报告，上财毕业生的年收入排全国第二，仅次于清华"},
        {writer: "李四", body: "上财yyds"},
        {writer: "王五", body: "上财yyds"},
        {writer: "赵六", body: "上财yyds"},
        {writer: "马七", body: "上财yyds"},
      ],
    };

  },
  methods: {
    /*回到顶部*/
    upward: function () {
      document.body.scrollTop = document.documentElement.scrollTop = 0;
    },

    /* 评论 */
    comment: function () {
      document.body.scrollTop = document.documentElement.scrollTop = 9999;
    },
    /* 收藏 */
    stars: function () {

    },

    /* 刷新 */
    refresh: function () {
      location.reload();
    },

    refresh_on: function () {

    },
    /* 分享 */
    share: function () {

    },

    /*点赞 */
    thumb_up: function () {
      document.getElementById("1").color = "red";
    },

    d: function () {

    },
    goToPost() {
      this.$router.replace({name: "Post"});
    },
    overToChangeTextStatus(buttonName) {
      this.buttonTextStatus[buttonName] = !this.buttonTextStatus[buttonName]
    },
  },

}
</script>


<style>
.heatrank {
  width: 300px;
  background: #FFFFFF;
}

a.heatrank {
  text-decoration: none;
}

a:hover.heatrank {
  color: #335EB6;
  text-decoration: underline;
}


</style>
