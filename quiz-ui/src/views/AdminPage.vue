<script setup>
</script>

<template>

  <p>AdminPage</p>
  <div v-if="token">

    <div class="formulaire" style="top:100px;">
      <p class="formulaireQuest"> Saisissez le titre de la question :</p>
      <input class="inputAdmin" type="text" v-model="questionTitle" style="width:300px;left:100px;" />
      <p class="formulaireQuest"> Saisissez la question :</p>
      <input type="text" v-model="questionText" style="width:300px;left:100px;" />


      <p class="formulaireQuest"> Saisissez les réponses (cochez la bonne réponse):</p>
      <table>
        <tbody>
          <tr>
            <td><input type="text" v-model="answer1" style="width:300px;left:100px;" /></td>
            <td><input type="radio" id="rep1" name="boolrep" style="left:130px;top:-10px;" /></td>
          </tr>
          <tr>
            <td><input type="text" v-model="answer2" style="width:300px;left:100px;" /></td>
            <td> <input type="radio" id="rep2" name="boolrep" style="left:130px;top:-10px;" /></td>
          </tr>
          <tr>
            <td><input type="text" v-model="answer3" style="width:300px;left:100px;" /></td>
            <td><input type="radio" id="rep3" name="boolrep" style="left:130px;top:-10px;" /></td>
          </tr>
          <tr>
            <td><input type="text" v-model="answer4" style="width:300px;left:100px;" /></td>
            <td><input type="radio" id="rep4" name="boolrep" style="left:130px;top:-10px;" /></td>
          </tr>
        </tbody>
      </table>

      <table style="left:160px;">
        <tbody>
          <tr>
            <td>
              <p class="formulaireQuest">Chargez une image :</p>
            </td>
            <td style="left:350px;top:-5px;">
              <ImageUpload @file-change="imageFileChangedHandler" />
            </td>
          </tr>
          <tr>
            <td style="left:580px;top:-130px;"><button class="button-admin" @click="PushQuestion"
                style="top:140px; left:-190px;background-color: #b0efb2;">Ajouter la question</button>
            </td>
            <td style="left:580px;top:-130px;"> <button class="button-admin" @click="listQuestion"
                style="top:140px;left:-190px;width:190px;height:50px;">Liste des
                questions</button>
            </td>
          </tr>
        </tbody>
      </table>

    </div>

  </div>
  <div v-else>
    <div class="error" style="top:380px;left:-100px" v-if="error == true">
      <p>mauvais mot de passe</p>
    </div>
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
      error: false,
      boolrep: "",
      totalNumberOfQuestion: 0,

      possibleAnswers: [],
      id: 0,
    };
  },
  methods: {
    async loginAgain() {
      var login_res = await quizApiService.login(this.passwordInput);
      if (login_res) {
        participationStorageService.saveToken(login_res.data.token);
        this.token = await participationStorageService.getToken();
      } else {
        this.error = true;
      }

    },
    imageFileChangedHandler(b64String) {
      this.questionImage = b64String;
    },
    listQuestion() {
      this.$router.push('/ListQuestions');
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
      this.questionPosition = this.totalNumberOfQuestion + 1;
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
      this.$router.push('/ListQuestions');
    },
  },
  components: { ImageUpload },
  async created() {
    console.log("admin page");

    var totalQuestion = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestion = totalQuestion.data.size;

  }
};
</script>

<style>
.formulaire {
  left: -83%;
}

.formulaireQuest {
  right: -340px;
  text-align: center;
  font-family: 'Poppins', sans-serif;
  font-size: 20px;
}
</style>