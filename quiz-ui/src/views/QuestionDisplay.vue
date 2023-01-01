<script setup>
</script>

<template>
  <h1>Question Display</h1>

  <img v-if="question.image" :src="question.image" />

  {{ question.questionTitle }}
  {{ question.questionText }}
  {{ question.possibleAnswers[1] }}
  {{ question.possibleAnswers[2] }}
  {{ question.possibleAnswers[3] }}
  {{ question.possibleAnswers[4] }}

</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";



export default {
  name: "QuestionDisplay",
  emits: ['click-on-answer'],
  data() {
    return {
    };
  },
  props: {
    question: {
      type: Object
    }
  },
  methods: {
  },
  created() {

  }
};
</script>