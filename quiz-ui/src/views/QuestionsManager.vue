<script setup>
</script>

<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <div>
    <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
  </div>
  {{ currentQuestion.text }}

  <hr />

</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionDisplay from '@/views/QuestionDisplay.vue'



export default {
  name: "QuestionManager",
  data() {
    return {
      AnswerValue: "No Answer yet",
      totalNumberOfQuestion: 10,
      currentQuestion: {
        image: "",
        position: "",
        text: "testtext",
        title: "testtitle",
        possibleAnswers: ["rep1", "rep2", "rep3", "rep4"],
      },
      currentQuestionPosition: 1,
      list: [],
    };
  },
  methods: {
    async answerClickedHandler(value) {
      this.list.push(this.value);
      this.currentQuestionPosition = this.currentQuestionPosition + 1;
      this.currentQuestion = await this.loadQuestionByPosition(this.currentQuestionPosition);
    },
    async loadQuestionByPosition(currentQuestionPosition) {
      var questionByPosition = await quizApiService.getQuestionByPos(this.currentQuestionPosition);
      return this.currentQuestion = questionByPosition.data;
    },
    endQuiz() {
      const storelist = JSON.stringify(this.list);

      //push resultat;
    },
  },
  components: { QuestionDisplay },
  async created() {
    var questionByPosition = await quizApiService.getQuestionByPos(this.currentQuestionPosition);
    this.currentQuestion = questionByPosition.data;


  }
};
</script>