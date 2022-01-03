import { instance } from "../utils/http"; // 导入http中创建的axios实例

const user = {
  login(data) {
    return instance.post(`/api/user/login`, data);
  },
  logout() {
    return instance.get(`/api/user/logout`);
  },
  isLogin() {
    return instance.get(`/api/user/isLogin`);
  },
  setToken() {
    return instance.get(`/api/user/setToken`);
  },
  register(data) {
    return instance.post(`/api/user/register`, data);
  },
};

export default user;
