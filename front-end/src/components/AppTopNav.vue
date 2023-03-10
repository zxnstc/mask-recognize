<template>
    <div class="app-top-nav">
        <div class="w">
        <!-- 定义菜单列表 -->
            <ul>
              <li>
                <a href="http://localhost:8080/#/layout">
                <i class="iconfont icon-shouyefill"></i>
                  首页
                </a>
              </li>
              <li>
                <a href="http://localhost:8080/#/user">
                <i class="iconfont icon-xinrenzhinan"></i>
                  用户
                </a>
              </li>
              <li>
                <a href="http://localhost:8080/#/twomethods">
                <i class="iconfont icon-kaishi"></i>
                  开始体验
                </a>
              </li>
              <li>
                <a href="http://localhost:8080/#/about">
                <i class="iconfont icon-guanyu"></i>
                  关于
                </a>
              </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default{

}
</script>

<style lang="less" scoped>
//引入颜色设定文件
@import url('../assets/styles/variable.less');

.app-top-nav{
    //使用已定义的主题颜色，便于更改
    background-color:@xTxColor;
    ul{
        height: 38px;
        line-height: 38px;
        //弹性布局，默认按行排列
        display: flex;
        //从末端开始
        justify-content: flex-end;
        li{
            a{
                padding: 0 10px;
                color:#fff;
                border-left: 1px solid #fff;
                &:hover{
                    color: @helpColor;
                }
            }
        }
    }
}

</style>