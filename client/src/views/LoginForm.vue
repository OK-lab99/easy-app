<template>
<div class="login-form">
 <h1>ログイン</h1>
 <label>ユーザーネーム(必須)</label>
 <input type="text" v-model="username">
 <br><br>
 <label>パスワード(必須)</label>
 <input type="password" v-model="password">
 <div>
 <input @click="login_user" type="button" value="ログイン" />  
 </div>
 {{ result }}
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginForm',
  data () {
    return {
      namename: "",
      password: "",
      result: ""  
    }
  },
  
  methods: {
    login_user () {
      axios
      .get('http://0.0.0.0:8000/token/',{
        "namename": this.name, 
        "password": this.password
        })
      .then((response) => this.result = response.data)
      .catch((error) => this.result = error)
    },
  }
      
    

}
</script>

<style>
.login-form {
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