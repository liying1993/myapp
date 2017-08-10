import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui'
import Vuex from 'vuex'


Vue.use(ElementUI);
Vue.use(VueRouter);
Vue.use(Vuex);
Vue.config.debug = true;

import pageRegister from './page/register.vue';
import pageChatClient from './page/chat_client.vue';
import pageTest from  './page/test.vue';
import pageIndex from './page/index.vue';

const router = new VueRouter({routes:[

    {
        path: '/',
        component: pageIndex,
        children: [
            {
                path:'/register',
                component:pageRegister
            },
            {
                path:'/chat_client',
                component:pageChatClient
            },
            {
                path:'/test',
                component:pageTest
            }
        ]
    }
    // {
    //   path:'/register',
    //   component:pageRegister
    // },
    // {
    //   path:'/chat_client',
    //   component:pageChatClient
    // },
    // {
    //   path:'/test',
    //   component:pageTest
    // }
]});

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
