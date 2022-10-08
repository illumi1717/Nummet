import { createRouter, createWebHistory } from 'vue-router'

import MainPage from "@/views/MainPage"
import SlaeSolvingPage from "@/views/SlaeSolvingPage"
import MatrixOperationsPage from "@/views/MatrixOperationsPage/MatrixOperationsPage"
import ResultPage from '@/views/ResultPage'

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainPage
  },

  {
    path: '/slae-solving-page',
    name: 'slae',
    component: SlaeSolvingPage
  },

  {
    path: '/matrix-operation',
    name: 'matrix',
    component: MatrixOperationsPage
  },

  {
    path: '/result',
    name: 'result',
    component: ResultPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
