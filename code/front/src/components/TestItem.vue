<template>
  <div v-if="showstatue()" style="opacity: 100%;">
    <q-item-section style="padding: 50px 25px 25px 50px">
      <q-item-label class="text-h5 text-left">{{ idx + 1 }}.{{ questionData }}</q-item-label>
    </q-item-section>
    <div class="row">
      <q-item tag="label" v-ripple class="col-6">
        <q-item-section avatar>
          <q-radio v-model="check" val="0" color="teal" />
        </q-item-section>
        <q-item-section>
          <q-item-label class="text-body1">Yes</q-item-label>
        </q-item-section>
      </q-item>

      <q-item tag="label" v-ripple class="col-6">
        <q-item-section avatar>
          <q-radio v-model="check" val="1" color="red" />
        </q-item-section>
        <q-item-section>
          <q-item-label class="text-body1">No</q-item-label>
        </q-item-section>
      </q-item>
    </div>
  </div>

  <div v-else style="opacity: 50%">
    <q-item-section style="padding: 50px 25px 25px 50px">
      <q-item-label class="text-h5 text-left">{{ idx + 1 }}.{{ questionData }}</q-item-label
      >
    </q-item-section>
    <div class='row'>
    <q-item tag="label" v-ripple class='col-6'>
      <q-item-section avatar>
        <q-radio v-model="check" val="0" color="teal" />
      </q-item-section>
      <q-item-section>
        <q-item-label class="text-body1">Yes</q-item-label>
      </q-item-section>
    </q-item>

    <q-item tag="label" v-ripple class='col-6'>
      <q-item-section avatar>
        <q-radio v-model="check" val="1" color="red" />
      </q-item-section>
      <q-item-section>
        <q-item-label class="text-body1">No</q-item-label>
      </q-item-section>
    </q-item>
    </div>
  </div>
</template>

<script>
export default {
  name: "TestItem",
  props: {
    questionData: String,
    checklist: Array,
    lastlist: Array,
    idx: Number,
    sb: Boolean,
  },
  watch: {
    check() {
      this.checklist[this.idx] = this.check;
      this.$emit('checklist',this.checklist)
      this.lastlist[this.idx] = 1;
      console.log(this.lastlist[this.idx])
      if (this.seen) {
        for (let i = 0; i < 86; i++) {
          setTimeout(() => {
            document.documentElement.scrollTop =
              document.documentElement.scrollTop + 2;
          }, 3 * i);
        }
      }
      this.seen = false;
    },
  },
  methods: {
    showstatue() {
      if (this.seen && this.idx == 0) {
        return true;
      } else if (this.seen == true) {
        return true;
      } else {
        //console.log(this.lastlist[this.idx-1])
        return false;
      }
    },
  },
  data() {
    return {
      check: 0,
      color: "cyan",
      seen: true,
    };
  },
};
</script>

<style scoped>
</style>
