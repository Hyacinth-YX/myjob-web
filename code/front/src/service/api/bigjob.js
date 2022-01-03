import { instance } from "../utils/http"; // 导入http中创建的axios实例

const bigjob = {
  jobs(key1, key2, key3) {
    return instance.get(
      `/api/bigjob/jobs?key1=${key1}&key2=${key2}&key3=${key3}`
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
};

export default bigjob;