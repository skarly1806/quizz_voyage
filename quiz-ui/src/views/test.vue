<template>
  <input type="text" v-model="textValue" />
  <hr />
  <button class="btn btn-primary" @click="buttonClickHandler">Count</button>
  <hr />
  "{{ textValue }}" has {{ lettersCount }} chars
</template>

<script>
export default {
  name: "test",
  data() {
    return {
      textValue: "",
      lettersCount: 0
    };
  },
  methods: {
    buttonClickHandler() {
      console.log('Compute letters count');
      this.lettersCount = this.textValue.length;
    }
  }
};
</script>