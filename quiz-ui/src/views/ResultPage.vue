<script setup>
</script>
 
<template>
  <div>
    <img src="/src/assets/logo.png" alt="logo" style="top:70%;">
  </div>

  <div class="borderScore" style="animation:bounce 2s linear infinite alternate-reverse;">
    <p class="textScore">Voici votre score <br><u>{{ player }}</u> : <font color="red">{{ score }}</font><br> {{ text }}
    </p>
  </div>


  <!-- <div class="score" v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    liste result : {{ scoreEntry["playerName"] }} ::{{ scoreEntry["score"] }}
  </div> -->
  <div id="table-wrapper" style="left:-10%;top:-73%;width:400px;">
    <div id="table-scroll" style="height:715px;">
      <table id="customers" class="relative" style=" top:-2%;left:10%;">
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
    </div>
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
      score: 0,
      text: "",
    };
  },
  methods: {
    postparti() {
      //this.resultatJsonAPush = [player, list];
      //var participe = quizApiService.postParticipation();
    },
    message() {
      if (this.score == 10) {

        return "bravo champion !"

      }
      else if (this.score > 7) {
        return "peut mieux faire"
      }
      else if (this.score < 8 && this.score > 4) {
        return "ah ouais chaud :/"
      }
      else {
        return "la honte"
      }
    },
  },
  async created() {
    this.list = participationStorageService.getList();
    this.player = participationStorageService.getPlayerName();
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    this.registeredScores = quizInfoApiResult.data.scores;
    var playerScore = await quizApiService.getScore();
    this.score = playerScore.data;
    this.text = this.message();
    console.log(this.text);
  }
}
</script>

<style>
#table-wrapper {
  position: relative;
  width: 500px;
  height: 400px;
}


#table-scroll {
  height: 360px;
  overflow-y: scroll;
  overflow-x: hidden;
  margin-top: 20px;
}

#table-wrapper table {
  width: 100%;
}

#table-wrapper table * {
  color: black;
}

#table-wrapper table thead th .text {
  position: absolute;
  top: -20px;
  z-index: 2;
  height: 20px;
  width: 35%;
  border: 1px solid red;
}

img {
  display: block;
  margin-left: 350px;
  margin-right: auto;
  margin-top: -200px;

}

.textScore {
  top: 15%;
  text-align: center;
  width: 480px;
  height: 150px;
  font-size: 30px;
  font-family: 'Poppins', sans-serif;
}

.borderScore {
  top: 165%;
  right: 58%;
  width: 490px;
  height: 180px;
  border-radius: 50% 20% / 10% 40%;
  background-color: rgb(135, 204, 143);
}
</style>
