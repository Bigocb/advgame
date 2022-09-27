<template>
<!--  <h1>Vue 3 and Fetch Example</h1>-->
<!--  &lt;!&ndash;  {{data}}&ndash;&gt;-->
<!--  <ul v-if="!loading && data && data.length">-->
<!--    <li v-for="post of data">-->
<!--      <p><strong>{{ post['title'] }}</strong></p>-->
<!--      <p></p>-->
<!--    </li>-->
<!--  </ul>-->
  <div class="row">
  <input
      v-model="sample"
      :placeholder=sample
  />
<!--  <input v-model="seed" placeholder="Enter seed count" />-->
  <!--  <argon-input placeholder="Type here..." />-->
  <button type="button" v-on:click="genEntry({sample})">Add</button>
  </div>
  <div class="row">&nbsp;</div>
  <div class="row">
<input
    v-model="message"
    :placeholder=message
/>
<!--  <argon-input placeholder="Type here..." />-->
  <button type="button" v-on:click="testPost({message})">Add</button>
  </div>
</template>

<script>
import {ref, onMounted} from "vue";
import axios from 'axios'

export default {
  name: 'Posts',
  sample: null,
  message: null,
  components: {},
  tag_message: "Enter Tag",
  sample_message: "Enter Sample",
  props: {},
  // rep: {},
  data () {
    return {
      sample: "enter sample",
      message: "enter tag"
    }
  },
  setup() {
    const data = ref(null);
    const loading = ref(true);
    const error = ref(null);

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
        const article = {tag: tag['message']};
        axios.post("http://127.0.0.1:5000/tag", article)
            .then(function (response) {
              // this.articleId = response.data.id;
              console.log(response.data)
              this.results = response.data
              return response.data;
            })
            .catch ( function (error){
              console.log(error);
        });
        this.sample = null
        this.message = null
      },
    genEntry(sample) {
      // const data = ref(null);

      // console.log(tag)
      // Simple POST request with a JSON body using axios
      const sampleInfo = {sample: sample['sample'], seedCount: 10};
      console.log(sampleInfo)
      axios.post("http://127.0.0.1:5000/generate", sampleInfo)
          .then(function (response) {
            // this.articleId = response.data.id;
            console.log(response.data)
            this.results = response.data
            return response.data;
          })
          .catch ( function (error){
            console.log(error);
          });
    }
  }
}
</script>