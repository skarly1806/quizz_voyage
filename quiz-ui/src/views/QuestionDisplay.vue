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
div[class*=box] {
  height: 33.33%;
  width: 40%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.box-3 {
  background-color: #66A182;
}

.btn {
  line-height: 50px;
  height: 50px;
  text-align: center;
  width: 250px;
  cursor: pointer;
}

/* 
========================
      BUTTON THREE
========================
*/
.btn-three {
  color: #FFF;
  transition: all 0.5s;
  position: relative;
}

.btn-three::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  background-color: rgba(255, 255, 255, 0.1);
  transition: all 0.3s;
}

.btn-three:hover::before {
  opacity: 0;
  transform: scale(0.5, 0.5);
}

.btn-three::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  opacity: 0;
  transition: all 0.3s;
  border: 1px solid rgba(255, 255, 255, 0.5);
  transform: scale(1.2, 1.2);
}

.btn-three:hover::after {
  opacity: 1;
  transform: scale(1, 1);
}
</style>