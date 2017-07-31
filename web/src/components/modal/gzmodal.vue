<template src="./gzmodal.html"></template>
<style src="./gzmodal.css"></style>
<script>
  import $ from "jquery"

  export default {
    name: "gzmodal",
    methods: {
      openModal () {
        $("#gzmodal").modal("open");
      },
      closeModal () {
        $("#gzmodal").modal("close");
      }
    },
    mounted () {
      $(".modal").modal();
      this.openModal();
    }
  }
</script>
