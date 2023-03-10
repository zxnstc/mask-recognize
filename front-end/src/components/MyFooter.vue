<template>
  <!-- 固定footer-->
  <div class="footer">
    <span class="word">© 2022</span>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="less" scoped>
@import url('../assets/styles/variable.less');

.footer {
  background-color: @xTxColor;
  height: 35px;
  margin-bottom: 0;
  text-align: center;
}
.word{
    color:#fff;
    font-size: 14px;
    text-align: center;
}
</style>