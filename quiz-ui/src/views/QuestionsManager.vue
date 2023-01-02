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
    answerClickedHandler(value) {
      this.list.push(this.value);
      this.currentQuestionPosition = this.currentQuestionPosition + 1;
      this.currentQuestion = loadQuestionByPosition(currentQuestionPosition);
      this.$router.push('/QuestionsManager');
    },
    loadQuestionByPosition(currentQuestionPosition) {
      var questionByPosition = quizApiService.getQuestionByPos(this.currentQuestionPosition);
      return this.currentQuestion = questionByPosition.data;
    },
    endQuiz() {
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