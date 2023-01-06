<script setup>
</script>

<template>
  <div class="bg">
  </div>

  <div id="table-wrapper" style="right:117%;top:10%;">
    <div id="table-scroll">
      <table id="customers" class="relative" style=" top:-5%;left:0%;height:360px;">
        <thead>
          <tr>
            <th>Player Name</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="unit in registeredScores" :key="unit.id">
            <td>{{ unit["playerName"] }}</td>
            <td>{{ unit["score"] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="wrapperHome" style="left: 34%;
  top: 25%;">
    <a class="cta" href="#" style="left:-100px;top:-250px;">
      <span @click="launchNewQuiz">Commencer !</span>
      <span @click="launchNewQuiz">
        <svg width="66px" height="43px" viewBox="0 0 66 43" version="1.1" xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink">
          <g id="arrow" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
            <path class="one"
              d="M40.1543933,3.89485454 L43.9763149,0.139296592 C44.1708311,-0.0518420739 44.4826329,-0.0518571125 44.6771675,0.139262789 L65.6916134,20.7848311 C66.0855801,21.1718824 66.0911863,21.8050225 65.704135,22.1989893 C65.7000188,22.2031791 65.6958657,22.2073326 65.6916762,22.2114492 L44.677098,42.8607841 C44.4825957,43.0519059 44.1708242,43.0519358 43.9762853,42.8608513 L40.1545186,39.1069479 C39.9575152,38.9134427 39.9546793,38.5968729 40.1481845,38.3998695 C40.1502893,38.3977268 40.1524132,38.395603 40.1545562,38.3934985 L56.9937789,21.8567812 C57.1908028,21.6632968 57.193672,21.3467273 57.0001876,21.1497035 C56.9980647,21.1475418 56.9959223,21.1453995 56.9937605,21.1432767 L40.1545208,4.60825197 C39.9574869,4.41477773 39.9546013,4.09820839 40.1480756,3.90117456 C40.1501626,3.89904911 40.1522686,3.89694235 40.1543933,3.89485454 Z"
              fill="#FFFFFF"></path>
            <path class="two"
              d="M20.1543933,3.89485454 L23.9763149,0.139296592 C24.1708311,-0.0518420739 24.4826329,-0.0518571125 24.6771675,0.139262789 L45.6916134,20.7848311 C46.0855801,21.1718824 46.0911863,21.8050225 45.704135,22.1989893 C45.7000188,22.2031791 45.6958657,22.2073326 45.6916762,22.2114492 L24.677098,42.8607841 C24.4825957,43.0519059 24.1708242,43.0519358 23.9762853,42.8608513 L20.1545186,39.1069479 C19.9575152,38.9134427 19.9546793,38.5968729 20.1481845,38.3998695 C20.1502893,38.3977268 20.1524132,38.395603 20.1545562,38.3934985 L36.9937789,21.8567812 C37.1908028,21.6632968 37.193672,21.3467273 37.0001876,21.1497035 C36.9980647,21.1475418 36.9959223,21.1453995 36.9937605,21.1432767 L20.1545208,4.60825197 C19.9574869,4.41477773 19.9546013,4.09820839 20.1480756,3.90117456 C20.1501626,3.89904911 20.1522686,3.89694235 20.1543933,3.89485454 Z"
              fill="#FFFFFF"></path>
            <path class="three"
              d="M0.154393339,3.89485454 L3.97631488,0.139296592 C4.17083111,-0.0518420739 4.48263286,-0.0518571125 4.67716753,0.139262789 L25.6916134,20.7848311 C26.0855801,21.1718824 26.0911863,21.8050225 25.704135,22.1989893 C25.7000188,22.2031791 25.6958657,22.2073326 25.6916762,22.2114492 L4.67709797,42.8607841 C4.48259567,43.0519059 4.17082418,43.0519358 3.97628526,42.8608513 L0.154518591,39.1069479 C-0.0424848215,38.9134427 -0.0453206733,38.5968729 0.148184538,38.3998695 C0.150289256,38.3977268 0.152413239,38.395603 0.154556228,38.3934985 L16.9937789,21.8567812 C17.1908028,21.6632968 17.193672,21.3467273 17.0001876,21.1497035 C16.9980647,21.1475418 16.9959223,21.1453995 16.9937605,21.1432767 L0.15452076,4.60825197 C-0.0425130651,4.41477773 -0.0453986756,4.09820839 0.148075568,3.90117456 C0.150162624,3.89904911 0.152268631,3.89694235 0.154393339,3.89485454 Z"
              fill="#FFFFFF"></path>
          </g>
        </svg>
      </span>
    </a>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
      password: "",
    };
  },
  methods: {
    launchNewQuiz() {
      this.$router.push('/start-new-quiz-page');
    },
    async launchAdminPage() {
      participationStorageService.savePassword(this.password);
      this.$router.push('/AdminPage');
    },
  },
  async created() {
    var quizInfoApiResult = await quizApiService.getQuizInfo();
    this.registeredScores = quizInfoApiResult.data.scores;
    participationStorageService.clear();
    console.log("Composant Home page 'created'");
  }
};
</script>

<style>
.bg {
  background-image: url("../assets/fondSite.png");
  background-size: cover;
  left: 70px;
  width: 1472px;
  height: 750px;
}


div.container {
  left: -100%;
  bottom: 150%;
  /* position: relative; */
  min-height: 10em;
  max-height: 360px;
  display: table-cell;
  /* margin-left: auto;
  margin-right: auto; */
}

@import url('https://fonts.googleapis.com/css?family=Poppins:900i');

* {
  box-sizing: border-box;
}



body {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.wrapperHome {
  display: flex;
  justify-content: center;
}

.ctaHome {
  display: flex;
  padding: 10px 60px;
  text-decoration: none;
  font-family: 'Poppins', sans-serif;
  font-size: 40px;
  color: white;
  background: #548fed;
  transition: 1s;
  box-shadow: 6px 6px 0 #b0efb2;
  transform: skewX(-15deg);
}

.ctaHome:focus {
  outline: none;
}

.ctaHome:hover {
  transition: 0.5s;
  box-shadow: 10px 10px 0 #548fed;
}

.ctaHome span:nth-child(2) {
  transition: 0.5s;
  margin-right: 0px;
}

.ctaHome:hover span:nth-child(2) {
  transition: 0.5s;
  margin-right: 45px;
}

span {
  transform: skewX(15deg)
}

span:nth-child(2) {
  width: 20px;
  margin-left: 30px;
  position: relative;
  top: 12%;
}

/**************SVG****************/

path.one {
  transition: 0.4s;
  transform: translateX(-60%);
}

path.two {
  transition: 0.5s;
  transform: translateX(-30%);
}

.ctaHome:hover path.three {
  animation: color_anim 1s infinite 0.2s;
}

.ctaHome:hover path.one {
  transform: translateX(0%);
  animation: color_anim 1s infinite 0.6s;
}

.ctaHome:hover path.two {
  transform: translateX(0%);
  animation: color_anim 1s infinite 0.4s;
}

/* SVG animations */

@keyframes color_anim {
  0% {
    fill: white;
  }

  50% {
    fill: #548fed;
  }

  100% {
    fill: white;
  }
}

.relative {
  width: 500px;
  max-height: 360px;
  top: -30px;
  text-align: center;
}

#customers {
  left: 55%;
  top: 10%;
  font-family: 'Poppins', sans-serif;
  border-collapse: collapse;
  width: 40%;
  max-height: 360px;
}

#customers td,
#customers th {
  border: 1px solid #ddd;
  padding: 10px;
  padding-top: 2px;
  padding-bottom: 2px;
}

#customers tr:nth-child(even) {
  background-color: #f2f2f2;
}

#customers tr:hover {
  background-color: #ddd;
}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #b0efb2;
  color: white;
}

img {
  position: relative;
  top: 100px;
  left: -350px;
  display: block;
  margin-left: auto;
  margin-right: 10px;
  margin-top: -400px;
  size: 2000%;
}
</style>