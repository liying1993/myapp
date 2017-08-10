<template>
    <div class="wrapper">

        <el-row id="topbar">
            <el-col :span="6" class="topleft">
                <div class="grid-content bg-purple-dark">

                <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
                    <el-menu-item index="1">首页</el-menu-item>
                    <el-menu-item index="2"><a href="https://www.ele.me" target="_blank">python开发</a></el-menu-item>
                    <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">社区</a></el-menu-item>
                    <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">教程</a></el-menu-item>
                    <el-submenu index="5">
                        <template slot="title">速查表</template>
                        <el-menu-item index="2-1">选项1</el-menu-item>
                        <el-menu-item index="2-2">选项2</el-menu-item>
                        <el-menu-item index="2-3">选项3</el-menu-item>
                    </el-submenu>

                </el-menu>
            </div>
            </el-col>

            <el-col :span="6" class="topmiddle"><div class="grid-content bg-purple-dark"><el-input placeholder="搜索" icon="search"></el-input></div></el-col>
            <el-col :span="6" class="topright"><div class="grid-content bg-purple-dark">
                <el-button type="success">登陆</el-button>
                <el-button type="success">注册</el-button>
            </div></el-col>

            <el-col :span="6" class="content">
                <router-view></router-view>
            </el-col>
        </el-row>


        <div class="index_content">
            <div class="content_left">dsds</div>
            <div class="content_right">dsds</div>
        </div>

        <div class="sideserver">
            <!-- Table -->
            <el-button type="text" @click="dialogTableVisible = true">客服<i class="el-icon-more"></i></el-button>

            <el-dialog title="对话中..." :visible.sync="dialogTableVisible">
                <el-input type="textarea" :rows="5"></el-input>
                <el-input v-model="input" placeholder="请输入内容"></el-input>
                <el-button type="primary">主要按钮</el-button>

            </el-dialog>
        </div>

    </div>

</template>

<script>
    export default {
        data () {
          return {
              dialogTableVisible: false,


          }
        },
        methods:{
            startDialog () {
                this.$prompt('请输入邮箱', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
                    inputErrorMessage: '邮箱格式不正确'
                }).then(({ value }) => {
                    this.$message({
                        type: 'success',
                        message: '你的邮箱是: ' + value
                    });
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '取消输入'
                    });
                });
            }
        },
    };
</script>

<style lang="scss">
    @import "../assets/scss/main";

    #log {
        width: 440px;
        height: 200px;
        border: 1px solid #7F9DB9;
        overflow: auto;
    }

    #msg {
        width: 330px;
    }
    .wrapper {
        .sideserver {
            width: 100px;
            height: 100px;
            background-color: #13ce66;
            margin-top: 800px;
            margin-left: 1300px;
            z-index: 999;
            position: absolute;
        }
        .index_content{
            width: 100%;
            height: 100%;
            margin:0 auto;
            background-color: #eaf0f0;
            position: fixed;

            /*left: 150px;*/
            .content_left{
                width: 750px;
                height:100%;
                position: absolute;
                /*height: 40%;*/
                background-color: #ffffff;
                margin-left: 220px;
                border: 1px solid #cdd1d6;
            };
            .content_right{
                width: 248px;
                height: 100%;
                /*height:40%;*/
                background-color: #b8c0c8;
                margin-left: 980px;
                border: 1px solid #cdd1d6;
                position: absolute;
            }
        };
        .el-row{
            background-color: #324157;
        };

        #topBar {
            background-color: #324157;

            /*height: 40px;*/
            /*.title {*/
                /*font-size: 100px;*/
            /*}*/
        }
        .topleft{
            width: 550px;
            margin-right: 20px;
            margin-left: 70px;
            .grid-content{
                padding-right: 20px;
            }
        }
        .topmiddle{
            width: 400px;
            margin-top: 13px;
        }
        .topright{
            width: 300px;
            margin-top: 13px;
            margin-left: 100px;
        }
    }
    /*.el-col-12 {*/
        /*width: 100%;*/
    /*}*/
    /*.el-col-6 {*/
         /*width: 33%;*/
     /*}*/


</style>
