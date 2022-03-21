<template>
  <div class="contact-form">
    <h1>お問い合わせ</h1>
    <div>
    <label for="text">名前(必須)</label>
    <input type="text" name="name" id="name" v-model="name"/>
    </div>
    <div>
    <label for="email">メールアドレス(必須)</label>
    <input type="email" name="email" id="email" v-model="email"/>
    </div>
    <div>
    <label for="content">お問い合わせ内容</label>
    <textarea name="content" id="content" v-model="content"></textarea>
    </div>
    <div>
    <button type="submit">送信</button>
    </div>

  </div>
</template>

<style>
.contact-form {
  padding-top: 100px;
}

label{
  float: left;
  margin-right: 20px;
  width:150px;
  border-left: solid 3px #e0505d;
}

input, textarea {
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