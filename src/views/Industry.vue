<template>
  <div>
    <!--    头部信息-->
    <div class="info-container row" style="min-height: 300px">
      <!--      信息框-->
      <div class="info-block col-4 q-pa-md">
        <!--        标题-->
        <div class="text-h5 text-bold">{{ industryName }}</div>
        <!--        描述-->
        <div class="text-caption">{{ industryDescription }}</div>
      </div>

      <!--      行业各岗位数量占比饼图-->
      <div class="info-block col-4 q-pa-md">
        <div class="text-h5 text-bold">行业各岗位数量占比饼图</div>
        <div id="number-pie" class="pie-graph-height"/>
      </div>

      <!--      行业各岗位薪资占比饼图-->
      <div class="info-block col-4 q-pa-md">
        <div class="text-h5 text-bold">行业各岗位薪资占比饼图</div>
        <div id="salary-pie" class="pie-graph-height"/>
      </div>
    </div>

    <!--    趋势图标-->
    <div class="row info-container">
      <!--    行业薪资趋势-->
      <div class="col-6 info-block q-pa-md">
        <div class="text-h5 q-mb-sm text-bold">行业薪资趋势</div>
        <div id="salary-trend-line" class="trend-graph-height"></div>
      </div>

      <!--    行业岗位数量趋势-->
      <div class="col-6 info-block q-pa-md" style="height: auto;">
        <div class="text-h5 q-mb-sm text-bold">行业岗位数量趋势</div>
        <div id="number-trend-line" class="trend-graph-height"></div>
      </div>
    </div>
    <!--    具体岗位排行榜-->
    <div class="column info-container info-block">
      <div class="text-bold text-h5 q-ma-md col">行业岗位排行榜</div>
      <!--      名称、岗位数量、薪资、热门讨论-->
      <q-list class="col" separator>
        <q-item v-for="item of jobList" :key="item.id" class="q-pa-md hover-active">
          <q-item-section>
            <q-item-label class="text-bold text-h6 cursor-pointer cover-color" @click="goToJob">{{
                item.jobName
              }}
            </q-item-label>
            <q-item-label caption lines="2">
              <div v-for="comment of item.hotComments" :key="comment.id">
                <a>{{ comment.time }}</a> <a class="text-bold text-blue">{{ comment.uname }}:</a>{{ comment.comment }}
                <q-icon name="thumb_up" class="q-ml-md"/>
                {{ comment.like }}
                <q-icon name="thumb_down"/>
                {{ comment.dislike }}
              </div>
            </q-item-label>
          </q-item-section>

          <q-item-section side top>
            <q-item-label class="text-primary text-bold">平均薪资：{{ item.salaryAvg }}</q-item-label>
            <q-item-label class="text-primary text-bold">岗位数量：{{ item.positionNum }}</q-item-label>
            <a>
              <q-icon name="loupe"/>
              详细信息</a>
            <a>
              <q-icon name="forum"/>
              论坛讨论</a>
          </q-item-section>
        </q-item>
        <q-separator spaced inset></q-separator>
      </q-list>
    </div>
  </div>
</template>

<script>
import {Pie, Line} from '@antv/g2plot';

export default {
  name: "Industry",
  data() {
    return {
      industryName: "计算机/网络/技术类",
      industryDescription: "计算机网络技术主要研究计算机网络和网络工程等方面基本知识和技能，进行网络安装维护、" +
          "网络管理、网络软件部署、系统集成、计算机软硬件方面的维护与营销、数据库管理等。例如：电脑等设备安装与调试，" +
          "计算机系统的测试、维护和维修，网页图形、图像、动画、视频、声音等多媒体设计及制作等。",
      jobList: [
        {
          jobName: "产品经理", positionNum: 11203, salaryAvg: 234232, hotComments: [
            {
              cid: 1122,
              uid: 2424,
              time: "2021-10-01",
              uname: "转角遇到爱",
              like: 522,
              dislike: 11,
              comment: "产品经理是一个非常有潜力的岗位网络管理、网络软件部署、系统集成、计算机软硬件方面的维护与营销、数据库管理等。例如：电脑等设备安装与调试……"
            },
            {
              cid: 1121,
              uid: 2421,
              time: "2021-10-01",
              uname: "春秋笔法",
              like: 123,
              dislike: 1,
              comment: "我是一名从业多年的产品经理，我网络管理、网络软件部署、系统集成、计算机软硬件方面的维护与营销、数据库管理等。例如：电脑等设备安装与调试……"
            }
          ]
        },
        {
          jobName: "高级产品经理", positionNum: 11203, salaryAvg: 234232, hotComments: [
            {
              cid: 1122,
              uid: 2424,
              time: "2021-10-01",
              uname: "转角遇到爱",
              like: 522,
              dislike: 11,
              comment: "产品经理是一个非常有潜力的岗位网络管理、网络软件部署、系统集成、计算机软硬件方面的维护与营销、数据库管理等。例如：电脑等设备安装与调试……"
            },
            {
              cid: 1121,
              uid: 2421,
              time: "2021-10-01",
              uname: "春秋笔法",
              like: 123,
              dislike: 1,
              comment: "我是一名从业多年的产品经理，我网络管理、网络软件部署、系统集成、计算机软硬件方面的维护与营销、数据库管理等。例如：电脑等设备安装与调试……"
            }
          ]
        },
        {
          jobName: "前端开发工程师", positionNum: 11203, salaryAvg: 234232, hotComments: [
            {
              cid: 1122,
              uid: 2424,
              time: "2021-10-01",
              uname: "转角遇到爱",
              like: 522,
              dislike: 11,
              comment: "产品经理是一个非常有潜力的岗位……"
            },
            {
              cid: 1121,
              uid: 2421,
              time: "2021-10-01",
              uname: "春秋笔法",
              like: 123,
              dislike: 1,
              comment: "我是一名从业多年的产品经理，我……"
            }
          ]
        },
        {
          jobName: "web前端开发工程师", positionNum: 11203, salaryAvg: 234232, hotComments: [
            {
              cid: 1122,
              uid: 2424,
              time: "2021-10-01",
              uname: "转角遇到爱",
              like: 522,
              dislike: 11,
              comment: "产品经理是一个非常有潜力的岗位……"
            },
            {
              cid: 1121,
              uid: 2421,
              time: "2021-10-01",
              uname: "春秋笔法",
              like: 123,
              dislike: 1,
              comment: "我是一名从业多年的产品经理，我……"
            }
          ]
        },
        {
          jobName: "java开发工程师", positionNum: 11203, salaryAvg: 234232, hotComments: [
            {
              cid: 1122,
              uid: 2424,
              time: "2021-10-01",
              uname: "转角遇到爱",
              like: 522,
              dislike: 11,
              comment: "产品经理是一个非常有潜力的岗位……"
            },
            {
              cid: 1121,
              uid: 2421,
              time: "2021-10-01",
              uname: "春秋笔法",
              like: 123,
              dislike: 1,
              comment: "我是一名从业多年的产品经理，我……"
            }
          ]
        },
      ]
    }
  },
  methods: {
    goToJob() {
      this.$router.replace({name: "Job"})
    }
  },
  mounted() {
    fetch('https://gw.alipayobjects.com/os/bmw-prod/1d565782-dde4-4bb6-8946-ea6a38ccf184.json')
        .then((res) => res.json())
        .then((data) => {
          const line = new Line('salary-trend-line', {
            data,
            padding: 'auto',
            xField: 'Date',
            yField: 'scales',
            xAxis: {
              tickCount: 5,
            },
            slider: {
              start: 0.1,
              end: 0.5,
            },
          });
          const line2 = new Line('number-trend-line', {
            data,
            padding: 'auto',
            xField: 'Date',
            yField: 'scales',
            xAxis: {
              tickCount: 5,
            },
            slider: {
              start: 0.1,
              end: 0.5,
            },
          });
          line.render();
          line2.render();
        });

    const data = [
      {type: '分类一', value: 27},
      {type: '分类二', value: 25},
      {type: '分类三', value: 18},
      {type: '分类四', value: 15},
      {type: '分类五', value: 10},
      {type: '其他', value: 5},
    ];

    const piePlot = new Pie('number-pie', {
      appendPadding: 10,
      data,
      angleField: 'value',
      colorField: 'type',
      radius: 0.75,
      label: {
        type: 'inner',
        offset: '-30%',
        content: ({percent}) => `${(percent * 100).toFixed(0)}%`,
        style: {
          fontSize: 14,
          textAlign: 'center',
        },
      },
      interactions: [{type: 'element-selected'}, {type: 'element-active'}],
    });

    const piePlot2 = new Pie('salary-pie', {
      appendPadding: 10,
      data,
      angleField: 'value',
      colorField: 'type',
      radius: 0.75,
      label: {
        type: 'inner',
        offset: '-30%',
        content: ({percent}) => `${(percent * 100).toFixed(0)}%`,
        style: {
          fontSize: 14,
          textAlign: 'center',
        },
      },
      interactions: [{type: 'element-selected'}, {type: 'element-active'}],
    });

    piePlot.render();
    piePlot2.render();
  }
}
</script>

<style scoped>
.info-container {
  width: 90%;
  margin: auto;
}

.info-block {
  background: white;
  border: solid 10px #F5F6F9;
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

.hover-active:hover{
  background: azure;
}
</style>
