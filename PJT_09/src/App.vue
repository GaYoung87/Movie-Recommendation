<template>
  <div id="app">
    <div class="container">
      <!-- 1-3. 호출하시오. 
        필요한 경우 props로 데이터를 보내줍니다. (값을 넘길 때 props로 넘김ex. todo-category)
      -->
      <!-- Vue에서 movies, genres의 데이터를 넘겨주겠다. -->
      <!-- v-bind사용하지 않으면, movies에 movies라는 단어만 넘겨주게 됨 -->
      <!-- 내가 가지고있는것="넘겨서 받을 이름" -->
      <MovieList v-bind:movies="movies" v-bind:genres="genres" />
    </div>
  </div>
</template>

<script>
const axios = require('axios');
// 1-1. 저장되어 있는 MovieList 컴포넌트를 불러오고,
import MovieList from './components/movies/MovieList.vue'

export default {
  name: 'app',
  
  // 1-2. 아래에 등록 후
  components: {
    MovieList: MovieList,
  },
  
  data() {
    return {
      // 활용할 데이터를 정의하시오.
      movies: [],
      genres: [],
    }
  },
  mounted() {  // created와 비슷한 동작
    // 처음 실행되고, vue instance가 생성되었을 때
    // console.log('나 이제 그려졌다!')
    // 0. mounted 되었을 때,
    // axios로 불러온다음
    // 1) 제시된 URL로 요청을 통해 data의 movies 배열에 해당 하는 데이터를 넣으시오.
    this.get_movies()  // methods에서는 함수만 만들고, mounted에서는 함수실행!

    // 2) 제시된 URL로 요청을 통해 data의 genres 배열에 해당 하는 데이터를 넣으시오.
    // axios는 위에 호출되어 있으며, node 설치도 완료되어 있습니다.
    this.get_genres()
  },
  methods: {
    get_movies: function() {
      const API_URL = 'https://gist.githubusercontent.com/edujason-hphk/f57d4cb915fcec433ece535b2f08a10f/raw/612fd3f00468722ead2cfe809f14e38230b47686/movie.json'

      axios.get(API_URL)
        .then((response) => {
          // this.movies는 data의 movies
          this.movies = response.data
          // console.log(response)
        })
    },
    get_genres: function() {
      const API_URL = 'https://gist.githubusercontent.com/edujason-hphk/eea9c85a937cbf469b8f55fd7f8524df/raw/68bad38a2bc911d3a39bce26d6dd9b68a7efe849/genre.json'

      axios.get(API_URL)
        .then((response) => {
          // this.genres는 data의 genres
          this.genres = response.data
          // console.log(response)
        })
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
