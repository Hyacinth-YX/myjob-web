import axios from "axios"; // 引入axios
var instance = axios.create({
  timeout: 1000 * 60,
});
// instance.defaults.withCredentials = false //开启后服务器才能拿到cookie
instance.defaults.headers.post["Content-Type"] =
  "application/json; charset=UTF-8"; //配置默认请求头
// instance.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

let getCookie = function (cookie) {
  let reg = /csrftoken=([\w]+)[;]?/g;
  return reg.exec(cookie)[1];
};

instance.interceptors.request.use(
  function (config) {
    // 在post请求前统一添加X-CSRFToken的header信息
    let cookie = document.cookie;
    if (cookie && config.method === "post") {
      config.headers["X-CSRFToken"] = getCookie(cookie);
    }
    return config;
  },
  function (error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

export { instance };
