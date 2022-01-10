<template>
  <div class="home">
    <!--    背景-->
    <div class="video-container">
      <video autoplay loop muted>
        <source src="@/assets/backgroundVideo.mp4" type="video/mp4" />
        浏览器不支持 video 标签，建议升级浏览器。
      </video>
    </div>
    <!--      标题和logo-->
    <div class="title-container text-white">
      <h1 class="en-art-font">My Job</h1>
      <h2 class="en-art-font2">Information Platform</h2>
    </div>
    <!--      搜索框部分-->
    <div class="q-pa-md" style="width: 70%; margin: 0 auto">
      <div style="height: 300px"></div>
      <q-input
        bottom-slots
        label-color="grey-8"
        bg-color="white"
        filled
        dark
        outlined
        clearable
        debounce="500"
        v-model="searchText"
        label="搜索行业/岗位"
        counter
        maxlength="40"
      >
        <template v-slot:before>
          <q-icon name="flight_takeoff" />
        </template>
        <template v-slot:after>
          <q-btn label="Search" icon="search" color="grey-9" size="lg"></q-btn>
        </template>
        <template v-slot:hint> 热门搜索 </template>
      </q-input>
    </div>

    <!--    排行榜-->
    <div
      class="rank-container q-ma-lg row q-mb-lg shadow-3"
      style="background: transparent"
    >
      <!--排行榜框-->
      <div class="rank-container col">
        <q-select
          filled
          rounded
          v-model="rankSelect"
          label="排行依据"
          dense
          :options="rankOptions"
          class="q-ma-sm"
        />
        <q-scroll-area style="height: 300px">
          <q-list bordered separator>
            <q-item
              clickable
              v-ripple
              v-for="item in industry"
              @click="goToIndustry(item.jobCat)"
              @mouseover="changeJobCat(item.jobCat)"
              :key="item.id"
            >
              <q-item-section>
                <q-item-label>{{ item.jobName }}</q-item-label>
                <q-item-label caption
                  >年薪：{{ item.salary | number }}</q-item-label
                >
              </q-item-section>
            </q-item>
          </q-list>
        </q-scroll-area>
      </div>
      <!--行业信息框-平均薪资趋势-->
      <div class="rank-container q-pa-md q-ml-sm col">
        <p><strong>平均薪资趋势</strong></p>
        <div id="trend-container" style="height: 300px"></div>
      </div>
      <!--行业信息框-薪资分布直方图-->
      <div class="rank-container q-pa-md q-ml-sm col">
        <p><strong>相关信息</strong></p>
        <q-img
          :src="bigjobData.bigJobImg"
          height="70%"
          width="70%"
          spinner-color="white"
          style="margin-left: 15%"
        />
        <div style="text-align: center" class="text-blue text-bold">
          {{ bigjobData.jobName }}
        </div>
        <div style="text-align: left; text-indent: 2em">
          {{ bigjobData.jobDesc }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Line } from "@antv/g2plot";

export default {
  name: "Home",
  components: {},
  data() {
    return {
      jobCat: "2012003002",
      searchText: "",
      industry: [],
      rankSelect: "按行业薪资",
      rankOptions: ["按行业薪资", "按行业热度"],
      lineGraph: null,
      lineData: null,
      bigjobData: {},
      isLogin: false,
    };
  },
  methods: {
    goToIndustry(jobCat) {
      this.$router.push({ name: "Industry", query: { jobCat: jobCat } });
    },
    changeJobCat(jobCat) {
      this.jobCat = jobCat;
    },
  },
  watch: {
    jobCat: async function (newVal) {
      if (this.lineGraph != null) {
        let res = await this.$api.bigjob.bigjobSalaryTrend(newVal);
        this.lineData = res.data.data;
        const data = this.lineData;
        this.lineGraph.changeData(data);

        res = await this.$api.bigjob.getBigJobDetail(this.jobCat);
        this.bigjobData = res.data.data;
      }
    },
  },
  mounted: async function () {
    let res = await this.$api.user.isLogin();
    this.isLogin = res.data.data.result;

    res = await this.$api.bigjob.allBigJobs();
    this.industry = res.data.data;
    this.jobCat = this.industry[0].jobCat;
    res = await this.$api.bigjob.bigjobSalaryTrend(this.jobCat);
    this.lineData = res.data.data;

    res = await this.$api.bigjob.getBigJobDetail(this.jobCat);
    this.bigjobData = res.data.data;

    const data = this.lineData;

    this.lineGraph = new Line("trend-container", {
      data,
      autoFit: true,
      padding: "auto",
      xField: "Date",
      yField: "scales",
      yAxis: {
        min: 100000,
      },
      annotations: [
        {
          type: "regionFilter",
          start: ["min", "median"],
          end: ["max", "0"],
          color: "#F4664A",
        },
        {
          type: "text",
          position: ["min", "median"],
          content: "中位数",
          offsetY: -4,
          style: {
            textBaseline: "bottom",
          },
        },
        {
          type: "line",
          start: ["min", "median"],
          end: ["max", "median"],
          style: {
            stroke: "#F4664A",
            lineDash: [2, 2],
          },
        },
      ],
    });
    this.lineGraph.render();
  },
};
</script>

<style scoped>
.rank-container {
  height: 400px;
  position: relative;
  background: white;
  border-radius: 30px;
}

.video-container video {
  z-index: 0;
  top: 0;
  position: absolute;
  width: 100%;
}

.title-container {
  z-index: 1;
  position: absolute;
  left: 10%;
}

.en-art-font {
  font-family: "Impact", fantasy;
}

.en-art-font2 {
  font-family: "Bradley Hand", cursive;
}
</style>
