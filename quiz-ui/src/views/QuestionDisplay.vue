<script setup>
</script>

<template>
  <h1>Question Display</h1>

  <img v-if="question.image" :src="question.image" />
  <div>
    <div>{{ question.questionTitle }}</div>
    <div>{{ question.questionText }}</div>
    <div><a @click="$emit('answer-selected', 1)">{{ question.possibleAnswers[0] }}</a></div>
    <div><a @click="$emit('answer-selected', 2)">{{ question.possibleAnswers[1] }}</a></div>
    <div><a @click="$emit('answer-selected', 3)">{{ question.possibleAnswers[2] }}</a></div>
    <div><a @click="$emit('answer-selected', 4)">{{ question.possibleAnswers[3] }}</a></div>
  </div>

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