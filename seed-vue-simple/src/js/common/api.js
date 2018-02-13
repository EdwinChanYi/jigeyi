var dataType = 'jsonp';
var timeout = 15000;
var url = 'http://fts.yy.com/rank/activitystartpart/';


// require('../dev/mock-data');
// dataType = 'json';


var request = function (opt) {
  return $.ajax({
    dataType: dataType,
    timeout: timeout,
    url: /^http/.test(opt.url) ? opt.url : url + opt.url,
    data: opt.data || null
  });
};


module.exports = {

  /*
   * 主持页面
   */

  // 主持人阶段榜单
  compereStepList: function (group, step) {
    return request({
      url: 'compere_step_list',
      data: {
        group: group,
        step: step
      }
    });
  },

  // 主持人贡献榜单
  compereContributionList: function (uid, group, step) {
    return request({
      url: 'compere_contribution_list',
      data: {
        uid: uid,
        group: group,
        step: step
      }
    });
  },

  /*
   * 管理页面
   */

  // 管理榜单
  administrationList: function (date) {
    return request({
      url: 'administration_list',
      data: {
        date: date
      }
    });
  },

  // 管理贡献榜单
  administrationContributionList: function (uid, date) {
    return request({
      url: 'administration_contribution_list',
      data: {
        uid: uid,
        date: date
      }
    });
  },

  // 获取主持频道管理信息
  adminInfoList: function () {
    return request({
      url: 'admin_info_list'
    });
  },

  // 主持人报名管理
  compereAddAdmin: function (adminUid) {
    return request({
      url: 'compere_add_admin',
      data: {
        adminUid: adminUid
      }
    });
  },

  // 查询主持人报名情况
  compereQueryAdmin: function () {
    return request({
      url: 'compere_query_admin'
    });
  },

  /*
   * 王者页面
   */

  // 神豪榜
  richManList: function (date) {
    return request({
      url: 'rich_man_list',
      data: {
        date: date
      }
    });
  },


  /*
   * 公会页面
   */

  // 工会阶段赛
  guildGroupStepList: function (step, group) {
    return request({
      url: 'guild_group_step_list',
      data: {
        step: step,
        group: group
      }
    });
  },

  // 工会淘汰赛
  guildCompeteStepList: function (step) {
    return request({
      url: 'guild_compete_step_list',
      data: {
        step: step
      }
    });
  },

  // 十大工会和新星工会
  guildList: function (group, type) {
    return request({
      url: 'guild_list',
      data: {
        rankgroup: group,
        ranktype: type
      }
    });
  },

  // 十大工会和新星工会贡献榜单
  guildContributionList: function (sid, type) {
    return request({
      url: 'guild_contribution_list',
      data: {
        sid: sid,
        ranktype: type
      }
    });
  },


  /*
   * 其他
   */

  // 时段冠军
  hourChampion: function () {
    return request({
      url: 'hour_champion'
    });
  },

  // Y阅实时战报
  yYue: function () {
    return request({
      url: 'http://yue.yy.com/yyue/topicMsg/queryWithCount',
      data: {
        topicId: 241,
        count: 1,
        from: 'jiaoyou'
      }
    });
  },

  // 获取主持任务进度
  getCompereTask: function (uid) {
    return request({
      url: 'http://s.fts.yy.com/activity/get_compere_task',
      data: { compereUid: uid }
    });
  },

  // 是否有抽奖资格
  getActivityRewardInfo: function () {
    return request({
      url: 'get_activity_reward_info'
    });
  },

  // 点亮铭牌
  setLight: function () {
    return request({
      url: 'http://s.fts.yy.com/activity/settailight',
      data: {
        tailight_id: 9,
        grade: 1
      }
    });
  },

  // 是否点亮尾灯
  getLight: function () {
    return request({
      url: 'http://s.fts.yy.com/activity/tailight_info',
      data: {
        tailight_id: 9
      }
    });
  },

  // 获取当前阶段主持排名的信息
  compereRankInfo: function (uid, step) {
    return request({
      url: 'compere_rank_info',
      data: {
        uid: uid,
        step: step
      }
    });
  },

  // 获取当前工会排名的信息
  guildRankInfo: function (sid) {
    return request({
      url: 'guild_rank_info',
      data: {
        sid: sid
      }
    });
  },

  // 获取当前正在团战的频道
  battleGroupChannelInfo: function () {
    return request({
      url: 'battle_group_channel_info'
    });
  }

};
