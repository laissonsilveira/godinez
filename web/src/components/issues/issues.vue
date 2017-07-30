<template src="./issues.html"></template>
<style src="./issues.css"></style>
<script>
  export default {
    name: "app",
    created: () => {
    },
    methods: {
    },
    data: () => {
      let data = [];
      data.push({
        title: "Titulo 1",
        description: "Description 1"
      });
      data.push({
        title: "Titulo 2",
        description: "Description 2"
      });
      data.push({
        title: "Titulo 3",
        description: "Description 3"
      });
      data.push({
        title: "Titulo 4",
        description: "Description 4"
      });
      data.push({
        title: "Titulo 5",
        description: "Description 6"
      });
      return data;
    }
  }
</script>