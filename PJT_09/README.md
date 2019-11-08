# PJT_09

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).



## App.vue

```vue
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
  components: {
    MovieList: MovieList,
  },
  // 1-2. 아래에 등록 후
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

```

#### 1-1. URL로부터 불러오기

- URL 불러오는 함수만들기

```vue
<script>
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
</script>
```

- 함수 실행

```vue
<script>
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
</script>
```

#### 1-2. MovieList에 데이터 제공

- 저장되어있는 MovieList 컴포넌트 불러오기

```vue
<script>
// 1-1. 저장되어 있는 MovieList 컴포넌트를 불러오고,
import MovieList from './components/movies/MovieList.vue'
</script>
```

- 등록 후, 활용할 데이터 정의

```vue
<script>
  // components 등록
  components: {
    MovieList: MovieList,
  },
      
  // 활용할 데이터를 정의하시오.
  data() {
    return {
      movies: [],
      genres: [],
    }
  },
</script>
```

- MovieList에 값을 넘기기

- props: 최상위(App)에있는 데이터를 밑으로 내려줌 

  ​           ( 현재 우리는 movie정보들을 최상위app이 데이터에 가지고있다.)

```vue
<template>
  <div id="app">
    <div class="container">
      <!-- 1-3. 호출하시오. 필요한 경우 props로 데이터를 보내줍니다. -->
      <!-- Vue에서 movies, genres의 데이터를 넘겨주겠다. -->
      <!-- v-bind사용하지 않으면, movies에 movies라는 단어만 넘겨주게 됨 -->
      <!-- 내가 가지고있는것="넘겨서 받을 이름" -->
        
      <!-- 이것이 컴포넌트! --> 
      <MovieList v-bind:movies="movies" v-bind:genres="genres" />
    </div>
  </div>
</template>
```



## 2. MovieList

```vue
<template>
<!-- 여러개 movielisttiem을 가지고있음.전달받은 movielistitem을 하나씩 찍어내야함.
  movielistitem은 movie정보 없음 -> for문돌면서 실행 -->
  <div>
    <h1>영화 목록</h1>
    <h2>장르 선택</h2>
    <!-- 2. 장르 선택(제일 마지막에 구현하시오.)
    2-1. App 컴포넌트로 부터 받은 genres를 반복하여 드롭다운을 완성 해주세요.
    2-2. 드롭다운은 selectedGenreId data와 양방향바인딩(v-model)이 됩니다.
    2-3. 값 변경이 되면, 특정한 함수를 실행 해야합니다.
     -->
     <!-- v-bind: 위에서 v-bind로 주면 그것을 받으려면 props 사용 -->
    <select class="form-control" v-model="selectedGenre">
      <!-- 옵션에 따라 selectedGenre가 바뀐다. -->

      <!-- v-bind는 내가 가지고있는 값을 표현한다. (Vue에서 가지고있는 값을 할당한다.) -->
      <!-- vue에서 값을 바뀌면 input도 바뀐다 -->
      <option v-bind:value="0">모두</option>
      <option v-for="genre in genres" v-bind:key="genre.id" v-bind:value="genre.id">
        {{ genre.name }}
      </option>
    </select>
    <!-- for문돌때 movie는 그냥 꺼내오는 것 -> 그래서 v-bind로 보내줘야하는게 또 있어야함! -->
    <div class="row mt-5">
      <!-- 1-3. 반복을 통해 호출하시오. div 안쪽에서 반복
        필요한 경우 props를 데이터를 보내줍니다. -->
      <MovieListItem v-for="movie in select" v-bind:key="movie.id" v-bind:movie="movie" />
      <!-- (나중에 마지막으로) selectedGenreId 값에 따른 분기를 해야 합니다. -->

    </div>
  </div>
</template>

<script>
// 1-1. 저장되어 있는 MovieListItem 컴포넌트를 불러오고,
// App.vue에서는 MovieList에 있는 것들을 가지고오기 위해서 components/movies/로 들어갔지만, 
// 지금은 이미 components/movies까지 들어와있으므로, from './MovieListItem.vue'라고 해야함
import MovieListItem from './MovieListItem.vue'

export default {
  name: 'MovieList',
  // 1-2. 아래에 등록 후
  components: {
    MovieListItem: MovieListItem,
  },

  data () {
    return {
      // 활용할 데이터를 정의하시오.
      // 새롭게 만들어지는 데이터면 이렇게 작성하는거지만, 우리가하는건 지금 App.vue에서 전달받아서 하는 것 -> return {}만 쓰면 괜찮
      // movies: [],

      // 장르만 선택할 수 있게, 데이터를 만든다 -> selectedGenre
      // genre의 id값이 들어가야하므로, 앞으로도 없을 숫자인 0을 넣는다(=모든 장르)
      // 우리가 할 것이 genre의 id값이므로, 그 id값이 int라서 selectedGenreeh 0
      selectedGenre: 0,
    }
  },
  // 0. props 데이터를 받이 위하여 설정하시오.
  // genres와 movies 모두 타입은 Array이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
  props: {
    movies: {
      type: Array,
      required: true,
    },
    genres:  {
      type: Array,
      required: true,
    },  // 이렇게 들고오면, App.vue에 있는 movie에 대한 정보를 받아온다
  },

  // 2-3.에서 이야기하는 특정한 함수는 selectedGenreId의 값이 변경될 때마다 호출 됩니다.
  // 드랍다운에서 장르를 선택하면, 해당 영화들만 보여주도록 구현 예정입니다.
  // 주의할 것은 직접 부모 컴포넌트의 데이터를 변경할 수 없다는 점입니다.
  computed: {
    select: function() {
      if (this.selectedGenre !== 0) {
        // console.log(this.movies)
        return this.movies.filter( selectMovie => {
          return this.selectedGenre === selectMovie.genre_id
        })
      } else {
        return this.movies
      }
    },
  },
}
</script>

<style>
select {
  display: block;
  width: 50% !important;
  margin: 2rem auto !important;
}
</style>
```



#### 2-1.  MovieListItem에 데이터 제공

- 저장되어있는 MovieListItem컴포넌트 불러오기

```vue
<script>
// 1-1. 저장되어 있는 MovieList 컴포넌트를 불러오고,
// App.vue에서는 MovieList에 있는 것들을 보내기위해 components/movies/로 들어갔지만, 
// 지금은 이미 components/movies까지 들어와있으므로, from './MovieListItem.vue'
import MovieListItem from './MovieListItem.vue'
</script>
```

- 등록 후, 활용할 데이터 정의

```vue
<script>
// 1-2. 아래에 등록 후
    components: {
    MovieListItem: MovieListItem,
  },

// 0. props 데이터를 받이 위하여 설정하시오.
  // genres와 movies 모두 타입은 Array이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
  props: {
    movies: {
      type: Array,
      required: true,
    },
    genres:  {
      type: Array,
      required: true,
    },  // 이렇게 들고오면, App.vue에 있는 movie에 대한 정보를 받아온다
  },
      
// 활용할 데이터를 정의하시오.
  data () {
    return {}
  },
</script>
```

- MovieListItemModal에 movie 값을 넘기기

```vue
<template>
  <div class="col-3 my-3">
      <!-- 이것이 컴포넌트! --> 
      <MovieListItem v-for="movie in select" v-bind:key="movie.id" v-bind:movie="movie" />
  </div>
</template>
```



## 3. MovieListItem.vue

```vue
<template>
  <div class="col-3 my-3">
    <!-- img 태그에 src와 alt값(영화제목)을 설정하시오 -->
    <!-- 데이터를 props로 받아온 것이므로 v-bind사용해야함! -->
    <img class="movie--poster my-3" v-bind:src="movie.poster_url" v-bind:alt="영화제목">
    <!-- 영화 제목을 출력하시오. -->
    <!-- text는 {{  }} 이거로한다. -->
    <h3>{{ movie.name }}</h3>
    <!-- 모달을 활용하기 위해서는 data-taget에 모달에서 정의된 id값을 넣어야 합니다. -->
    <button class="btn btn-primary" data-toggle="modal" v-bind:data-target="`#movie-${movie.id}`">영화 정보 상세보기</button>
    
    <!-- 1-3. 호출하시오. 필요한 경우 props를 데이터를 보내줍니다. -->
    <MovieListItemModal v-bind:movie="movie" />
  </div>
</template>

<script>
// 1-1. 저장되어 있는 MovieListItemModal 컴포넌트를 불러오고,
import MovieListItemModal from './MovieListItemModal.vue'

export default {
  name: 'MovieListItem',
  // 1-2. 아래에 등록 후
  components: {
    MovieListItemModal: MovieListItemModal,
  },
  
  // 0. props 데이터를 받기 위하여 설정하시오.
  // movie 타입은 Object이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },

  data () {
    // 활용할 데이터를 정의하시오.
    return {
      
    }
  },
}
</script>

<style>
.movie--poster {
  width: 200px;
}
</style>
```



#### 3-1. MovieListItemModal에 데이터 제공

- 저장되어있는 MovieListItemModal컴포넌트 불러오기

```vue
<script>
// 1-1. 저장되어 있는 MovieList 컴포넌트를 불러오고,
import MovieListItemModal from './MovieListItemModal.vue'
</script>
```

- 등록 후, 활용할 데이터 정의

```vue
<script>
// 1-2. 아래에 등록 후
  components: {
    MovieListItemModal: MovieListItemModal,
  },
      
// 0. props 데이터를 받기 위하여 설정하시오.
  // movie 타입은 Object이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },

  data () {
    // 활용할 데이터를 정의하시오.
    return {}
  },
</script>
```

- MovieListItemModal에 movie 값을 넘기기


```vue
<template>
  <div class="col-3 my-3">
      <!-- 이것이 컴포넌트! --> 
      <MovieListItemModal v-bind:movie="movie" />
  </div>
</template>
```



#### 3-2. 화면에 영화 정보 보이기

```vue
<template>
  <div class="col-3 my-3">
    <!-- img 태그에 src와 alt값(영화제목)을 설정하시오 -->
    <!-- 데이터를 props로 받아온 것이므로 v-bind사용해야함! -->
    <img class="movie--poster my-3" v-bind:src="movie.poster_url" v-bind:alt="영화제목">
    <!-- 영화 제목을 출력하시오. -->
    <!-- text는 {{  }} 이거로한다. -->
    <h3>{{ movie.name }}</h3>
    <!-- 모달을 활용하기 위해서는 data-taget에 모달에서 정의된 id값을 넣어야 합니다. -->
    <button class="btn btn-primary" data-toggle="modal" v-bind:data-target="`#movie-${movie.id}`">영화 정보 상세보기</button>
    
    <!-- 1-3. 호출하시오. 필요한 경우 props를 데이터를 보내줍니다. -->
    <MovieListItemModal v-bind:movie="movie" />
  </div>
</template>
```

![image-20191108170017176](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191108170017176.png)



## 4. MovieListItemModal.vue

```vue
<template>
<!-- vue 콘솔에서 확인하여, 추가 정보들도 출력하세요. -->
<!-- 고유한 모달을 위해 id 속성을 정의하시오. 예) movie-1, movie-2, ... -->
<!-- MovieListItem에서 data-target을 지정했기 때문에 MovieListItemModal에서 id를 똑같이 지정해야함! -->
<div class="modal fade" tabindex="-1" role="dialog" v-bind:id="`movie-${movie.id}`">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <!-- 영화 제목을 출력하세요. -->
        <h5 class="modal-title">{{ movie.name }}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <!-- 영화 설명을 출력하세요. -->
        <img class="movie--poster my-3" v-bind:src="movie.poster_url" alt="영화포스터">
        <p>{{ movie.rating }}</p>
        <p>{{ movie.description }}</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'movie-list-item-modal',
  // 0. props 데이터를 받이 위하여 설정하시오.
  // movie 타입은 Object이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
}
</script>

<style>

</style>
```



#### 4-1. URL로부터 불러오기

- props로 데이터 받기

```vue
<script>
// 0. props 데이터를 받이 위하여 설정하시오.
  // movie 타입은 Object이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
</script>
```

- 내용 출력

```vue
<template>

<!-- 고유한 모달을 위해 id 속성을 정의하시오. 예) movie-1, movie-2, ... -->
<!-- MovieListItem에서 data-target을 지정했기 때문에 MovieListItemModal에서 id를 똑같이 지정해야함! -->
<div class="modal fade" tabindex="-1" role="dialog" v-bind:id="`movie-${movie.id}`">

<!-- 영화 제목을 출력하세요. -->
<h5 class="modal-title">{{ movie.name }}</h5>
<button type="button" class="close" data-dismiss="modal" aria-label="Close">
  <span aria-hidden="true">&times;</span>
</button>

<!-- 영화 설명을 출력하세요. -->
<img class="movie--poster my-3" v-bind:src="movie.poster_url" alt="영화포스터">
<p>{{ movie.rating }}</p>
<p>{{ movie.description }}</p>
```

![image-20191108163939777](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191108163939777.png)



## 5. 드롭다운을 통한 장르 선택시 필터링 된 영화들 실시간 출력

- selectedGenre 값에 따른 분기를 해야 합니다.

```vue
<template> 
<!-- 2. 장르 선택(제일 마지막에 구현하시오.)
    2-1. App 컴포넌트로 부터 받은 genres를 반복하여 드롭다운을 완성 해주세요.
    2-2. 드롭다운은 selectedGenreId data와 양방향바인딩(v-model)이 됩니다.
    2-3. 값 변경이 되면, 특정한 함수를 실행 해야합니다. -->
     <!-- v-bind: 위에서 v-bind로 주면 그것을 받으려면 props 사용 -->
    <select class="form-control" v-model="selectedGenre">
      <!-- 옵션에 따라 selectedGenre가 바뀐다. -->

      <!-- v-bind는 내가 가지고있는 값을 표현한다.(Vue에서 가지고있는 값을 할당한다.) -->
      <!-- vue에서 값을 바뀌면 input도 바뀐다 -->
     <option v-bind:value="0">모두</option>
     <option v-for="genre in genres" v-bind:key="genre.id" v-bind:value="genre.id">
        {{ genre.name }}
      </option>
    </select>
</template>



<script>
computed: {
    select: function() {
      if (this.selectedGenre !== 0) {
        // console.log(this.movies)
        return this.movies.filter( selectMovie => {
          return this.selectedGenre === selectMovie.genre_id
        })
      } else {
        return this.movies
      }
    },
  },
</script>
```

![image-20191108171036828](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191108171036828.png)