export default {
  clear() {
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem('participationScore', participationScore);
  },
  getParticipationScore() {
    return window.localStorage.getItem('participationScore');
  },
  saveList(list) {
    window.localStorage.setItem('list', list);
  },
  getList() {
    return window.localStorage.getItem('list');
  },
  saveToken(token) {
    window.localStorage.setItem('token', token);
  },
  getToken() {
    return window.localStorage.getItem('token');
  },
  savePassword(password) {
    window.localStorage.setItem('password', password);
  },
  getPassword() {
    return window.localStorage.getItem('password');
  }
};