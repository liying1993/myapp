<template>
    <div>
        <el-form ref="form"  label-width="80px">
            <el-form-item v-model="version" label="版本号">
                <el-input></el-input>
            </el-form-item>
            <el-form-item v-model="oid_partner" label="商户编号">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="user_id" label="用户id">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="timestamp" label="时间戳">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="sign_type" label="签名方式">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="sign" label="签名">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="busi_partner" label="商户业务类型">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="no_order" label="商户唯一订单号">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="dt_order" label="商户订单时间">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="name_goods" label="商品名称">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="money_order" label="交易金额">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="notify_url" label="服务器异步通知地址">
                <el-input></el-input>
            </el-form-item>

            <el-form-item v-model="risk_item" label="风险控制参数">
                <el-input></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="gopay">立即创建</el-button>
                <el-button>取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    import request from "../lib/request";
    import axios from 'axios';

    export default {
        data () {
            return {
                version: '',
                oid_partner: '',
                user_id: '',
                timestamp: '',
                sign_type: '',
                sign:'',
                busi_partner:'',
                no_order:'',
                dt_order:'',
                name_goods:'',
                money_order:'',
                notify_url:'',
                risk_item:'',
            }
        },
        methods: {
            async gopay () {
                let urlbar = {
                    version: this.version ,
                    oid_partner: this.oid_partner,
                    user_id: this.user_id,
                    timestamp: this.timestamp,
                    sign_type: this.sign_type,
                    sign:this.sign,
                    busi_partner:this.busi_partner,
                    no_order:this.no_order,
                    dt_order:this.dt_order,
                    name_goods:this.name_goods,
                    money_order:this.money_order,
                    notify_url:this.notify_url,
                    risk_item:this.risk_item
                };
                axios.get("https://cashier.lianlianpay.com/payment/bankgateway.htm").then(function(r){
                    alert(r.data);
                });

            }
        }
    }
</script>
