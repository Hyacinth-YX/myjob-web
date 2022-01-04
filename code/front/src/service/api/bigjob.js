import { instance } from "../utils/http"; // 导入http中创建的axios实例

const bigjob = {
  jobs(key1, key2, key3, limit = "") {
    return instance.get(
      `/api/bigjob/jobs?key1=${key1}&key2=${key2}&key3=${key3}&limit=${limit}`
    );
  },
  getTags(jobCat) {
    return instance.get(`/api/bigjob/tags?jobCat=${jobCat}`);
  },
  getPersonality(jobCat) {
    return instance.get(`/api/bigjob/personality?jobCat=${jobCat}`);
  },
  getWage(jobCat) {
    return instance.get(`/api/bigjob/wage?jobCat=${jobCat}`);
  },
  getMajor(jobCat) {
    return instance.get(`/api/bigjob/major?jobCat=${jobCat}`);
  },
  getAgeSex(jobCat) {
    return instance.get(`/api/bigjob/ageSex?jobCat=${jobCat}`);
  },
  getTask(jobCat) {
    return instance.get(`/api/bigjob/task?jobCat=${jobCat}`);
  },
  getHollandCodeQuestions(startIndex, number) {
    return instance.get(
      `/api/bigjob/hollandCodeQuestions?startIndex=${startIndex}&number=${number}`
    );
  },
  postHollandCodeTest(data) {
    return instance.post(`/api/bigjob/hollandCode`, data);
  },
  getJobDetail(jobId) {
    return instance.get(`/api/bigjob/jobdetail?jobId=${jobId}`);
  },
  bigjobSalaryTrend(jobCat) {
    return instance.get(`/api/bigjob/graph/bigjobSalaryTrend?jobCat=${jobCat}`);
  },
  jobSalaryTrend(jobCat) {
    return instance.get(`/api/bigjob/graph/jobSalaryTrend?jobCat=${jobCat}`);
  },
  allBigJobs(limit){
    return instance.get(
      `/api/bigjob/allBigJobs?limit=${limit}&useCache=True`
    );
  }
};

export default bigjob;
