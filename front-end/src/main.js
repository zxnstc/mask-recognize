import { createApp, VueElement } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.withCredentials = true

// 引入初始化样式
import '@/assets/styles/base.css'

import installElementPlus from './plugins/element'

const app = createApp(App)
installElementPlus(app)
app.use(store).use(router).mount('#app')