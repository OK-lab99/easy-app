<template>
<header>
<nav>
    <router-link to="/">home</router-link> |
    <router-link to="articles">投稿を見る</router-link>|
    <router-link to="contact">Contact</router-link>|
    <router-link to="login">login</router-link>|
    <router-link to="logout">logout</router-link>|
    <router-link to="signin">signin</router-link>|
  </nav>
    </header>
</template>

<script>
export default {
    name: 'MyHeader',
}
</script>