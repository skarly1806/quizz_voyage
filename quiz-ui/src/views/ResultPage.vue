<script setup>
</script>
 
<template>
  <div>
    <img src="/src/assets/logo.png" alt="logo">
  </div>
  <div>
    Rsultpage
  </div>

  <div class="score" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry }}
  </div>


  <div></div>

</template>

<script>
import quizApiService from "@/services/QuizApiService";



export default {
  name: "ResultPage",
  data() {
    return {
      list: [],
      playerName: "",
    };
  },
  methods: {
    launchNewQuiz() {
      this.$router.push('/start-new-quiz-page');
    },
  },
  async created() {
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    this.registeredScores = quizInfoApiResult.data.scores;
    console.log("Composant Home page 'created'");
  }
};
</script>

<style>
img {
  display: block;
  margin-left: 350px;
  margin-right: auto;
  margin-top: -200px;
}
</style>
