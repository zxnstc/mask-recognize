import { createRouter, createWebHashHistory } from 'vue-router'
import Layout from '@/views/Layout.vue'
const Login=()=>import('@/views/Login.vue')
const About=()=>import('@/views/About.vue')
const HomeView=()=>import('@/views/HomeView.vue')
const HomeView2=()=>import('@/views/HomeView2.vue')
const twoMethods=()=>import('@/views/twoMethods.vue')
const user=()=>import('@/views/user')

//配置路由
const routes = [
  {
    path: '/',
    name:'login',
    component: Login,
  },{
    path: '/layout',
    component:Layout,
  },{
    path: '/about',
    name:'About',
    component:About
  },{
    path: '/homeview',
    component:HomeView
  },{
    path: '/homeview2',
    component:HomeView2
  },{
    path: '/twomethods',
    component:twoMethods
  },{
    path: '/user',
    component:user
  }
]

//使用vue的HASH模式
const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
