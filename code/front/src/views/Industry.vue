<template>
  <div>
    <!--    头部信息-->
    <div class="info-container row" style="min-height: 300px">
      <!--      信息框-->
      <div class="info-block col-4 q-pa-md">
        <!--        标题-->
        <div class="text-h5 text-bold">{{ industryName }}</div>
        <!--        描述-->
        <div class="text-caption q-mt-md" style="text-indent: 2em">
          {{ industryDescription }}
        </div>
        <div>
          <!-- {{ information.wage | number }} -->
        </div>
      </div>

      <div class="info-block col-4 q-pa-md">
        <q-img :src="jobInfo.bigJobImg" spinner-color="blue" height="90%" />
        <div>{{ jobInfo.jobDesc }}</div>
      </div>

      <div class="info-block col-4 q-pa-md">
        <div class="text-h5 q-mb-sm text-bold">行业薪资趋势</div>
        <div id="salary-trend-line" class="trend-graph-height"></div>
      </div>

      <div class="row info-container">
        <div class="col-4 info-block q-pa-md">
          <div class="text-h5 text-bold">证书要求</div>
          <div
            id="my-word-cloud-certi"
            class="pie-graph-height"
            style="max-height: 300px"
          />
        </div>

        <div class="col-4 info-block q-pa-md" style="height: auto">
          <div class="text-h5 text-bold">技能要求</div>
          <div
            id="my-word-cloud-skill"
            class="pie-graph-height"
            style="max-height: 300px"
          />
        </div>

        <div class="col-4 info-block q-pa-md" style="height: auto">
          <div class="text-h5 text-bold">工具标签</div>
          <div
            id="my-word-cloud-tool"
            class="pie-graph-height"
            style="max-height: 300px"
          />
        </div>
      </div>
    </div>

    <!--    具体岗位排行榜-->
    <div class="column info-container info-block">
      <div class="text-bold text-h5 q-ma-md col">行业岗位</div>
      <!--      名称、岗位数量、薪资、热门讨论-->
      <q-list class="col" separator>
        <q-item
          v-for="item of jobList"
          :key="item.id"
          class="q-pa-md hover-active"
        >
          <q-item-section avatar>
            <img :src="item.companyLogo" style="max-width: 120px" />
            <q-item-label
              class="text-h6 cursor-pointer cover-color q-ma-sm"
              @click="goToJob(item.id)"
              >{{ item.jobSubName }}
            </q-item-label>
          </q-item-section>

          <q-item-section>
            <q-item-label caption lines="4">
              <div>
                <div>
                  工作限制:
                  {{ item.jobLimitExperience }}
                  {{ item.jobLimitStudy }}
                </div>
                <div>
                  工作地区:
                  {{ item.jobArea }}
                </div>
                <div>
                  融资状况:
                  {{ item.financialStatus }}
                </div>
                <div> 
                  {{ item.bonus }}
                  {{ item.scale }}
                  {{ item.jobIndustry }}
                </div>
              </div>
            </q-item-label>
          </q-item-section>

          <q-item-section side top>
            <q-item-label class="text-primary text-bold"
              >薪资：{{ item.jobSalary }}
            </q-item-label>
            <a @click="goToJob(item.id)" class="cursor-pointer">
              <q-icon name="loupe" />
              详细信息
            </a>
            <a>
              <q-icon name="forum" />
              论坛讨论</a
            >
          </q-item-section>
        </q-item>
        <q-separator spaced inset></q-separator>
      </q-list>
    </div>
  </div>
</template>

<script>
import { Line, WordCloud } from "@antv/g2plot";

export default {
  name: "Industry",
  data() {
    return {
      tags: {},
      personality: {},
      major: {},
      ageSex: {},
      task: {},
      jobInfo: {},
      information: {},
      industryName: "加载中",
      industryDescription: "加载中",
      jobList: [
        {
          jobName: "产品经理",
          positionNum: 11203,
          salaryAvg: 234232,
          hotComments: [
            {
              cid: 1122,
              uid: 2424,
              time: "2021-10-01",
              uname: "转角遇到爱",
              like: 522,
              dislike: 11,
              comment:
                "产品经理是一个非常有潜力的岗位网络管理、网络软件部署、系统集成、计算机软硬件方面的维护与营销、数据库管理等。例如：电脑等设备安装与调试……",
            },
            {
              cid: 1121,
              uid: 2421,
              time: "2021-10-01",
              uname: "春秋笔法",
              like: 123,
              dislike: 1,
              comment:
                "我是一名从业多年的产品经理，我网络管理、网络软件部署、系统集成、计算机软硬件方面的维护与营销、数据库管理等。例如：电脑等设备安装与调试……",
            },
          ],
        },
      ],
    };
  },
  methods: {
    goToJob(jobId) {
      this.$router.push({ name: "Job", query: { jobId: jobId } });
    },
    getCloudFormat(ob) {
      var result = Array();
      for (let i = 0; i < ob.length; i++) {
        result.push({ value: ob[i].count, name: ob[i].desc });
      }
      return result;
    },
  },
  mounted: async function () {
    this.jobCat = this.$route.query.jobCat ?? this.jobCat;
    let res = await this.$api.bigjob.bigjobSalaryTrend(this.jobCat);
    this.lineData = res.data.data;
    const data = this.lineData;
    const line = new Line("salary-trend-line", {
      data: data,
      padding: "auto",
      xField: "Date",
      yField: "scales",
      xAxis: {
        tickCount: 5,
      },
      slider: {
        start: 0.1,
        end: 0.5,
      },
    });

    res = await this.$api.bigjob.getTags(this.jobCat);
    this.information.tags = res.data.data;

    var certi_cloud = this.getCloudFormat(this.information.tags.certification);
    const data1 = certi_cloud;
    const skill_cloud = this.getCloudFormat(this.information.tags.skill);
    const tool_cloud = this.getCloudFormat(this.information.tags.tool);

    const wordCloudCerti = new WordCloud("my-word-cloud-certi", {
      data: data1,
      wordField: "name",
      weightField: "value",
      colorField: "name",
      height: 300,
      wordStyle: {
        fontFamily: "Verdana",
        fontSize: [8, 32],
        rotation: 0,
      },
      random: () => 0.5,
    });
    const wordCloudSkill = new WordCloud("my-word-cloud-skill", {
      data: skill_cloud,
      wordField: "name",
      weightField: "value",
      colorField: "name",
      wordStyle: {
        fontFamily: "Verdana",
        fontSize: [8, 32],
        rotation: 0,
      },
      random: () => 0.5,
    });
    const wordCloudTool = new WordCloud("my-word-cloud-tool", {
      data: tool_cloud,
      wordField: "name",
      weightField: "value",
      colorField: "name",
      wordStyle: {
        fontFamily: "Verdana",
        fontSize: [8, 32],
        rotation: 0,
      },
      random: () => 0.5,
    });
    line.render();
    wordCloudCerti.render();
    wordCloudSkill.render();
    wordCloudTool.render();

    res = await this.$api.bigjob.getSubJobs(this.jobCat);
    this.jobList = res.data.data;

    res = await this.$api.bigjob.getBigJobDetail(this.jobCat);
    this.jobInfo = res.data.data;
    this.industryName = this.jobInfo.jobName;
    this.industryDescription = this.jobInfo.jobWork;

    res = await this.$api.bigjob.getPersonality(this.jobCat);
    this.information.personality = res.data.data;

    res = await this.$api.bigjob.getWage(this.jobCat);
    this.information.wage = res.data.data;

    res = await this.$api.bigjob.getMajor(this.jobCat);
    this.information.major = res.data.data;

    res = await this.$api.bigjob.getAgeSex(this.jobCat);
    this.information.ageSex = res.data.data;

    res = await this.$api.bigjob.getTask(this.jobCat);
    this.information.task = res.data.data;

    // const data = [
    //   {type: '分类一', value: 27},
    //   {type: '分类二', value: 25},
    //   {type: '分类三', value: 18},
    //   {type: '分类四', value: 15},
    //   {type: '分类五', value: 10},
    //   {type: '其他', value: 5},
    // ];

    // const piePlot = new Pie('number-pie', {
    //   appendPadding: 10,
    //   data,
    //   angleField: 'value',
    //   colorField: 'type',
    //   radius: 0.75,
    //   label: {
    //     type: 'inner',
    //     offset: '-30%',
    //     content: ({percent}) => `${(percent * 100).toFixed(0)}%`,
    //     style: {
    //       fontSize: 14,
    //       textAlign: 'center',
    //     },
    //   },
    //   interactions: [{type: 'element-selected'}, {type: 'element-active'}],
    // });

    // const piePlot2 = new Pie('salary-pie', {
    //   appendPadding: 10,
    //   data,
    //   angleField: 'value',
    //   colorField: 'type',
    //   radius: 0.75,
    //   label: {
    //     type: 'inner',
    //     offset: '-30%',
    //     content: ({percent}) => `${(percent * 100).toFixed(0)}%`,
    //     style: {
    //       fontSize: 14,
    //       textAlign: 'center',
    //     },
    //   },
    //   interactions: [{type: 'element-selected'}, {type: 'element-active'}],
    // });

    // piePlot.render();
    // piePlot2.render();
  },
};
</script>

<style scoped>
.info-container {
  width: 90%;
  margin: auto;
}

.info-block {
  background: white;
  border: solid 10px #f5f6f9;
  border-radius: 20px;
}

.trend-graph-height {
  height: 300px;
}

.pie-graph-height {
  height: 200px;
}

.cover-color:hover {
  color: deepskyblue;
}

.hover-active:hover {
  background: azure;
}
</style>
