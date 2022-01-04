<template>
  <q-page>
    <!--底层页面-->
    <particles-bg :bg="true" type="cobweb" num="100"></particles-bg>
    <div class="row">
      <!--帖子部分-->
      <div class="col-8 q-ml-xl">
        <!--标题行-->
        <div>
          <a class="text-h4">{{ industrylist[0].name }}</a>
          <q-btn
            :label="personalStatus.star ? '已关注' : '+关注'"
            color="red"
            size="sm"
            rounded
            class="q-ml-sm"
            @click="changeStarStatus"
            v-if="showStarBtn"
          ></q-btn>
        </div>
        <!--信息行-->
        <div class="text-bold text-body1">
          当前行业薪资排名{{ industrylist[0]["rank"] }}，平均薪资{{
            industrylist[0]["average"]
          }}
        </div>
        <!--帖子行-->
        <q-list bordered separator>
          <discussion-item
            v-for="post of posts"
            :key="post.id"
            :post-data="post"
            class="q-pa-sm discussion-item-class"
          ></discussion-item>
        </q-list>
        <!--发帖行-->
        <div>
          <q-input
            label-color="grey-8"
            bg-color="white"
            outlined
            clearable
            debounce="500"
            class="q-mb-sm"
            v-model="sendPostData.title"
            label="标题"
            counter
            maxlength="20"
          />
          <q-input
            label-color="grey-8"
            bg-color="white"
            outlined
            debounce="500"
            class="q-mb-sm"
            v-model="sendPostData.text"
            label="评论"
            counter
            type="textarea"
          />
          <q-btn
            label="发个帖子"
            color="blue"
            style="float: right"
            @click="sendPost"
          ></q-btn>
        </div>
        <!--页码行-->
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
      <!--排行榜-->
      <div class="col-3 q-ma-sm">
        <heat-rank />
      </div>
    </div>

    <!--粘贴按钮-->
    <div>
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
          @mouseover="overToChangeTextStatus('share')"
          v-if="!buttonTextStatus.share"
        ></q-btn>
        <q-btn
          label="分享"
          rounded
          color="grey"
          @mouseout="overToChangeTextStatus('share')"
          v-else
        ></q-btn>
      </q-page-sticky>
    </div>
  </q-page>
</template>

<script>
import HeatRank from "../components/HeatRank.vue";
import DiscussionItem from "../components/DiscussionItem";
import { ParticlesBg } from "particles-bg-vue";

export default {
  components: {
    DiscussionItem,
    HeatRank,
    ParticlesBg,
  },
  data() {
    return {
      jobCat: "2012003002",
      showStarBtn: true,
      personalStatus: {},
      sendPostData: {
        title: "",
        text: "",
      },
      buttonTextStatus: {
        upward: false,
        addpost: false,
        refresh: false,
        share: false,
      },
      current: 6,
      right: false,
      industrylist: [
        { name: "计算机/网络/技术类", rank: 1, average: 10000, nposts: 50 },
        { name: "销售类", rank: 2, average: 9999, nposts: 40 },
      ],
      posts: [
        {
          title: "post1",
          body: "These are the first 20 words of post1 These are the first 20 words of post1",
          writer: "one",
        },
        {
          title: "post2",
          body: "These are the first 20 words of post2 These are the first 20 words of post2",
          writer: "two",
        },
        {
          title: "post3",
          body: "These are the first 20 words of post3 These are the first 20 words of post3",
          writer: "three",
        },
        {
          title: "post4",
          body: "These are the first 20 words of post4 These are the first 20 words of post4",
          writer: "three",
        },
        {
          title: "post5",
          body: "These are the first 20 words of post5 These are the first 20 words of post5",
          writer: "three",
        },
      ],
    };
  },
  methods: {
    overToChangeTextStatus(buttonName) {
      this.buttonTextStatus[buttonName] = !this.buttonTextStatus[buttonName];
    },
    sendPost: function () {
      this.$q.notify({
        message: "请先登录!",
        color: "red",
        position: "top-right",
        icon: "announcement",
      });
      this.$router.replace({ name: "Login" });
    },
    /*回到顶部*/
    upward: function () {
      document.body.scrollTop = document.documentElement.scrollTop = 0;
    },
    /*发帖子 */
    add_post: function () {
      document.body.scrollTop = document.documentElement.scrollTop = 9999;
    },
    /* 刷新 */
    refresh: function () {
      location.reload();
    },
    /*关注成功*/
    changeStarStatus: function () {
      this.showStarBtn = false;
      if (this.personalStatus.star) {
        this.$q.notify({
          message: "已经取消关注555~",
          color: "blue",
          position: "top-right",
          icon: "announcement",
        });
        this.personalStatus.star = false;
      } else {
        this.$q.notify({
          message: "关注成功!",
          color: "green",
          position: "top-right",
          icon: "announcement",
        });
        this.personalStatus.star = true;
      }
      this.$nextTick().then(() => {
        this.showStarBtn = true;
      });
    },
    goToPost() {
      this.$router.replace({ name: "Post" });
    },
  },
};
</script>

<style scoped>
.discussion-item-class{
  background: #F6F6F6;
}
</style>
