<template>
  <div id="app">
    <div class="container overflow-hidden text-center">
      <div class="row gy-5">
        <div class="col-4" v-for="book in books" :key="book.id">
          <div class="card mb-3">
            <img src="https://res.cloudinary.com/geetechlab-com/image/upload/v1567092352/geetech/project-1_j8gjpc.jpg" class="card-img-top" alt="{{book.id}}">
            <div class="card-body">
              <h5 class="card-title">{{book.name}}</h5>
              <p class="card-text">ISBN: {{book.isbn}}</p>
              <p class="card-text"><small class="text-muted">Author: {{book.book_author}}</small></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      books: []
    }
  },
  async created() {
    var response = await fetch('http://127.0.0.1:8000/');
    this.books = await response.json();
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
