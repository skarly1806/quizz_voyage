<script setup>
</script>

<template>
  <div class="questionBorder">
    <img class="rounded mx-auto d-block" v-if="question.image" :src="question.image" style="top:70px;left:0px;" />

    <div class="question">

      <div class="questionBadge">{{ question.title }}</div>
      <div class="questionText">{{ question.text }}</div>
      <div class="answerBloc"><a class="answerText" @click="$emit('click-on-answer', 0)">{{
        question.possibleAnswers[0].text
      }}</a></div>
      <div class="answerBloc"><a class="answerText" @click="$emit('click-on-answer', 1)">{{
        question.possibleAnswers[1].text
      }}</a></div>
      <div class="answerBloc"><a class="answerText" @click="$emit('click-on-answer', 2)">{{
        question.possibleAnswers[2].text
      }}</a></div>
      <div class="answerBloc"><a class="answerText" @click="$emit('click-on-answer', 3)">{{
        question.possibleAnswers[3].text
      }}</a></div>
    </div>
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
.answerText {
  width: 100px;
  font-size: 15px;
}

.question {
  left: 250px;
  top: 150px;
}

.questionText {
  display: inline-block;
  padding: 10px;
  width: 500px;
  height: 75px;
  top: -105px;
  right: 232px;
  font-size: 18px;
  font-weight: 700;
  line-height: 1;
  background-color: rgb(251, 252, 252);
  color: rgb(0, 0, 0);
  text-align: center;
  vertical-align: middle;
  border-radius: 0.25rem;
  border: thick double #32a1ce;
}

.questionBadge {
  display: inline-block;
  padding: 10px;
  top: -435px;
  width: 500px;
  right: 232px;
  font-size: 20px;
  font-weight: 700;
  line-height: 1;
  background-color: rgb(41, 177, 168);
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: 0.25rem;
}

.answerBloc {
  display: inline-block;
  padding: 10px;
  width: 500px;
  height: 40px;
  top: -87px;
  right: 233px;
  font-size: 14px;
  font-weight: 700;
  line-height: 1;
  background-color: rgb(251, 252, 252);
  color: rgb(0, 0, 0);
  text-align: center;
  vertical-align: middle;
  border-radius: 0.25rem;
  border: thick double #32a1ce;
}

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