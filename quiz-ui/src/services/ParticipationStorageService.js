export default {
  clear() {
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("participationScore", participationScore);
  },
  getParticipationScore() {
    window.localStorage.getItem("participationScore");
  },
  saveList(list) {
    window.localStorage.setItem("list", list);
  },
  getList() {
    window.localStorage.getItem("list");
  }
};