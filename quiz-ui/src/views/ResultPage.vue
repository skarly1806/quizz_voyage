<script setup>
</script>
 
<template>
  <div>
    <img src="/src/assets/logo.png" alt="logo" style="top:50%;">
  </div>
  <div>Voici votre score {{ player }} : {{ list }}</div>

  <!-- <div class="score" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    liste result : {{ scoreEntry["playerName"] }} ::{{ scoreEntry["score"] }}
  </div> -->
  <table id="customers" class="relative" style="top:-80%; left:10%;">
    <thead>
      <tr>
        <th>Player Name</th>
        <th>Score</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="unit in registeredScores" :key="unit.id">
        <td>{{ unit["playerName"] }}</td>
        <td>{{ unit["score"] }}</td>
      </tr>
    </tbody>
  </table>
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
