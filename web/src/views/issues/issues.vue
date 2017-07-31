<template src="./issues.html"></template>
<style scoped src="./issues.css"></style>
<script>
  import IssuesController from "../../controllers/issuesController";
  import Vue from "vue";
  import Gzmodal from "../../components/modal/gzmodal";
  const controller = new IssuesController(Vue.http);

  export default {
    name: "issues",
    components: { Gzmodal },
    data () {
      return {
        issues: [{}]
      }
    },
    methods: {
      getIssues () {
        return controller.findAll((issues) => {
          this.issues = issues;
        });
      },
      createIssue () {
        console.log("createIssue issues cx!");
      }
    },
    mounted: function () {
      this.getIssues();
    }
  }
</script>