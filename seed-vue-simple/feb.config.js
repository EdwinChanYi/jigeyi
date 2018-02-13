module.exports = {
  css: {
    px2rem: true,
    autoprefixer: true
  },
  project: {
    path: {
      dev: './dev',
      output: '../output/mobile' // PC || mobile
    },
    cdn: ['//web.yystatic.com/', '//web1.yystatic.com/', '//web2.yystatic.come/'] // 最后一个 `/` 随意，不强制
  },
  webpack: {
    externals: {
      jquery: 'jQuery',
      vue: 'Vue',
      hammerjs: 'Hammer'
    },
    provide: {
      $: 'jquery',
      Vue: 'vue'
    }
  }
};
