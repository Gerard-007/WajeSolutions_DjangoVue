<template>
  <div id="app">
    <div class="row justify-content-md-center">
      <div class="col-6 mx-auto mt-5">
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
          add book
        </button>

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Add a book</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <form @submit.prevent="createBook">
                  <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="floatingInput" placeholder="book-name" v-model="book.name">
                    <label for="floatingInput">Name</label>
                  </div>
                  <div class="form-floating mb-3">
                    <input  type="text" class="form-control" id="floatingISBN" placeholder="isbn" v-model="book.isbn">
                    <label for="floatingISBN">ISBN</label>
                  </div>
                  <div class="form-floating mb-3">
                    <select class="form-select" id="floatingSelect" aria-label="Floating label select example" v-model="book.author">
                      <option selected v-for="author in authors" :key="author.id">{{author.id}} {{author.first_name}} {{author.last_name}}</option>
                    </select>
                    <label for="floatingSelect">Author</label>
                  </div>
                  <div class="d-grid gap-2">
                    <button type="submit" class="btn btn-primary mb-3">Create Book</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br/>
    <br/>
    <div class="row gy-5">
      <div class="col-3" v-for="book in books" :key="book.id">
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
</template>

<script>

  export default {
    name: 'App',
    data(){
      return {
        book: {
          'name': '',
          'isbn': '',
          'author': ''
        },
        books: [],
        authors: []
      }
    },

    async created() {
      await this.getBooks();
      await this.getAuthors();
    },

    methods: {
      async getAuthors() {
        var response = await fetch('http://127.0.0.1:8000/authors/');
        this.authors = await response.json();
      },

      async getBooks() {
        var response = await fetch('http://127.0.0.1:8000/');
        this.books = await response.json();
      },

      async createBook() {
        await this.getBooks();

        var response = await fetch('http://127.0.0.1:8000', {
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.book)
        });

        await this.getBooks();
        this.books.push(await response.json());
      }
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
