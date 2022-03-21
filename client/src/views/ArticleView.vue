<template>
  <div class="article-view">
    <div v-for="article in articles" v-bind:key="article.id">
      <h2>作者: ログインされていないユーザー</h2>
      <h3>タイトル：{{ article.title }}</h3>
      <h4>内容：{{ article.content }}</h4>
      <hr>
    </div>
    
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  name: 'ArticleView',
  data () {
    return {
      articles: []
    }
  },
  mounted () {
      axios
      .get('http://0.0.0.0:8000/articles')
      .then(response => (this.articles = response.data))
    },
  }
</script>