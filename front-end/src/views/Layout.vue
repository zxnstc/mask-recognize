<template>
    <div>
        <!-- 顶部通栏 -->
        <AppTopNav/>
        <!-- main -->
        <div class="main">
            <span class="sent">动态场景下口罩佩戴监测与特效提醒系统:)</span>
        </div>
        <!-- part2标题-->
        <h2 style="text-align: center;line-height: 200px;">小组成员</h2>
        <!-- part2内容-->
        <div class="member" style="display: flex;justify-content: space-around;height: 450px;">
          <div class="ig" id="zjr">
            <img src="../assets/images/zjr.jpg" style="flex-direction: row;">
            <h3 style="flex-direction: row;text-align: center;line-height: 100px;">张家冉</h3>
          </div>
          <div class="ig" id="zrc">
            <img src="../assets/images/zrc.png" style="flex-direction: row;">
            <h3 style="flex-direction: row;text-align: center;line-height: 100px;">张若迟</h3>
          </div>
          <div class="ig" id="zyz">
            <img src="../assets/images/zyz.jpg" style="flex-direction: row;">
            <h3 style="flex-direction: row;text-align: center;line-height: 100px;">张怡桢</h3>
          </div>
          <div class="ig" id="wyf">
            <img src="../assets/images/wyf.jpg" style="flex-direction: row;">
            <h3 style="flex-direction: row;text-align: center;line-height: 100px;">吴祎璠</h3>
          </div>
        </div>
        <!-- bottom -->
        <my-footer>fixed</my-footer>
    </div>
</template>

<script>
import AppTopNav from '@/components/AppTopNav.vue';
import MyFooter from "@/components/MyFooter";

export default{
  name:'layout',
    components:{
      MyFooter,
    AppTopNav
  }
}
</script>

<style lang="less" scoped>
//设置主图背景
.main {
  box-sizing: border-box;
  width:100%;
  height:680px;
  background: no-repeat url("../assets/images/bg-img2.jpg");
  display: flex;
  align-items: center;
}
//设置文字css
.sent{
  width:640px;
    position: absolute;
    top: 25%;
    left: 5%;
    color: #fff;
    font-size: 50px;
    font-weight: bold;
    text-align: center;
}

</style>