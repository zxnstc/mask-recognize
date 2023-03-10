<template>
<div id="background">
    <!-- 星空背景-->
    <div class="stars">
        <div class="star" v-for="(item,index) in starsCount" :key="index" ref="star"></div>
    </div>
    <!-- 登录部分-->
    <div class="container">
        <form action="">
          <h1>口罩佩戴监测系统登录窗口</h1>
          <div class="form">
              <div class="item">
                <!-- v-model把输入的值传输给name变量 -->
                <label>用户名：</label><input type="text" v-model.trim="name"
                                          placeholder="请输入用户名">
                <br/>
              </div>
              <div class="item">
                <label>密码：</label><input type="password" v-model.trim="password"
                                         placeholder="请输入密码">
                <br/>
              </div>
          </div>
        </form>
        <!-- 点击按钮触发handlelogin方法 -->
        <button type="submit" @click.prevent="handlelogin">登录</button>
    </div>
</div>
</template>

<script>
export default {
  data(){
    return{
      //定义星星的数量与间距
      starsCount:1000,
      distance:800,
    };
  },
    //实现星星的运动
    mounted() {
    //绑定组件
    let starArr=this.$refs.star
    //调用数组中每个元素
    starArr.forEach(item=>{
      var distance = this.distance+(Math.random()*300)
      //设置旋转的基点
      item.style.transformOrigin=`0 0 ${distance}px`
      item.style.transform=`translate3d(0,0,-${distance}px)
      rotateY(${(Math.random()*360)}deg) rotateX(${(Math.random()*(-80))}deg)`
    })
  },
  methods:{
    handlelogin:function()
    {
      //进行匹配
      if(this.name==='zrgjdzjz' && this.password==='123456')
       {
         this.$router.replace('/layout');//成功匹配则跳转至主页面
       }
       else if(this.name==='')//如果提交用户名为空
       {
         alert('用户名不为空');
       }
       else if(this.password==='')//如果提交密码为空
       {
         alert('密码不为空');
       }
      else{
        alert('账号不存在，请注册后登录');//如果匹配失败
        }
    },
  }
};
</script>

<style scoped>
#background{
  width: 100%;
  min-width: 1200px;
  height: 800px;
  /*径向渐变*/
  background: radial-gradient(ellipse at bottom, #383c3d 10%, #090a0f 100%);
  /*溢出隐藏*/
  overflow: hidden;
  position: relative;
}
.container{
  width: 480px;
  height: 300px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background: rgba(0, 0, 0, 0.5);
  text-align: center;
  border-radius: 20px;
  margin-top: 10px;
}
.container h1{
  margin-top: 5%;
  color: aliceblue;
  margin-left: 20px;
}
.container button{
  margin-top: 5%;
}
.item {
  color: white;
  margin-left: 15%;
  margin-top: 35px;
  font-size: 20px;
  text-align: left;
}
.item label{
  float:left;
  width: 5em;
  margin-right: 1em;
  text-align: right;
}
.form{
  margin-top: 5%;
}
/*登录输入框css*/
input{
  margin-left: -5px;
  padding: 4px;
  border: solid 2px #006bc2;
  border-radius: 10px;
  outline: 0;
  width: 200px;
  height: 23px;
}
/*登录按钮*/
button{
  position: relative;
  height: 33px;
  width: 100px;
  background: rgba(35, 19, 252, 0.5);
  border-radius: 10px;
  margin-top: 18px;
  color: white;
  margin-left: 40px;
  margin-right: 10px;
}
/*星空部分css*/
.stars{
    transform: perspective(800px);
    transform-style: preserve-3d;
    position: absolute;
    left: 50%;
    /*动画属性，控制速度；infinite 动画播放无限次；linear从头到尾速度相同*/
    animation: rotate 70s infinite linear;
    /*调整位置 让星星处于屏幕中间*/
    bottom: -300px;
  }
/*定义star属性*/
.star{
  width: 2px;
  height: 2px;
  background: #ffffff;
  position: absolute;
  top: 0;
  left: 0;
}
/*无限旋转 rorate为动画名称*/
@keyframes rotate {
  /*0%为动画的开始时间*/
  0%{
    /*css样式,perspective为视距，rotate*为移动距离*/
    transform: perspective(600px) rotateZ(20deg) rotateX(-40deg) rotateY(0);
  }
  /*100%为动画的结束时间*/
  100%{
    transform: perspective(600px) rotateZ(20deg) rotateX(-40deg) rotateY(-360deg);
  }
}
</style>
