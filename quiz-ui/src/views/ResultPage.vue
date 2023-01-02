<script setup>
</script>
 
<template>
  <div>
    <img src="/src/assets/logo.png" alt="logo">
  </div>
  Voici votre score {{ player }} :
  {{ list }}
  <div>liste result : {{ resultats }} ::{{ resultats.scores }} </div>

</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";



export default {
  name: "ResultPage",
  data() {
    return {
      list: [],
      player: "",
      resultats: [],
    };
  },
  methods: {
    launchNewQuiz() {

    },
  },
  async created() {
    this.list = participationStorageService.getList();
    this.player = participationStorageService.getPlayerName();
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    this.resultats = quizInfoApiResult.data.scores;

  }
}
</script>

<style>
img {
  display: block;
  margin-left: 350px;
  margin-right: auto;
  margin-top: -200px;
}
</style>
