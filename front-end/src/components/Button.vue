<template>
<!--  根据鼠标轨迹在按钮上的横坐标变换颜色的按钮-->
<!--  hsl三个参数分别为：色调、饱和度、亮度，其中横坐标决定色调-->
  <div
  @mousemove="onMousemove"
  :style="{ backgroundColor: `hsl(${x}, 70%, 80%)` }"
  class="movearea"
>
  </div>
</template>

<script>
export default {
  //x的初始坐标为0
  data() {
    return {
      x: 0
    }
  },
  //定义获取坐标的方法
  methods: {
    onMousemove(e) {
      //获取水平坐标并赋值给x
      this.x = e.clientX
    }
  }
}
</script>

<style scoped lang="less">
//定义按钮css
.movearea {
  width:198px;
  height:50px;
  border-radius: 10px;
  transition: 0.3s background-color;
}
</style>

