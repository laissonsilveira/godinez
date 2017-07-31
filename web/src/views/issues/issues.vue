<template src="./issues.html"></template>
<style scoped src="./issues.css"></style>
<script>
  import IssuesController from "../../controllers/issuesController";
  import Gzmodal from "../../components/modal/gzmodal";
  import { bus } from "../../main"

  export default {
    name: "issues",
    components: { Gzmodal },
    data () {
      return {
        issues: [],
        issue: {
          title: "New Title"
        }
      }
    },
    methods: {

      getIssues () {
        return this.controller.findAll((issues) => {
          this.issues = issues;
        });
      },

      createIssue () {
        bus.$emit("openModal");
      },

      saveIssue () {
        this.controller.save(this.issue, () => {
          this.getIssues();
        });
      }

    },
    mounted () {
      this.controller = new IssuesController(this.$http);
      this.getIssues();
    }
  }
</script>