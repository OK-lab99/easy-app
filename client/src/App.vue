<template>
  <nav>
    <router-link to="/">home</router-link> |
    <router-link to="articles">投稿を見る</router-link>|
    <router-link to="article">投稿する</router-link>|
    <router-link to="signin">signin</router-link>|
    <router-link to="login">login</router-link>|
  </nav>
  <router-view />
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
