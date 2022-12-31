<script setup>
</script>

<template>
  <div>
    <img src="/src/assets/logo.png" alt="logo">
    <p class="quest"> Saisissez votre nom :</p>
    <input type="text" v-model="username" />
    <p>{{ username }}</p>
    <div><button class="but" type="button" @click="launchNewQuiz"> Go!</button></div>
  </div>




</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";



export default {
  name: "NewQuizPage",
  data() {
    return {
      username: '',
    };
  },
  methods: {
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/QuestionsManager');
    },
  },
  async created() {

    console.log("Composant New quiz page 'created'");
  }
};
</script>

<style>
.but {
  background-color: #b0efb2;
  text-align: center;
  color: white;
  margin-top: 10px;
  margin-left: 540px;
  border-radius: 4px;
  padding: 14px 40px;
  border: none;
  transition-duration: 0.4s;
}

.but:hover {
  border: 2px solid #b0efb2;
  background-color: #ffffff;
  color: black;
}

.quest {
  margin-left: 525px;
}

img {
  display: block;
  margin-left: 350px;
  margin-right: auto;
  margin-top: -200px;
}

input[type=text] {
  border: 3px solid rgb(145, 197, 220);
  margin-left: 500px;
}

input[type=text]:focus {
  border: 3px solid rgb(145, 197, 220);

}
</style>