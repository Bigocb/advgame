<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-12 mb-lg">
            <div class="card">
              <Toolbar class="mb-4">
                <template #start>
                  <Button label="New" icon="pi pi-plus" class="p-button-success mr-2" @click="openNew" />
                  <Button label="Delete" icon="pi pi-trash" class="p-button-danger" @click="confirmDeleteSelected" :disabled="!selectedProducts || !selectedProducts.length" />
                </template>

                <template #end>
                  <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" label="Import" chooseLabel="Import" class="mr-2 inline-block" />
                  <Button label="Export" icon="pi pi-upload" class="p-button-help" @click="exportCSV($event)"  />
                </template>
              </Toolbar>

              <DataTable ref="dt" :value="cars" v-model:selection="selectedProducts" dataKey="id"
                         :paginator="true" :rows="10" :filters="filters"
                         paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[5,10,25]"
                         currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" responsiveLayout="scroll">
                <template #header>
                  <div class="table-header flex flex-column md:flex-row md:justiify-content-between">
                    <h5 class="mb-2 md:m-0 p-as-md-center">Manage Products</h5>
                    <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global'].value" placeholder="Search..." />
                        </span>
                  </div>
                </template>

<!--                <Column selectionMode="multiple" style="width: 3rem" :exportable="false"></Column>-->
<!--                <Column field="id" header="Id" :sortable="true"></Column>-->
<!--                <Column field="seed" header="Seed" :sortable="true"></Column>-->
<!--                <Column field="sample" header="Sample" :sortable="true"></Column>-->
                <Column field="text" header="Text" :sortable="true">
<!--                  <template #body="slotProps">-->
<!--                    {{ slotProps.data.price.text }}-->
<!--                  </template>-->
                </Column>
                <Column :exportable="false" style="min-width:8rem">
                  <template #body="slotProps">
<!--                    <Button icon="pi pi-check" class="p-button-text"  @click="deleteProduct(slotProps.data.id)" />-->
                    <Button icon="pi pi-pencil" class="p-button-rounded p-button-success mr-2 p-button-sm" @click="editProduct(slotProps.data)" />
                    <Button icon="pi pi-trash" class="p-button-rounded p-button-warning p-button-sm" @click="deleteProduct(slotProps.data.id)" />
                    <Button icon="pi pi-check" class="p-button-rounded p-button-stop p-button-sm" @click="editProduct(slotProps.data)" />
                  </template>
                </Column>
              </DataTable>
            </div>

            <Dialog v-model:visible="productDialog" :style="{width: '600px'}" header="Product Details" :modal="true" class="p-fluid">
<!--              <img src="https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png" :alt="product.image" class="product-image" v-if="product.image" />-->
              <div class="field">
                <!--                <label for="description">Sample</label>-->
                <p>{{product.id}}</p>
              </div>
              <div class="field">
                <!--                <label for="description">Sample</label>-->
                <p>{{product.seed}}</p>
              </div>
              <div class="field">
                <Editor v-model="product.text" editorStyle="height: 320px">
<!--                  <template #toolbar>-->
<!--                          <span class="ql-formats">-->
<!--                            <button class="ql-bold"></button>-->
<!--                            <button class="ql-italic"></button>-->
<!--                            <button class="ql-underline"></button>-->
<!--                          </span>-->
<!--                  </template>-->
                </Editor>
<!--                <label for="description">Sample</label>-->
<!--                <Textarea id="text" v-model="product.text" required="true" rows="3" cols="20" />-->
              </div>

<!--              <div class="field">-->
<!--                <label for="inventoryStatus" class="mb-3">Inventory Status</label>-->
<!--                <Dropdown id="inventoryStatus" v-model="product.inventoryStatus" :options="statuses" optionLabel="label" placeholder="Select a Status">-->
<!--                  <template #value="slotProps">-->
<!--                    <div v-if="slotProps.value && slotProps.value.value">-->
<!--                      <span :class="'product-badge status-' +slotProps.value.value">{{slotProps.value.label}}</span>-->
<!--                    </div>-->
<!--                    <div v-else-if="slotProps.value && !slotProps.value.value">-->
<!--                      <span :class="'product-badge status-' +slotProps.value.toLowerCase()">{{slotProps.value}}</span>-->
<!--                    </div>-->
<!--                    <span v-else>-->
<!--							{{slotProps.placeholder}}-->
<!--						</span>-->
<!--                  </template>-->
<!--                </Dropdown>-->
<!--              </div>-->

<!--              <div class="field">-->
<!--                <label class="mb-3">Category</label>-->
<!--                <div class="formgrid grid">-->
<!--                  <div class="field-radiobutton col-6">-->
<!--                    <RadioButton id="category1" name="category" value="Accessories" v-model="product.category" />-->
<!--                    <label for="category1">Accessories</label>-->
<!--                  </div>-->
<!--                  <div class="field-radiobutton col-6">-->
<!--                    <RadioButton id="category2" name="category" value="Clothing" v-model="product.category" />-->
<!--                    <label for="category2">Clothing</label>-->
<!--                  </div>-->
<!--                  <div class="field-radiobutton col-6">-->
<!--                    <RadioButton id="category3" name="category" value="Electronics" v-model="product.category" />-->
<!--                    <label for="category3">Electronics</label>-->
<!--                  </div>-->
<!--                  <div class="field-radiobutton col-6">-->
<!--                    <RadioButton id="category4" name="category" value="Fitness" v-model="product.category" />-->
<!--                    <label for="category4">Fitness</label>-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->

<!--              <div class="formgrid grid">-->
<!--                <div class="field col">-->
<!--                  <label for="price">Price</label>-->
<!--                  <InputNumber id="price" v-model="product.price" mode="currency" currency="USD" locale="en-US" />-->
<!--                </div>-->
<!--                <div class="field col">-->
<!--                  <label for="quantity">Quantity</label>-->
<!--                  <InputNumber id="quantity" v-model="product.quantity" integeronly />-->
<!--                </div>-->
<!--              </div>-->
              <template #footer>
                <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog"/>
                <Button label="Save" icon="pi pi-check" class="p-button-text" @click="editEntry(product.text, product.id)" />

              </template>
            </Dialog>

            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<style lang="scss" scoped>
.table-header {
  display: flex;
  align-items: center;
  justify-content: space-between;

  @media screen and (max-width: 960px) {
    align-items: start;
  }
}

.product-image {
  width: 50px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}

.p-dialog .product-image {
  width: 50px;
  margin: 0 auto 2rem auto;
  display: block;
}

.p-button-rounded {
  margin-bottom: 0.25rem;
  margin-right: 0.25rem;
}

.confirmation-content {
  display: flex;
  align-items: center;
  justify-content: center;
}
@media screen and (max-width: 960px) {
  ::v-deep(.p-toolbar) {
    flex-wrap: wrap;

    .p-button {
      margin-bottom: 0.25rem;
      margin-right: 0.25rem;
    }
  }
}
</style>
<script>
import { FilterMatchMode } from 'primevue/api';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Dialog from 'primevue/dialog';
// import Textarea from 'primevue/textarea';
import Editor from 'primevue/editor';
// import { FilterMatchMode } from 'primevue/api';
import axios from "axios";
import {cacheAdapterEnhancer} from "axios-extensions";
// import ColumnGroup from 'primevue/columngroup';     //optional for column grouping
// import Row from 'primevue/row';
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
      editingRows: [],
      productDialog: false,
      deleteProductDialog: false,
      deleteProductsDialog: false,
      product: {},
      selectedProducts: null,
      filters: {},
      submitted: false,
      cars: null,
      rowUpdate: {},
      filter: '',
      resp: null,
      resp_entry: null,
      total: null,
      id: null,
      resultsL: null,
      sample: null,
      interval: null,
      interval_entry: null,
      tbp: null,
      keep: null,
      data: null,
      texts: null,
      messages: null,
      metrics: {
        keep_per: null,
        remove_per: null
      },
      samples: null,
      remove: null,
      text: null,

    };
  },
  beforeMount() {
    this.getEntries();
  },
  mounted() {
    this.data = this.cars;
  },
  created() {
    this.initFilters();
    // this.interval = setInterval(this.getMetrics, 1000)
  },
  beforeUnmount() {
    // clearInterval(this.interval)
    // clearInterval(this.interval_entry)
  },
  components: {
    DataTable,
    Column,
    Dialog,
    // Textarea,
    Editor

    // GradientLineChart,
    // Carousel,
    // CategoriesCard,
  },

  methods: {
    initFilters() {
      this.filters = {
        'global': {value: null, matchMode: FilterMatchMode.CONTAINS},
      }
    },
    editProduct(product) {
      console.log("_____________")
      console.log(product)
      this.product = {...product};
      this.productDialog = true;
    },
    hideDialog() {
      this.productDialog = false;
      this.submitted = false;
    },
    async deleteProduct(id) {
      const texts = {id: {id}};
      await http.post("https://api.cldevlab.shop/delete",texts,{ cache: false });
      await this.getEntries();
    },
    async editEntry(text, id) {
      // console.log("--------------")
      console.log(text,id)
      const texts = {text: text, id: {id}};
      console.log(texts)
      await http.post("https://api.cldevlab.shop/edit",texts,{ cache: false });
      this.productDialog = false;
      this.product = {};
      await this.getEntries();
      // const ids = {id: id};
      // http.post("https://api.cldevlab.shop/edit", texts,{ cache: false })
      //     .then(function (response) {
      //       // this.articleId = response.data.id;
      //       console.log(response.data)
      //       // this.results = response.data
      //       return response.data;
      //     })
      //     .catch ( function (error){
      //       console.log(error);
      //     });
      // // this.keepRemove(true,id)
      // // this.getEntry()
      // this.productDialog = false;
      // this.product = {};
      // this.getEntries();
    },
    async getEntries() {
      // const data = ref(null);
      console.log("------------------")
      // Simple POST request with a JSON body using axios
      const response = await http.get("https://api.cldevlab.shop/entries",{ cache: false });
      this.cars = response.data
    }

  }
}
</script>
