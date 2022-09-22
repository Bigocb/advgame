<template>
  <div class="about">
     <div id ='input-container'>
    <div>
      <!--element which is going to render the TextBox-->
      <p>Message is: {{ message }}</p>
      <input v-model="message" placeholder="edit me" />
    </div>
     </div>
  </div>
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

<script>
export default {
  data() {
    return {
      message: ''
    }
  }
}
</script>
