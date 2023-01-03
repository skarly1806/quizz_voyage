<script setup>
</script>

<template>

  <p>'AdminPage'</p>
  <div v-if="token">
    token valid
  </div>
  <div v-else>
    token not valid
  </div>



</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";



export default {
  name: "AdminPage",
  data() {
    return {
      token: '',
    };
  },
  methods: {
    launchNewQuiz() {

    },
  },
  async created() {
    var password = await participationStorageService.getPassword();
    var login_res = await quizApiService.login(password);
    participationStorageService.saveToken(login_res.data.token);
    this.token = await participationStorageService.getToken();
    console.log(this.token);
  }
};
</script>

<style>

</style>