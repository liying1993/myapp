<template>
<div>
<button @click="aaaaa">sasa</button>
</div>
</template>

<script>
import request from '../lib/request';

export default {
name: 'app',
data () {
return {
}
},
methods: {
async aaaaa () {
let bodyPra = {
telephone:"15623652325",
password:"123456"
};
console.log(bodyPra);
//let result = await request.register_post(bodyPra);
let result = await request.lianlian_get();
console.log(result.data);
//      axios.get("http://127.0.0.1:5000").then(function(r) {
//        alert(r.data)
//      });
}
}
}
</script>