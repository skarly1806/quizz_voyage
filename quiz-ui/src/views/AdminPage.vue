<script setup>
</script>

<template>

  <p>AdminPage</p>
  <div v-if="token">

    <div style="top:75%;left:-15%;">
      <p class="formulaireQuest" style="left:-250px;">Chargez une image :</p>
      <ImageUpload @file-change="imageFileChangedHandler" />
    </div>
    <div class="formulaire">
      <p class="formulaireQuest"> Saisissez le titre de la question :</p>
      <input type="text" v-model="questionTitle" />
      <p class="formulaireQuest"> Saisissez la question :</p>
      <input type="text" v-model="questionText" />
      <p class="formulaireQuest"> Saisissez la position :</p>
      <input type="text" v-model="questionPosition" />


      <p class="formulaireQuest"> Saisissez les réponses :</p>
      <input type="text" v-model="answer1" /> <input type="radio" id="rep1" name="boolrep" style="left:130px;" />
      <input type="text" v-model="answer2" /> <input type="radio" id="rep2" name="boolrep" style="left:130px;" />
      <input type="text" v-model="answer3" /> <input type="radio" id="rep3" name="boolrep" style="left:130px;" />
      <input type="text" v-model="answer4" /> <input type="radio" id="rep4" name="boolrep" style="left:130px;" />

    </div>
    <button @click="PushQuestion" style="top:140px; left:-65px;">Ajouter la question</button>
  </div>
  <div v-else>
    <div class="login" style="top:50%;left:-18%;">
      <input type="login_inp" v-model="passwordInput" />
      <button @click="loginAgain">Login</button>
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
      questionPosition: 0,
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
    reloadtrue() {
      this.questionTitle = "";
      this.questionText = "";
      this.questionPosition = 0;
      this.questionImage = "";
      this.answer1 = "";
      this.answer2 = "";
      this.answer3 = "";
      this.answer4 = "";
      this.answer1verif = false;
      this.answer2erif = false;
      this.answer3verif = false;
      this.answer4verif = false;
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
        this.answer4verif = true;
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
      this.reloadtrue();
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
.formulaire {
  right: 700px;
  top: 0%;
}

.formulaireQuest {
  right: -340px;
  text-align: center;
  font-family: 'Poppins', sans-serif;
  font-size: 20px;
}
</style>