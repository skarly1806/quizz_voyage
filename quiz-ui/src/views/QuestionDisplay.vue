<script setup>
</script>

<template>
  <h1>Question Display</h1>

  <img v-if="question.image" :src="question.image" />


  {{ question.tile }}
  {{ question.answer1 }}
  <a @click="$emit('click-on-answer', 1)">La réponse A</a>
  <a @click="$emit('click-on-answer', 2)">La réponse B</a>
  <a @click="$emit('click-on-answer', 3)">La réponse C</a>
  <a @click="$emit('click-on-answer', 4)">La réponse D</a>

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