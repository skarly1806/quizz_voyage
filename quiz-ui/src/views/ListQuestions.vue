<script setup>
</script>

<template>

  <p>Liste de questions</p>

  <div v-if="token" id="table-wrapper" style="left:-30%;top:0%;width:1000px;">
    <div id="table-scroll" style="height:715px;">
      <table id="customers" class="relative" style=" top:-2%;left:10%;">
        <thead>
          <tr>
            <th>titre</th>
            <th>text</th>
            <th>rep1</th>
            <th>rep2</th>
            <th>rep3</th>
            <th>rep4</th>
            <th>supprimer</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="unit in list" :key="unit.id">
            <td>{{ unit["title"] }}</td>
            <td>{{ unit["text"] }}</td>
            <td>{{ unit["possibleAnswers"][0]["text"] }}</td>
            <td>{{ unit["possibleAnswers"][1]["text"] }}</td>
            <td>{{ unit["possibleAnswers"][2]["text"] }}</td>
            <td>{{ unit["possibleAnswers"][3]["text"] }}</td>
            <td><button @click="deleteQuest(unit.id)">supprimer</button></td>
          </tr>
        </tbody>
      </table>
    </div>
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




export default {
  name: "AdminPage",
  data() {
    return {
      token: '',
      currentQuestionPosition: 1,
      currentQuestion: {
        image: "",
        position: "",
        text: "",
        title: "",
        possibleAnswers: ["", "", "", ""],
      },
      list: [],
      idd: 1,

    };
  },
  methods: {
    async loginAgain() {
      var login_result = await quizApiService.login(this.passwordInput);
      participationStorageService.saveToken(login_result.data.token);
      this.token = await participationStorageService.getToken();
    },
    async deleteQuest(id) {
      //this.idd = id;
      await quizApiService.deleteQuestion(this.idd, this.token);
      console.log("delete");
      console.log(this.token);
      console.log(this.idd);
    },
  },
  async created() {
    console.log("liste questions page");
    var totalQuestion = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestion = totalQuestion.data.size;
    for (let i = 1; i < this.totalNumberOfQuestion; i++) {
      var questionByPosition = await quizApiService.getQuestionByPos(i);
      this.currentQuestion = questionByPosition.data
      this.list.push(this.currentQuestion);
    }
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