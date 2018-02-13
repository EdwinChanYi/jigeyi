var VueTouch = require('vendor/vue-touch');
var tpl = require('./app.html');
var AppHeader = require('../appHeader/appHeader');

Vue.use(VueTouch);

module.exports = Vue.extend({
  name: 'app',
  template: tpl,
  components: {
    AppHeader: AppHeader
  },
  data: function () {
    return {
      message: 'Hello Vue!'
    };
  }
});
