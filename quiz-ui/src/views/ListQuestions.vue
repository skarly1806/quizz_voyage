<script setup>
</script>

<template>


  <div id="table-wrapper" style="left:-7%;top:2%;width:1600px;">
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
            <th>test</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="unit in list" :key="unit.position">
            <td>{{ unit["title"] }}</td>
            <td>{{ unit["text"] }}</td>
            <td>{{ unit["possibleAnswers"][0]["text"] }}</td>
            <td>{{ unit["possibleAnswers"][1]["text"] }}</td>
            <td>{{ unit["possibleAnswers"][2]["text"] }}</td>
            <td>{{ unit["possibleAnswers"][3]["text"] }}</td>
            <td><button @click="deleteQuest(unit.position)">supprimer</button></td>
            <td>"............................"</td>
          </tr>
        </tbody>
      </table>
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
    async deleteQuest(number) {
      var tok = await participationStorageService.getToken();
      await quizApiService.deleteQuestion(number, tok);
      console.log("delete");
      console.log(tok);
      console.log(number);
    },
  },
  async created() {
    console.log("list questions page");
    var totalQuestion = await quizApiService.getQuizInfo();
    this.totalNumberOfQuestion = totalQuestion.data.size;
    for (let i = 1; i < this.totalNumberOfQuestion + 1; i++) {
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