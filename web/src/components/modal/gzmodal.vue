<template src="./gzmodal.html"></template>
<style src="./gzmodal.css"></style>
<script>
  import $ from "jquery";
  import { bus } from "../../main";

  export default {
    name: "gzmodal",
    props: {
      title: {
        type: String
      }
    },
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

      bus.$on('openModal', () => {
        this.openModal();
      });
    }
  }
</script>
