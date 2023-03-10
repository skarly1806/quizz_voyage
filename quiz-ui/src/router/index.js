import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import ResultPage from '../views/ResultPage.vue'
import AdminPage from '../views/AdminPage.vue'
import ListQuestions from '../views/ListQuestions.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/start-new-quiz-page',
      name: 'NewQuizPage',
      component: NewQuizPage
    },
    {
      path: '/ResultPage',
      name: 'ResultPage',
      component: ResultPage
    },
    {
      path: '/QuestionsManager',
      name: 'QuestionsManager',
      component: QuestionsManager
    },
    {
      path: '/AdminPage',
      name: 'AdminPage',
      component: AdminPage
    },
    {
      path: '/ListQuestions',
      name: 'ListQuestions',
      component: ListQuestions
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
