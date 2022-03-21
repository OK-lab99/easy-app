<template>
<div class="signin-form">
 <h1>新規作成</h1>
 <label>名前(必須)</label>
 <input type="text" v-model="name">
 <br><br>
 <label>メールアドレス(必須)</label>
 <input type="email" v-model="email">
 <br><br>
 <label>パスワード(必須)</label>
 <input type="password" v-model="password">
 <div>
 <input @click="create_user" type="button" value="新規作成" />  
 </div>
 {{ result }}
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SigninForm',
  data () {
    return {
      name: "",
      email: "",
      password: "",
      result: ""  
    }
  },
  methods: {
    create_user () {
      axios
      .post('http://0.0.0.0:8000/user/',{
        "name": this.name, 
        "email": this.email,
        "password": this.password
        })
      .then((response) => this.result = response.data)
      .catch((error) => this.result = error)
    },
  }
      
    

}
</script>

<style>
.signin-form {
  padding-top: 100px;
}

label{
  float: left;
  margin-right: 20px;
  width:150px;
  border-left: solid 3px #e0505d;
}

input {
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