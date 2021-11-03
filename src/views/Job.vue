<template>
  <div>
    <!--    头部信息-->
    <div class="info-container row" style="min-height: 300px">
      <!--      信息框-->
      <div class="info-block col-4 q-pa-md">
        <!--        标题-->
        <div class="text-h4 q-pa-sm text-bold">{{ jobData.jobName }}</div>
        <!--        描述-->
        <div class="text-body1" style="text-indent: 2em">{{ jobData.jobDescription }}</div>
      </div>

      <!--      发展前景：薪资均值、最大值、最小值；招聘岗位数量2021；-->
      <div class="info-block col-4 q-pa-md text-h5">
        <div class="text-h4 q-pa-sm text-bold">发展前景</div>
        <table border="0" class="q-pa-sm text-body1" style="width: 100%;font-family: SimSun, cursive">
          <tr>
            <td>薪资均值</td>
            <td><a class="text-primary">{{ jobData.salary.mean }}</a>
              <q-icon class="q-mb-sm" color="red" name="north"/>
            </td>
          </tr>
          <tr>
            <td>薪资最大值</td>
            <td><a class="text-primary">{{ jobData.salary.max }}</a>
              <q-icon class="q-mb-sm" color="red" name="north"/>
            </td>
          </tr>
          <tr>
            <td>薪资最小值</td>
            <td><a class="text-primary">{{ jobData.salary.min }}</a>
              <q-icon class="q-mb-sm" color="red" name="north"/>
            </td>
          </tr>
          <tr>
            <td>岗位数量</td>
            <td><a class="text-primary">{{ jobData.number }}</a>
              <q-icon class="q-mb-sm" color="green" name="south"/>
            </td>
          </tr>
        </table>
        <span class="row justify-center">
          <div class="col-6" id="liquid-graph" style="max-height: 130px"></div>
          <div class="col-5" id="gauge-graph" style="max-height: 100px"></div>
        </span>
        <span class="row justify-center">
          <div class="col-6 text-caption" style="text-align: center">薪资中值/历史最大值</div>
          <div class="col-6 text-caption" style="text-align: center">当前岗位数量/历史平均</div>
        </span>

      </div>

      <!--要求标签-->
      <div class="info-block col-4 q-pa-md">
        <div class="text-h4 q-pa-sm text-bold">相关要求</div>
        <div id="my-word-cloud" class="pie-graph-height" style="max-height: 300px"/>
      </div>
    </div>

    <!-- 趋势图表-->
    <div class="row info-container">
      <!--岗位薪资趋势-->
      <div class="col-6 info-block q-pa-md">
        <div class="text-h4 q-pa-sm q-mb-sm text-bold">岗位薪资趋势</div>
        <div id="salary-trend-line" style="max-height: 300px"></div>
      </div>
      <!--岗位数量趋势-->
      <div class="col-6 info-block q-pa-md" style="height: auto;">
        <div class="text-h4 q-pa-sm q-mb-sm text-bold">岗位数量趋势</div>
        <div id="number-trend-line" style="max-height: 300px"></div>
      </div>
    </div>

    <!--要求图表 - 学历要求、经验要求-->
    <div class="row info-container">
      <!--学历要求-->
      <div class="col-6 info-block q-pa-md">
        <div class="text-h4 q-pa-sm q-mb-sm text-bold">学历要求</div>
        <div id="study-require-distribution" style="height: 300px"></div>
      </div>
      <!--经验要求-->
      <div class="col-6 info-block q-pa-md" style="height: auto;">
        <div class="text-h4 q-pa-sm q-mb-sm text-bold">经验要求</div>
        <div id="experience-require-distribution" style="height: 300px"></div>
      </div>
    </div>
    <!--相关岗位招聘信息-->
    <div class="column info-container info-block">
      <div class="text-bold text-h4 q-pa-sm q-ma-md col">相关岗位招聘信息</div>
      <!--名称、要求、薪资、发布网站、时间、热门讨论-->
      <q-list class="col" separator>
        <q-item v-for="item of jobData.jobRequirement" :key="item.id" class="q-pa-md hover-active">
          <q-item-section>
            <q-item-label class="text-bold text-h6 cursor-pointer cover-color">
              {{ item.jobName }}
            </q-item-label>
            <q-item-label caption lines="1" class="q-pa-sm">
              {{ item.experience }} || {{ item.study }} || {{ item.companyName }}
            </q-item-label>
            <q-item-label style="text-indent: 2em">
              {{ item.jobDescription }}
            </q-item-label>
          </q-item-section>

          <q-item-section side top>
            {{item.datetime}}
            <q-item-label class="text-primary text-bold">薪资：{{ item.salary }}</q-item-label>
            <a class="cursor-pointer">
              <q-icon name="loupe"/>
              详细信息
            </a>
          </q-item-section>
        </q-item>

        <q-separator spaced inset></q-separator>
      </q-list>
    </div>
  </div>
</template>

<script>
import {WordCloud, Liquid, Gauge, Line, Column} from '@antv/g2plot';

export default {
  name: "Job",
  data() {
    return {
      jobData: {
        salary: {mean: 12313, max: 134133, min: 1244},
        number: 23423,
        jobName: "算法工程师",
        jobDescription: `算法工程师是一个比较高端的职位；
专业要求：计算机、电子、通信、数学等相关专业；
学历要求：本科及其以上的学历，大多数是硕士学历及其以上；
语言要求：英语要求是熟练，基本上能阅读国外专业书刊；
必须掌握计算机相关知识，熟练使用仿真工具MATLAB等，必须会一门编程语言。`,
        jobRequirement: [
          {
            companyName: "华为", jobName: "图形算法工程师", reqDate: 11203, salary: "10-20w", experience: '1-3年',
            study: "本科以上", datetime: "2021-10-10", viewed: 12341,
            jobDescription: "岗位职责：1.负责各类图像检测算法研发与优化；2.负责各类机器视觉算法研发与优化；3.负责各类深度学习算法研发与优化。职位要求：1. 熟悉常用的图像检测算法，如运动检测、人脸检测、客流检测等；熟悉常用的图像处理算法，如降噪、边缘增强、色彩空间转换、运动估计与补偿等；熟悉深度学习与神经网路算法；2. 重点大学计算机、软件工程、数学、电子信息等相关专业本科及以上学历；3. 三年以上影像类行业工作经验；4. 熟悉C/C++语言，Matlab, Python 工具 了解嵌入式系统开发流程；有Linux驱动开发经验者优先；5. 具有很好的英文文档阅读能力和软件开发文档编写能力；6. 善于沟通，分析和解决问题，具备良好的团队合作能力。"
          },
          {
            companyName: "华为", jobName: "图形算法工程师", reqDate: 11203, salary: "10-20w", experience: '1-3年',
            study: "本科以上", datetime: "2021-10-10", viewed: 12341,
            jobDescription: "岗位职责：1.负责各类图像检测算法研发与优化；2.负责各类机器视觉算法研发与优化；3.负责各类深度学习算法研发与优化。职位要求：1. 熟悉常用的图像检测算法，如运动检测、人脸检测、客流检测等；熟悉常用的图像处理算法，如降噪、边缘增强、色彩空间转换、运动估计与补偿等；熟悉深度学习与神经网路算法；2. 重点大学计算机、软件工程、数学、电子信息等相关专业本科及以上学历；3. 三年以上影像类行业工作经验；4. 熟悉C/C++语言，Matlab, Python 工具 了解嵌入式系统开发流程；有Linux驱动开发经验者优先；5. 具有很好的英文文档阅读能力和软件开发文档编写能力；6. 善于沟通，分析和解决问题，具备良好的团队合作能力。"
          },
          {
            companyName: "华为", jobName: "图形算法工程师", reqDate: 11203, salary: "10-20w", experience: '1-3年',
            study: "本科以上", datetime: "2021-10-10", viewed: 12341,
            jobDescription: "岗位职责：1.负责各类图像检测算法研发与优化；2.负责各类机器视觉算法研发与优化；3.负责各类深度学习算法研发与优化。职位要求：1. 熟悉常用的图像检测算法，如运动检测、人脸检测、客流检测等；熟悉常用的图像处理算法，如降噪、边缘增强、色彩空间转换、运动估计与补偿等；熟悉深度学习与神经网路算法；2. 重点大学计算机、软件工程、数学、电子信息等相关专业本科及以上学历；3. 三年以上影像类行业工作经验；4. 熟悉C/C++语言，Matlab, Python 工具 了解嵌入式系统开发流程；有Linux驱动开发经验者优先；5. 具有很好的英文文档阅读能力和软件开发文档编写能力；6. 善于沟通，分析和解决问题，具备良好的团队合作能力。"
          },
          {
            companyName: "华为", jobName: "图形算法工程师", reqDate: 11203, salary: "10-20w", experience: '1-3年',
            study: "本科以上", datetime: "2021-10-10", viewed: 12341,
            jobDescription: "岗位职责：1.负责各类图像检测算法研发与优化；2.负责各类机器视觉算法研发与优化；3.负责各类深度学习算法研发与优化。职位要求：1. 熟悉常用的图像检测算法，如运动检测、人脸检测、客流检测等；熟悉常用的图像处理算法，如降噪、边缘增强、色彩空间转换、运动估计与补偿等；熟悉深度学习与神经网路算法；2. 重点大学计算机、软件工程、数学、电子信息等相关专业本科及以上学历；3. 三年以上影像类行业工作经验；4. 熟悉C/C++语言，Matlab, Python 工具 了解嵌入式系统开发流程；有Linux驱动开发经验者优先；5. 具有很好的英文文档阅读能力和软件开发文档编写能力；6. 善于沟通，分析和解决问题，具备良好的团队合作能力。"
          },

        ]
      },

    }
  },
  mounted() {
    const gauge = new Gauge('gauge-graph', {
      percent: 0.75,
      range: {
        color: 'l(0) 0:#B8E1FF 1:#3D76DD',
      },
      startAngle: Math.PI,
      endAngle: 2 * Math.PI,
      indicator: null,
      statistic: {
        content: {
          style: {
            fontSize: '10px',
            lineHeight: '10px',
            color: '#4B535E',
          },
        },
      },
    });
    gauge.render();

    fetch('https://gw.alipayobjects.com/os/antvdemo/assets/data/antv-keywords.json')
        .then((res) => res.json())
        .then((data) => {
          const wordCloud = new WordCloud('my-word-cloud', {
            data,
            wordField: 'name',
            weightField: 'value',
            colorField: 'name',
            wordStyle: {
              fontFamily: 'Verdana',
              fontSize: [8, 32],
              rotation: 0,
            },
            // 返回值设置成一个 [0, 1) 区间内的值，
            // 可以让每次渲染的位置相同（前提是每次的宽高一致）。
            random: () => 0.5,
          });

          wordCloud.render();
        });


    const liquidPlot = new Liquid('liquid-graph', {
      percent: 0.25,
      outline: {
        border: 4,
        distance: 3,
      },
      wave: {
        length: 128,
      },
      statistic: {
        content: {
          style: {fontSize: 15}
        }

      }
    });
    liquidPlot.render();

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
      {
        type: '0-1w',
        sales: 38,
      },
      {
        type: '1-2w',
        sales: 52,
      },
      {
        type: '2-3w',
        sales: 61,
      },
      {
        type: '3-4w',
        sales: 145,
      },
      {
        type: '4-5w',
        sales: 48,
      },
      {
        type: '5-6w',
        sales: 38,
      },
      {
        type: '6-7w',
        sales: 38,
      },
      {
        type: '7-8w',
        sales: 38,
      },
    ];
    const columnPlot = new Column('study-require-distribution', {
      data,
      xField: 'type',
      yField: 'sales',
      autoFit: true,
      columnWidthRatio: 0.95,
      label: {
        // 可手动配置 label 数据标签位置
        position: 'middle', // 'top', 'bottom', 'middle',
        // 配置样式
        style: {
          fill: '#FFFFFF',
          opacity: 0.6,
        },
      },
      xAxis: {
        label: {
          autoHide: true,
          autoRotate: false,
        },
      },
      meta: {
        type: {
          alias: '类别',
        },
        sales: {
          alias: '销售额',
        },
      },
    });

    const columnPlot2 = new Column('experience-require-distribution', {
      data,
      xField: 'type',
      yField: 'sales',
      autoFit: true,
      columnWidthRatio: 0.95,
      label: {
        // 可手动配置 label 数据标签位置
        position: 'middle', // 'top', 'bottom', 'middle',
        // 配置样式
        style: {
          fill: '#FFFFFF',
          opacity: 0.6,
        },
      },
      xAxis: {
        label: {
          autoHide: true,
          autoRotate: false,
        },
      },
      meta: {
        type: {
          alias: '类别',
        },
        sales: {
          alias: '销售额',
        },
      },
    });
    columnPlot.render();
    columnPlot2.render();

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

tr:hover {
  background: azure;
}

.hover-active:hover{
  background: azure;
}
</style>
