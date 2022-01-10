<template>
  <div>
    <particles-bg :bg="true" type="circle" num="10"></particles-bg>
    <div class="shadow-3 right-card bg-white" style="border-radius: 25px">
      <q-icon
        name="account_box"
        class="q-ma-md q-pa-lg"
        style="left: 110px"
        size="100px"
        color="cyan-8"
      ></q-icon>
      <q-form @submit="onSubmit" class="q-gutter-md q-ml-lg q-mr-lg">
        <q-input
          filled
          v-model="username"
          label="Username"
          hint="你的用户名"
          lazy-rules
          :rules="[(val) => (val && val.length > 0) || '用户名不能为空']"
        />

        <q-input
          filled
          v-model="password"
          hint="你的密码"
          label="Password"
          lazy-rules
          :type="isPwd ? 'password' : 'text'"
          :rules="[
            (val) => (val !== null && val !== '') || '密码不能为空',
            (val) => val.length >= 10 || '密码需要不少于10位',
          ]"
        >
          <template v-slot:append>
            <q-icon
              :name="isPwd ? 'visibility_off' : 'visibility'"
              class="cursor-pointer"
              @click="isPwd = !isPwd"
            />
          </template>
        </q-input>
        <q-btn
          flat
          label="点我人机验证！"
          color="blue"
          icon="fingerprint"
          @click="peopleJudge"
        ></q-btn>
        <Vcode :show="isHidden" @success="success" @close="close" />

        <div style="float: right">
          <q-btn
            label="登录"
            type="submit"
            color="primary"
            :disable="!isPeople"
          />
          <q-btn
            label="没有账号？现在注册"
            color="primary"
            @click="onRegister"
            flat
            class="q-ml-sm q-mr-lg"
          />
        </div>
      </q-form>
    </div>
  </div>
</template>

<script>
import Vcode from "vue-puzzle-vcode";
import { ParticlesBg } from "particles-bg-vue";

export default {
  name: "Login",
  components: {
    ParticlesBg,
    Vcode,
  },
  data() {
    return {
      username: "",
      password: "",
      isPeople: false,
      isPwd: true,
      isHidden: false, // 验证码模态框是否出现
    };
  },
  mounted: async function () {
    let res = await this.$api.user.isLogin();
    let isLogin = res.data.data.result;
    
    if (isLogin) {
      await this.$router.push({ name: "Home" });
    }
  },
  methods: {
    peopleJudge() {
      this.isHidden = true;
    },
    // 用户通过了验证
    success(msg) {
      console.log(msg);
      this.isHidden = false; // 通过验证后，隐藏模态框
      this.isPeople = true;
    },
    // 用户点击遮罩层，关闭模态框
    close() {
      this.isHidden = false;
    },
    onSubmit: async function () {
      let data = { username: this.username, password: this.password };
      await this.$api.user.setToken();
      let res = await this.$api.user.login(data);
      if (res.data.code !== 0) {
        this.$q.notify({
          message: res.data.message,
          color: "secondary",
          position: "top-right",
          icon: "announcement",
        });
      } else {
        res = await this.$api.user.isLogin();
        if (res.data.data.result) {
          await this.$router.push({ name: "Home" });
        }
      }
    },
    onRegister: function () {
      this.$router.push({ name: "Register" });
    },
  },
};
</script>

<style scoped>
.right-card {
  width: 400px;
  height: 550px;
  position: absolute;
  right: 5%;
  top: 15%;
}
</style>
