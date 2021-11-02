<template>
  <div>
    <!--    头部信息-->
    <div class="info-container row" style="min-height: 300px">
      <!--      信息框-->
      <div class="info-block col-4 q-pa-md">
        <!--        标题-->
        <div class="text-h5 text-bold">{{ jobData.jobName }}</div>
        <!--        描述-->
        <div class="text-caption">{{ jobData.jobDescription }}</div>
      </div>

      <!--      发展前景：薪资均值、最大值、最小值；招聘岗位数量2021；-->
      <div class="info-block col-4 q-pa-md">
        <div class="text-h5 text-bold">发展前景</div>
        <div class="text-bold">薪资均值 <a class="text-primary">{{jobData.salary.mean}}</a></div>
        <div class="text-bold">薪资最大值 <a class="text-primary">{{ jobData.salary.max }}</a></div>
        <div class="text-bold">薪资最小值 <a class="text-primary">{{ jobData.salary.min }}</a></div>
        <div class="text-bold">岗位数量 <a class="text-primary">{{ jobData.number }}</a></div>
      </div>

      <!--      学历要求、经验要求、要求标签-->
      <div class="info-block col-4 q-pa-md">
        <div class="text-h5 text-bold">相关要求</div>
        <div id="salary-pie" class="pie-graph-height"/>
      </div>
    </div>

    <!--    趋势图表-->
    <div class="row info-container">
      <!--    岗位薪资趋势-->
      <div class="col-6 info-block q-pa-md">
        <div class="text-h5 q-mb-sm text-bold">岗位薪资趋势</div>
        <div id="salary-trend-line" class="trend-graph-height"></div>
      </div>

      <!--    岗位数量趋势-->
      <div class="col-6 info-block q-pa-md" style="height: auto;">
        <div class="text-h5 q-mb-sm text-bold">岗位数量趋势</div>
        <div id="number-trend-line" class="trend-graph-height"></div>
      </div>
    </div>
    <!--    相关岗位招聘信息-->
    <div class="column info-container info-block">
      <div class="text-bold text-h5 q-ma-md col">相关岗位招聘信息</div>
      <!--      名称、要求、薪资、发布网站、时间、热门讨论-->
      <q-list class="col" separator>
        <q-item v-for="item of jobList" :key="item.id" class="q-pa-md">
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
        jobRequirement:[]
      }

    }
  }
}
</script>

<style scoped>
.info-container {
  width: 90%;
  margin: auto;
}

.info-block {
  border: solid;
  background: white;
}
</style>
