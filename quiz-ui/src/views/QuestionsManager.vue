<script setup>
</script>

<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />

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
        questionTitle: "",
        questionText: "",
        possibleAnswers: [],
      },
      currentQuestionPosition: 1,
      list: [],
    };
  },
  methods: {
    answerClickedHandler(value) {
      this.list.push(this.value);
      currentQuestionPosition = currentQuestionPosition + 1;
      this.currentQuestion = loadQuestionByPosition(currentQuestionPosition);
      this.$router.push('/QuestionsManager');
    },
    loadQuestionByPosition(currentQuestionPosition) {
      var questionByPosition = quizApiService.getQuestion(currentQuestionPosition);
      return currentQuestion = questionByPosition.data;
    },
    endQuiz() {
      //push resultat;
    },
  },
  components: { QuestionDisplay },
  async created() {
    var questionByPosition = await quizApiService.getQuestion(currentQuestionPosition);
    this.currentQuestion = questionByPosition.data;

  }
};
</script>