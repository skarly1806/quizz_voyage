import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestionByPos(position) {
    return this.call("get", "questions?position=" + position);
  },
  getQuestionById(id) {
    return this.call("get", "questions/" + id);
  },
  updateQuestion(id) {
    return this.call("put", "questions/" + id);
  },
  login() {
    //implements
  },
  addQuestion() {
    return this.call("post", "questions");
  },
  deleteQuestion(id) {
    return this.call("delete", "questions/" + id);
  },
  deleteAllQuestion() {
    return this.call("delete", "questions/all");
  }
};