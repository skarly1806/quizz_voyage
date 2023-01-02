<script setup>
</script>
 
<template>
  <div>
    <img src="/src/assets/logo.png" alt="logo">
  </div>
  Voici votre score {{ player }} : {{ list }}
  <div class="score" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    liste result : {{ scoreEntry["playerName"] }} ::{{ scoreEntry["score"] }}
  </div>
  {{ resultats }}

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
      registeredScores: [],
      resultatJsonAPush: [],
    };
  },
  methods: {
    postparti() {
      //this.resultatJsonAPush = [player, list];
      //var participe = quizApiService.postParticipation();
    },
  },
  async created() {
    this.list = participationStorageService.getList();
    this.player = participationStorageService.getPlayerName();
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    this.registeredScores = quizInfoApiResult.data.scores;

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
