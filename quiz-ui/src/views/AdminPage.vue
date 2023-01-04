<script setup>
</script>

<template>

  <p>AdminPage</p>
  <div v-if="token">
    <p class="quest"> Saisissez votre questionTitle :</p>
    <input type="text" v-model="questionTitle" />
    <p class="quest"> Saisissez votre questionText :</p>
    <input type="text" v-model="questionText" />
    <ImageUpload @file-change="imageFileChangedHandler" />
    <p class="quest"> Saisissez vos possibleAnswers :</p>
    <input type="text" v-model="answer1" /> <input type="radio" id="rep1" name="boolrep" />
    <input type="text" v-model="answer2" /> <input type="radio" id="rep2" name="boolrep" />
    <input type="text" v-model="answer3" /> <input type="radio" id="rep3" name="boolrep" />
    <input type="text" v-model="answer4" /> <input type="radio" id="rep4" name="boolrep" />

    <button @click="PushQuestion">Ajouter question</button>
  </div>
  <div v-else>
    <div class="login">
      <input type="login_inp" v-model="passwordInput" />
      <span @click="loginAgain">Login</span>
    </div>
  </div>



</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import ImageUpload from '@/views/ImageUpload.vue'



export default {
  name: "AdminPage",
  data() {
    return {
      token: '',
      passwordInput: "",
      questionTitle: "",
      questionText: "",
      questionPosition: "",
      questionImage: "",
      answer1: "",
      answer2: "",
      answer3: "",
      answer4: "",
      answer1verif: false,
      answer2verif: false,
      answer3verif: false,
      answer4verif: false,
      boolrep: "",

      possibleAnswers: [],
    };
  },
  methods: {
    async loginAgain() {
      var login_result = await quizApiService.login(this.passwordInput);
      participationStorageService.saveToken(login_result.data.token);
      this.token = await participationStorageService.getToken();
    },
    imageFileChangedHandler(b64String) {
      this.questionImage = b64String;
    },
    async PushQuestion() {
      const radioButtons = document.querySelectorAll('input[name="boolrep"]');
      if (radioButtons[0].checked) {
        this.answer1verif = true;
      } else if (radioButtons[1].checked) {
        this.answer2verif = true;
      } else if (radioButtons[2].checked) {
        this.answer3verif = true;
      } else if (radioButtons[3].checked) {
        this.answer3verif = true;
      }
      this.possibleAnswers = [{ "text": this.answer1, "isCorrect": this.answer1verif },
      { "text": this.answer2, "isCorrect": this.answer2verif },
      { "text": this.answer3, "isCorrect": this.answer3verif },
      { "text": this.answer4, "isCorrect": this.answer4verif }]
      const question = {
        "text": this.questionText, "title": this.questionTitle,
        "image": this.questionImage, "position": this.questionPosition,
        "possibleAnswers": this.possibleAnswers
      };
      console.log(question);
      console.log(this.boolrep);
      await quizApiService.addQuestion(question, this.token);
    },
  },
  components: { ImageUpload },
  async created() {
    console.log("admin page");
    var password = await participationStorageService.getPassword();
    var login_res = await quizApiService.login(password);
    participationStorageService.saveToken(login_res.data.token);
    this.token = await participationStorageService.getToken();

  }
};
</script>

<style>

</style>