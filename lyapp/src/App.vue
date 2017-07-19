<template>
  <div id="app">
    <button @click="aaaaa">sasa</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'app',
  data () {
    return {
    }
  },
  methods: {
    aaaaa () {
      axios.get("http://127.0.0.1:5000").then(function(r) {
        alert(r.data)
      });
    }
  }
}
</script>
