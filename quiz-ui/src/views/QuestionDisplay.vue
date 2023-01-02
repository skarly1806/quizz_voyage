<script setup>
</script>

<template>

  <img class="rounded mx-auto d-block" v-if="question.image" :src="question.image" />
  <div>
    <div class="badge bg-primary text-wrap" style="width: 20rem;">{{ question.title }}</div>
    <div>{{ question.text }}</div>
    <div><a @click="$emit('click-on-answer', 1)">{{ question.possibleAnswers[0].text }}</a></div>
    <div><a @click="$emit('click-on-answer', 2)">{{ question.possibleAnswers[1].text }}</a></div>
    <div><a @click="$emit('click-on-answer', 3)">{{ question.possibleAnswers[2].text }}</a></div>
    <div><a @click="$emit('click-on-answer', 4)">{{ question.possibleAnswers[3].text }}</a></div>
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

<style>

</style>