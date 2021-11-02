<template>
  <div>
    <div class="row" >
    <div class="col">
    </div>
    <div class="col-2" id="row_col1">
    <img :src="require('@/assets/writer.jpeg')" class="profile"/>
    </div>
    <div class="col-5" id="row_col1">
     {{body.body}}
    </div>
    <div class="col-4">
    </div>
    </div>
    
    <div class="row" >
    <div class="col">
    </div>
      <div class="col-2" style="text-align:center" id="row_col2">
        {{body.writer}}
      </div>
      <div class="col-5" style="text-align:right" id="row_col2">
        <q-btn 
        id="1"
        icon="thumb_up_alt"
        rounded flat
        color="black"
        @click="thumb_up"
      ></q-btn>
      <q-btn
        icon="thumb_down_alt"
        rounded flat
        color="black"
        @click="refresh"
      ></q-btn>
      </div>
      <div class="col-4">
      </div>
    </div>
    
  </div>
</template>



<script>
export default {
  name: 'forumItem',
  props:{
      body:Object
  }
}
</script>

<style>
#row_col1{
  background:#F5F6F9;
  border-width:1px 1px 0px 1px;
  border-style: solid;
  border-color: #DCDFE5;
  padding: 10px;
}

#row_col2{
  background:#F5F6F9;
  border-width:0px 1px 1px 1px;
  border-style: solid;
  border-color: #DCDFE5;
  padding: 10px;
}
.profile{
  width:150px;
  margin: 10px 10px 10px 20px;
}
</style>