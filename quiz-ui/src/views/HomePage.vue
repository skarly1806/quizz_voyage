<script setup>
</script>

<template>
  <div>
    <img src="/src/assets/logo.png" alt="logo">
  </div>

  <div class="score" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry }}
  </div>

  <div><button type="buttonhome" class="but" @click="launchNewQuiz">Démarrer le quiz !</button></div>

</template>

<script>
import quizApiService from "@/services/QuizApiService";



export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
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
.buttonhome {
  background-color: #b0efb2;
  text-align: center;
  color: white;

  border-radius: 4px;
  padding: 14px 40px;
  border: none;
  transition-duration: 0.4s;
}

.buttonhome:hover {
  border: 2px solid #b0efb2;
  background-color: #ffffff;
  color: black;
}

img {
  display: block;
  margin-left: 350px;
  margin-right: auto;
  margin-top: -200px;
}
</style>
