<template>
    <div>
        <!-- 顶部通栏 -->
        <AppTopNav fixed/>
        <!-- 背景图 -->
        <div class="aboutbg">
            <div class="aboutword1">
                关于
            </div>
            <div class="aboutword2">
                制作者：17组——带资进组
            </div>
        </div>
        <!-- footer -->
        <MyFooter>fixed</MyFooter>
    </div>
</template>

<script>
import AppTopNav from '@/components/AppTopNav.vue';
import MyFooter from '@/components/MyFooter.vue';
export default{
    components:{
    AppTopNav,
    MyFooter,
  }
}
</script>

<style lang="less" scoped>
.aboutbg{
    box-sizing: border-box;
    width:100%;
    height:680px;
    background: no-repeat url("../assets/images/bg-img3.jpg");
    display: flex;
    align-items: center;
}
.aboutword1{
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-30%,-30%);
    font-size: 50px;
    color: #fff;
    font-weight: bold;
}
.aboutword2{
    position: absolute;
    top: 50%;
    left: 45%;
    transform: translate(-30%,-30%);
    font-size: 30px;
    color: #fff;
    font-weight: bold;
}
</style>