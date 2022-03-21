<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <UserInfo />
    
  </div>
</template>

<script>
// @ is an alias to /src
import UserInfo from '@/components/UserInfo.vue';

export default {
  name: 'HomeView',
  components: {
    UserInfo,
  }
}
</script>