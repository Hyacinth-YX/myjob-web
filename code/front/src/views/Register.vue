<template>
  <div>
    <particles-bg :bg="true" type="circle" num=10></particles-bg>
    <div class="shadow-3 register-card bg-white " style="border-radius:25px">
      <div class="text-h4 text-bold q-pa-md" style="text-align: center">
        <q-icon name="how_to_reg"/>
        注册账户
      </div>
      <q-form
          @submit="onSubmit"
          class="q-gutter-md q-ml-xl q-mr-xl"
      >
        <q-input
            filled
            v-model="username"
            label="Username"
            hint="请输入你的用户名"
            lazy-rules
            :rules="[ val => val && val.length > 0 || '用户名不能为空']"
        />
        <q-input
            filled
            v-model="password"
            hint="请输入你的密码"
            label="Password"
            lazy-rules
            :rules="[val => val !== null && val !== '' || '密码不能为空',
          val => val.length >= 10 || '密码需要不少于10位']"
        />
        <q-input
            filled
            v-model="passwordRe"
            hint="再次输入你的密码"
            label="Password"
            lazy-rules
            error-message="两次输入的密码不同"
            :error="password!==passwordRe"
        />
        <q-input
            filled
            v-model="password"
            hint="请输入你的邮箱"
            label="E-mail"
            lazy-rules
        />

        <q-toggle v-model="accept">I accept the license and <a href="#">terms</a></q-toggle>

        <q-btn flat label="点我人机验证！" color="blue" icon="fingerprint" @click="peopleJudge"></q-btn>
        <Vcode :show="isHidden" @success="success" @close="close" name="validation"/>

        <div style="text-align: center" class="q-ma-md">
          <q-btn label="立即注册" type="submit" color="primary" :disable="!accept || !isPeople"/>
        </div>

      </q-form>

    </div>
  </div>
</template>

<script>
import {ParticlesBg} from "particles-bg-vue";
import Vcode from "vue-puzzle-vcode";


export default {
  name: "Register",
  components: {
    ParticlesBg,
    Vcode
  },
  data() {
    return {
      username: "",
      password: "",
      passwordRe: "",
      accept: false,
      isHidden: false,
      isPeople: false,
    }
  },
  methods: {
    peopleJudge() {
      this.isHidden = true;
    },
    // 用户通过了验证
    success(msg) {
      console.log(msg)
      this.isHidden = false; // 通过验证后，隐藏模态框
      this.isPeople = true;
    },
    // 用户点击遮罩层，关闭模态框
    close() {
      this.isHidden = false;
    },
    onSubmit: async function () {
      // let data = {username: this.username, password: this.password};
      // await this.$api.setToken();
      // let res = await this.$api.login(data);
      // if (res.data.code !== 1) {
      //   this.$q.notify({
      //     message: res.data.message,
      //     color: 'secondary',
      //     position: "top-right",
      //     icon: 'announcement'
      //   })
      // } else {
      //   res = await this.$api.isLogin();
      //   if (res.data.data) {
      //     await this.$router.replace({name: 'Experiment'})
      //   }
      // }
      await this.$router.replace({name: "Home"});
    },
  }
}
</script>

<style scoped>
.register-card {
  width: 45%;
  margin-left: 30%;
  margin-top: 30px;
  height: 600px;
}
</style>
