<template>
<div class="article-form">
 <h1>記事作成</h1>
 <label>タイトル(必須)</label>
 <input type="text" v-model="title">
 <br><br>
 <label>内容</label>
 <input type="text" v-model="content">
 <br>
 <input @click="create_article" type="button" value="記事作成" />  
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ArticleForm',
  data () {
    return {
      title: "",
      content: "",
      article_result: "",
    }
  },
  methods: {
    create_article () {
      axios
      .post('http://0.0.0.0:8000/article/',{
        "title": this.title, 
        "content": this.content
        })
      .then((response) => this.article_result = response.data)
      .catch((error) => this.article_result = error)
    },
  }
      
    

}
</script>

<style>
.article-form {
  padding-top: 100px;
}

label{
  float: left;
  margin-right: 20px;
  width:150px;
  border-left: solid 3px #e0505d;
}

input{
  width: 60%;
  margin-top: 10px;
  margin-bottom: 30px;
  padding: 20px;
  font-size: 18px;
  border: 1px solid #dee7ec;
}


button {
    width: 130px;
    height: 40px;
    margin-bottom: 30px;
  }
</style>
