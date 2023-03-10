<!--“开始体验”页面-->
<template>
  <div>
    <!-- 顶部通栏 -->
    <AppTopNav/>
    <!-- main-->
    <div class="main">
    <!-- 模块1-->
      <div class="test1">
        <img src="../assets/images/img5.jpg" alt=""/>
        <div class="test11">
          <Button @click="mtcnn" style="margin: 0% 30% 10% 15%;">按钮1</Button>
          <span>点击体验MTCNN口罩检测</span>
        </div>
      </div>

      <!-- 分割线-->
      <div class="tableTitle"></div>

      <!--  模块2-->
      <div class="test2">
        <div class="test22">
          <Button @click="yolov5" style="margin: 10% 30% 5% 15%;">按钮2</Button>
          <span>点击体验YOLOv5口罩检测</span>
        </div>
        <img src="../assets/images/img6.jpg" alt=""/>
       </div>
    </div>
    <!-- bottom -->
    <my-footer>fixed</my-footer>
  </div>
</template>

<script>
import AppTopNav from '@/components/AppTopNav.vue';
import Button from '@/components/Button.vue';
import MyFooter from "@/components/MyFooter";

export default {
  name: "twoMethods",
  components: {
    MyFooter,
    AppTopNav,
    Button
  },
  methods:{
    //实现两个按钮跳转
    mtcnn(){
      this.$router.replace('/homeview')
    },
    yolov5(){
      this.$router.replace('/homeview2')
    }
  }
}
</script>

<style scoped>
/*模块1：mtcnn*/
.test1 {
  display:flex;
}
.test1 img {
  padding:3% 5% 3% 5%;
}
.test1 span{
  font-size: 20px;
  color:#333;
  font-weight: bold;
  width:100px;
}
.test1 .test11{
  margin:auto;
}
/*模块2：yolov5*/
.test2 {
  display:flex;
}
.test2 img {
  padding:3% 5% 3% 5%;
}
.test2 span{
  font-size: 20px;
  color:#333;
  font-weight: bold;
  width:100px;
}
.test2 .test22{
  margin:auto;
}
.main {
  width:100%;
  height:860px;
}
/*分割线*/
.tableTitle {
    position: relative;
    margin:auto;
    width: 1000px;
    height: 2px;
    background-color: #d4d4d4;
    text-align: center;
    color: rgba(101, 101, 101, 1);
}

</style>