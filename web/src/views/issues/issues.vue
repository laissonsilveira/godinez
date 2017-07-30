<template src="./issues.html"></template>
<style src="./issues.css"></style>
<script>
  import IssuesController from "../../controllers/issuesController";
  import Vue from "vue";

  const controller = new IssuesController(Vue.http);

  let data = {
    issues: [{}]
  }

  export default {
    name: "app",
    data: () => {
      return data;
    },
    methods: {
      getIssues: () => {
        return controller.findAll((issues) => {
          console.log("issues: ", issues);
          data.issues = issues;
        });
      }
    },
    mounted: function () {
      this.getIssues();
    }
  }
</script>