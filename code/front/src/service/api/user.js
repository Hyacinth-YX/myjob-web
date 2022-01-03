import { instance } from "../utils/http"; // 导入http中创建的axios实例

const user = {
  login(data) {
    return instance.post(`/api/Users/login`, data);
  },
  logout() {
    return instance.get(`/api/Users/logout`);
  },
  isLogin() {
    return instance.get(`/api/Users/isLogin`);
  },
  setToken() {
    return instance.get(`/api/Users/setToken`);
  },
};

export default user