<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <card
                :title="stats.clients.title"
                :value=total
                :iconClass="stats.clients.iconClass"
                :iconBackground="stats.clients.iconBackground"
                :percentageColor="stats.clients.percentageColor"
                :detail="stats.clients.detail"
                directionReverse
            ></card>
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.money.title"
              :value=tbp
              :iconClass="stats.money.iconClass"
              :iconBackground="stats.money.iconBackground"
              :detail="stats.users.detail"
              directionReverse
            >

</card>
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.users.title"
              :value=keep
              :percentage=metrics.keep_per
              :iconClass="stats.users.iconClass"
              :iconBackground="stats.users.iconBackground"
              :detail="stats.users.detail"
              directionReverse
            ></card>
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <card
              :title="stats.sales.title"
              :value=remove
              :percentage=metrics.remove_per
              :iconClass="stats.sales.iconClass"
              :iconBackground="stats.sales.iconBackground"
              :detail="stats.sales.detail"
              directionReverse
            ></card>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-12 mb-lg" >
<!--            <card height="200%"-->
<!--                title="Entry"-->
<!--                  style="min-height: 10rem;"-->
<!--                  class="mb-2"-->
<!--                :value=text-->
<!--                :badge="{ text: 'Moderate', color: 'success' }"-->
<!--                :iconClass="stats.sales.iconClass"-->

<!--            >-->
<!--            </card>-->
            <textarea style="width: 100%; height: 75%"  v-model="text" placeholder="add multiple lines"></textarea>

            <button @click="keepRemove(true,{ id })">Keep</button>
            <button @click="keepRemove(false,{ id })">Remove</button>
            <button @click="editEntry(text,{ id })">Edit</button>
            </div>

        </div>
        </div>
        <div class="row mt-4">
          <div class="col-lg-12 mb-lg-0 mb-4">
            <div class="card">
              <div class="p-3 pb-0 card-header">
                <div class="d-flex justify-content-between">
                  <h6 class="mb-2">Entries by Sample and Model</h6> <input type="text"
                                                                           placeholder="Filter by department or employee"
                                                                           v-model="filter" />
                </div>
              </div>
              <div class="table-responsive">
                <table class="table align-items-center">
                  <tbody>
                    <tr v-for="(sale, index) in filteredRows" :key="index">
                      <td class="w-30">
                        <div class="px-2 py-1 d-flex align-items-center">
                          <div class="ms-4">
                            <p class="mb-0 text-xs font-weight-bold">Sample:</p>
                            <h6 class="mb-0 text-xxs">{{ sale['sample'] }}</h6>
                          </div>
                        </div>
                      </td>
                      <td class="w-30">
                        <div class="px-2 py-1 d-flex align-items-center">
                          <div class="ms-4">
                            <p class="mb-0 text-xs font-weight-bold">Model:</p>
                            <h6 class="mb-0 text-xxs">{{ sale['model'] }}</h6>
                          </div>
                        </div>
                      </td>
                      <td>
                        <div class="text-center">
                          <p class="mb-0 text-xs font-weight-bold">Keep:</p>
                          <h6 class="mb-0 text-xxs">{{ sale['keep'] }}</h6>
                        </div>
                      </td>
                      <td class="text-sm align-middle">
                        <div class="text-center col">
                          <p class="mb-0 text-xs font-weight-bold">Total:</p>
                          <h6 class="mb-0 text-xxs">{{ sale['total'] }}</h6>
                        </div>
                      </td>
                      <td>
                        <div class="text-center">
                          <p class="mb-0 text-xs font-weight-bold">% Kept:</p>
                          <h6 class="mb-0 text-xxs">{{ sale['per'] }}</h6>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
<!--          <div class="col-lg-5">-->
<!--            <categories-card />-->
<!--          </div>-->
        </div>
      </div>
    </div>
</template>
<script>
import Card from "@/examples/Cards/Card.vue";
import { cacheAdapterEnhancer } from 'axios-extensions';
// import https from 'https';
// import GradientLineChart from "@/examples/Charts/GradientLineChart.vue";
// import Carousel from "./components/Carousel.vue";
// import CategoriesCard from "./components/CategoriesCard.vue";

import US from "@/assets/img/icons/flags/US.png";
import DE from "@/assets/img/icons/flags/DE.png";
import GB from "@/assets/img/icons/flags/GB.png";
import BR from "@/assets/img/icons/flags/BR.png";
import axios from "axios";

const http = axios.create({
  baseURL: '/',
  headers: { 'Cache-Control': 'no-cache' },
  // cache will be enabled by default
  adapter: cacheAdapterEnhancer(axios.defaults.adapter)
});

export default {
  name: "dashboard-default",
  data() {
    return {
      filter: '',
      resp : null,
      resp_entry: null,
      total: null,
      id: null,
      resultsL: null,
      sample: null,
      interval: null,
      interval_entry: null,
      tbp: null,
      keep: null,
      texts: null,
      messages: null,
      metrics: {
        keep_per: null,
        remove_per: null
      },
      samples: null,
      remove: null,
      text: null,
      stats: {
        money: {
          title: "To Be Processed",
          value: "met",
          // percentage: "+55%",
          iconClass: "ni ni-money-coins",
          // detail: "since yesterday",
          iconBackground: "bg-gradient-primary",
        },
        users: {
          title: "Entries Kept",
          value: "2,300",
          percentage: "+3%",
          iconClass: "ni ni-world",
          iconBackground: "bg-gradient-danger",
          detail: "percent",
        },
        clients: {
          title: "Total Entries",
          value: "+3,462",
          percentage: "-2%",
          iconClass: "ni ni-paper-diploma",
          percentageColor: "text-danger",
          iconBackground: "bg-gradient-success",
          detail: "since last quarter",
        },
        sales: {
          title: "Entries Removed",
          value: "$103,430",
          percentage: "+5%",
          iconClass: "ni ni-cart",
          iconBackground: "bg-gradient-warning",
          detail: "percent",
        },
      },
      sales: {
        us: {
          country: "United States",
          sales: 2500,
          value: "$230,900",
          bounce: "29.9%",
          flag: US,
        },
        germany: {
          country: "Germany",
          sales: "3.900",
          value: "$440,000",
          bounce: "40.22%",
          flag: DE,
        },
        britain: {
          country: "Great Britain",
          sales: "1.400",
          value: "$190,700",
          bounce: "23.44%",
          flag: GB,
        },
        brasil: {
          country: "Brasil",
          sales: "562",
          value: "$143,960",
          bounce: "32.14%",
          flag: BR,
        },
      },
    };
  },
  beforeMount() {
    this.getEntry();
  },
  created() {
    this.interval = setInterval(this.getMetrics, 1000)
  },
  beforeUnmount () {
    clearInterval(this.interval)
    // clearInterval(this.interval_entry)
  },
  components: {
    Card,
    // GradientLineChart,
    // Carousel,
    // CategoriesCard,
  },
  computed: {
    filteredRows() {
      return this.samples.filter(row => {
        const sample = row.sample.toString().toLowerCase();
        // const text = row.text.toLowerCase();
        const searchTerm = this.filter.toLowerCase();
        // console.log('--------------')
        // console.log(sample)
        // console.log(searchTerm)
        return sample.includes(searchTerm);
      });
    }
  },
  methods: {
    async getEntry() {
      // const data = ref(null);
      console.log("------------------")
      // Simple POST request with a JSON body using axios
      const response = await http.get("https://api.cldevlab.shop/process",{ cache: false });
      this.resp_entry = response.data
      // console.log(this.resp_entry)
      this.text = this.resp_entry.text
      this.id = this.resp_entry.id
    },
    editEntry(text, id) {
      // console.log("--------------")
      console.log(text,id)
      const texts = {text: text, id: id};
      // const ids = {id: id};
      http.post("https://api.cldevlab.shop/edit", texts,{ cache: false })
          .then(function (response) {
            // this.articleId = response.data.id;
            console.log(response.data)
            // this.results = response.data
            return response.data;
          })
          .catch ( function (error){
            console.log(error);
          });
      this.keepRemove(true,id)
      // this.getEntry()
    },
    getMetrics() {
      // const data = ref(null);

      // console.log(tag)
      // Simple POST request with a JSON body using axios
      http.get("https://api.cldevlab.shop/metrics",{ cache: false })
          .then(response => this.resp = response.data);
      console.log(this.resp)
      this.total = this.resp.total
      this.tbp = this.resp.tbp
      this.keep = this.resp.keep
      this.remove = this.resp.Remove
      this.samples  = this.resp.samples
      this.metrics.keep_per = ((this.resp.keep/this.resp.total)*100).toFixed(2)
      this.metrics.remove_per = ((this.resp.remove/this.resp.total)*100).toFixed(2)
    },
    keepRemove(keep, id) {
      // const data = ref(null);
      console.log(keep, id)
      // Simple POST request with a JSON body using axios
      const article = {keep: keep, id: id};
      // const ids = {id: id};
      http.post("https://api.cldevlab.shop/keep", article,{ cache: false })
          .then(function (response) {
            // this.articleId = response.data.id;
            // console.log(response.data)
            // this.results = response.data
            return response.data;
          })
          .catch ( function (error){
            console.log(error);
          });
      this.getEntry()
    }

}}
</script>
