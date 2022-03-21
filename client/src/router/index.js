import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/articles',
    name: 'aritcles',
    component: () => import('../views/ArticleView.vue')
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('../views/ContactForm.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginForm.vue')
  },
  {
    path: '/article',
    name: 'article',
    component: () => import('../views/ArticleForm.vue')
  },
  {
    path: '/signin',
    name: 'signin',
    component: () => import('../views/SigninForm.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
