<template>
  <div id="result-page">
    <div class="row">
      <img
        class="col-4"
        src="@/assets/result_search_girl.jpeg"
        style="margin-left: 150px"
      />
      <div id="result-content" class="col-4">
        <div class="text-blue-4 text-h2" style="margin-top: 100px">
          <b>你的测试结果为</b>
        </div>
        <div>
          <div>
            <span class="text-h4">
              {{ hollandCode.key1 }}
              <q-badge :label="resultDict[hollandCode.key1].tag"></q-badge>
            </span>
            <span>
              {{ resultDict[hollandCode.key1].content }}
            </span>
          </div>
          <div>
            <span class="text-h4">
              {{ hollandCode.key2 }}
              <q-badge :label="resultDict[hollandCode.key2].tag"></q-badge>
            </span>
            <span>
              {{ resultDict[hollandCode.key2].content }}
            </span>
          </div>
          <div>
            <span class="text-h4">
              {{ hollandCode.key3 }}
              <q-badge :label="resultDict[hollandCode.key3].tag"></q-badge>
            </span>
            <span>
              {{ resultDict[hollandCode.key3].content }}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div id="recommend-area">
      <div class="q-ma-md text-h5 text-bold">
        推荐职业：
        <q-btn flat class="text-white bg-blue text-bold" @click="seeAll"
          >查看所有</q-btn
        >
      </div>
      <q-virtual-scroll :items="recommendJobs" virtual-scroll-horizontal style="height:300px;">
        <template v-slot="{ item, index }">
          <div
            :key="index"
            class="q-ma-md self-center recommend-item"
            @click="gotoJob(item.jobCat)"
          >
            <q-img :src="item.bigJobImg" spinner-color="blue" height="100%" />
            <div style="text-align: center">
              <b>{{ item.jobName }}</b>
            </div>
            <div>
              {{ item.jobDesc }}
            </div>
          </div>
        </template>
      </q-virtual-scroll>
    </div>
    <div id="recommand-all-area" v-if="ifSeeAll">
      <div
        v-for="(item, index) in recommendJobs"
        :key="index"
        class="q-ma-md self-center recommend-item"
        @click="gotoJob(item.jobCat)"
        style="margin-left: 100px; margin-right: 100px"
      >
        <div class="row">
          <div class="col-2 q-ma-sm q-pb-md">
            <q-img
              :src="item.bigJobImg"
              spinner-color="blue"
              height="100%"
              width="100%"
            />
            <div style="text-align: center">
              <b>{{ item.jobName }}</b>
            </div>
          </div>
          <div class="col-8" style="margin-top: 50px">
            <div>职位描述:{{ item.jobDesc }}</div>
            <div>职位工作:{{ item.jobWorks }}</div>
            <div>
              职业分类: <q-badge> {{ item.subject1 }} </q-badge>
              <q-badge> {{ item.subject2 }} </q-badge>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    gotoJob(jobCat) {
      this.$router.push({name:'Industry',query:{jobCat: jobCat}})
    },
    seeAll() {
      this.ifSeeAll = true;
      this.$nextTick(() => {
        let el = document.getElementById("recommand-all-area");
        if (!el) {
          return;
        }
        window.scrollTo({ behavior: "smooth", top: el.offsetTop });
      });
    },
  },
  mounted: async function () {
    this.hollandCode.key1 = this.$route.query.key1 ?? this.hollandCode.key1;
    this.hollandCode.key2 = this.$route.query.key2 ?? this.hollandCode.key2;
    this.hollandCode.key3 = this.$route.query.key3 ?? this.hollandCode.key3;
    let res = await this.$api.bigjob.jobs(
      this.hollandCode.key1,
      this.hollandCode.key2,
      this.hollandCode.key3
    );
    this.recommendJobs = res.data.data;
  },
  data() {
    return {
      ifSeeAll: false,
      hollandCode: {
        key1: "I",
        key2: "R",
        key3: "A",
      },
      resultDict: {
        R: {
          tag: "工/实做",
          content:
            "以具体实用的能力解决工作及其他方面的问题。自觉有机械和动作的能力，但可能较为缺乏人际关系或社交的兴趣。",
        },
        I: {
          tag: "理/研究",
          content:
            "喜欢以观察、分析、推理等方式，找出事物的原理原则，并运用语言、符号、数字或概念来解决问题。也喜欢花时间去钻研感兴趣的议题，以及提出新的观念与构想。偏好从事抽象思考或探索性质的工作。",
        },
        A: {
          tag: "文/艺术",
          content:
            "喜欢用文字、声音、影像、色彩与动作等方式，进行艺术相关的创作活动，也喜欢依循个人的审美观或灵感，进行创意性的表达",
        },
        S: {
          tag: "人/社会",
          content:
            "喜欢与人群互动，重视人的需求感受、看重人际间的和谐 。喜欢运用自身的知识教导他人，聆听别人的困难，主动提供关怀和协助。偏好从事与人相处或帮助他人的工作。",
        },
        E: {
          tag: "商/企业",
          content:
            "喜欢领导或游说他人，以达到个人或团体的目标。对于获得他人的注意、在团体中得到权力，或是改善现状有高度的兴趣。偏好从事影响他人或社会的工作。",
        },
        C: {
          tag: "事/事务",
          content:
            "喜欢执行具有明确标准与规则的任务。对于运用数字或机器进行计算、查核、排程、记录，或联系等工作有高度的兴趣，也比较喜欢从事处理精确事务及规律性高的工作。",
        },
      },
      recommendJobs: [],
    };
  },
};
</script>

<style scoped>
#result-page {
  background: #f6f6f6;
}
.recommend-item {
  cursor: pointer;
  border: 1px #f6f6f6 solid;
  z-index: 1;
}
.recommend-item:hover {
  color: #218be6;
  border: 1px #218be6 solid;
}
</style>
