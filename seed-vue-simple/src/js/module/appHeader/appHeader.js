var tpl = require('./appHeader.html');

module.exports = Vue.extend({
  name: 'app-header',
  template: tpl,
  props: ['message'],
  data: function () {
    return {};
  },
  methods: {
    onTap: function () {
      alert('I am touched!');
    }
  }
});
