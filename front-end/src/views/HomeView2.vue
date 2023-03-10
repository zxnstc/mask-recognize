<template>
  <div>
    <!-- 顶部通栏 -->
    <AppTopNav/>
    <!--    main-->
    <div style="width: 100%">
    <!--静态html资源-->

    <div>
      <iframe
        src="http://127.0.0.1:5004"
        scrolling="auto"
        frameborder="0"
        style="width: 100%; height: 900px"
      ></iframe>
    </div>
  </div>
    <!-- bottom -->
    <my-footer>fixed</my-footer>
  </div>
</template>

<script>
import MyFooter from "@/components/MyFooter";
import AppTopNav from '@/components/AppTopNav.vue';
export default {
  name: "HomeView2",
  components: {
    MyFooter,
    AppTopNav
  }
}
</script>

<style scoped>

</style>