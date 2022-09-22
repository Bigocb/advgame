<script>
import Posts from "../components/Posts.vue";
export default {
  components: {Posts}
}
</script>

<template>
  <main>
    <Posts />
  </main>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
