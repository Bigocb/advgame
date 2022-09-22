<template>
<!--  <h1>Vue 3 and Fetch Example</h1>-->
<!--  &lt;!&ndash;  {{data}}&ndash;&gt;-->
<!--  <ul v-if="!loading && data && data.length">-->
<!--    <li v-for="post of data">-->
<!--      <p><strong>{{ post['title'] }}</strong></p>-->
<!--      <p></p>-->
<!--    </li>-->
<!--  </ul>-->

  <p v-if="loading">
    Still loading..
  </p>
  <p v-if="error">

  </p>
<input v-model="message" placeholder="edit me">
  <button type="button" v-on:click="testPost({message})">Add</button>
{{ results }}
</template>

<script>
import {ref, computed, onMounted} from "vue";
import axios from 'axios'

export default {
  name: 'Posts',
  props: {},
  // rep: {},
  setup() {
    const data = ref(null);
    const loading = ref(true);
    const error = ref(null);

    // function fetchData() {
    //   loading.value = true;
    //   // I prefer to use fetch
    //   // you can use use axios as an alternative
    //   return axios.get('http://jsonplaceholder.typicode.com/posts')
    //       .then(res => {
    //         // a non-200 response code
    //         console.log(res)
    //         if (res.status != 200) {
    //           // create error instance with HTTP status text
    //           // console.log('test')
    //           const error = new Error(res.statusText);
    //           error.json = res.status;
    //           throw error;
    //         }
    //         return res.data;
    //       })
    //       .then(json => {
    //         // set the response data
    //         // console.log(json)
    //         data.value = json;
    //         console.log(data)
    //
    //       })
    //       .catch(err => {
    //         error.value = err;
    //         console.log(err)
    //         // In case a custom JSON error response was provided
    //         if (err.json) {
    //           return err.json.then(json => {
    //             // set the JSON response message
    //             error.value.message = json.message;
    //           });
    //         }
    //       })
    //       .then(() => {
    //         loading.value = false;
    //       });
    // }

    onMounted(() => {
      // fetchData();
    });

    return {
      data,
      loading,
      error
    };
  },
  methods: {
    testPost(tag) {
      // const data = ref(null);

      // console.log(tag)
        // Simple POST request with a JSON body using axios
        const article = {tag: tag['message']};
        axios.post("http://127.0.0.1:5000/tag", article)
            .then(function (response) {
              // this.articleId = response.data.id;
              console.log(response.data)
              // this.results = response.data
              return response.data;
            })
            .catch ( function (error){
              console.log(error);
        });
      }
  }
}
</script>