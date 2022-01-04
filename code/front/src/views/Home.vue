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
              @click="goToIndustry"
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
      <div class="rank-container q-pa-md col">
        <p><strong>平均薪资趋势</strong></p>
        <div id="trend-container" style="height: 300px"></div>
      </div>
      <!--行业信息框-薪资分布直方图-->
      <div class="rank-container q-pa-md col">
        <p><strong>薪资分布直方图</strong></p>
        <div id="distribution-container" style="height: 300px"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { Line } from "@antv/g2plot";
// import { Column } from "@antv/g2plot";

export default {
  name: "Home",
  components: {},
  data() {
    return {
      jobCat: "2012003002",
      searchText: "",
      industry: [
        "计算机/网络/技术类",
        "销售类",
        "经营管理类",
        "电子/电器/通信技术类",
        "市场/公关/媒介类",
        "财务/审计/统计类",
        "建筑/房地产/装饰装修/物业管理类",
        "美术/设计/创意类",
        "机械/仪器仪表类",
      ],
      rankSelect: "按行业薪资",
      rankOptions: ["按行业薪资", "按行业热度"],
      lineGraph: null,
      lineData: null,
    };
  },
  methods: {
    goToIndustry() {
      this.$router.push({ name: "Industry" });
    },
  },
  mounted: async function () {
    let res = await this.$api.bigjob.allBigJobs();
    this.industry = res.data.data;
    this.jobCat = this.industry[0].jobCat;
    res = await this.$api.bigjob.bigjobSalaryTrend(this.jobCat);
    this.lineData = res.data.data;

    const data = this.lineData;

    this.lineGraph = new Line("trend-container", {
      data,
      autoFit: true,
      padding: "auto",
      xField: "Date",
      yField: "scales",
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

    // fetch(
    //   "https://gw.alipayobjects.com/os/bmw-prod/1d565782-dde4-4bb6-8946-ea6a38ccf184.json"
    // )
    //   .then((res) => res.json())
    //   .then((data) => {

    //   });

    // data = [
    //   {
    //     type: "0-1w",
    //     sales: 38,
    //   },
    //   {
    //     type: "1-2w",
    //     sales: 52,
    //   },
    //   {
    //     type: "2-3w",
    //     sales: 61,
    //   },
    //   {
    //     type: "3-4w",
    //     sales: 145,
    //   },
    //   {
    //     type: "4-5w",
    //     sales: 48,
    //   },
    //   {
    //     type: "5-6w",
    //     sales: 38,
    //   },
    //   {
    //     type: "6-7w",
    //     sales: 38,
    //   },
    //   {
    //     type: "7-8w",
    //     sales: 38,
    //   },
    // ];

    // const columnPlot = new Column("distribution-container", {
    //   data,
    //   xField: "type",
    //   yField: "sales",
    //   autoFit: true,
    //   columnWidthRatio: 0.95,
    //   label: {
    //     // 可手动配置 label 数据标签位置
    //     position: "middle", // 'top', 'bottom', 'middle',
    //     // 配置样式
    //     style: {
    //       fill: "#FFFFFF",
    //       opacity: 0.6,
    //     },
    //   },
    //   xAxis: {
    //     label: {
    //       autoHide: true,
    //       autoRotate: false,
    //     },
    //   },
    //   meta: {
    //     type: {
    //       alias: "类别",
    //     },
    //     sales: {
    //       alias: "销售额",
    //     },
    //   },
    // });

    // columnPlot.render();
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
