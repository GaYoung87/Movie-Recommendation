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