var Mock = require("./mock");

Mock.setup({
  timeout: 200
});

// 主持人阶段榜单
Mock.mock(/compere_step_list/, {
  "status": 0,
  "compereList|30": [
    {
      "uid|9999-91000000" : 123456,
      "nick" : "主持昵称主持昵称主持昵称主持昵称主持昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000,
      "sid" : 87814665,
      "ssid" : 87814665,
      "contractSid" : 86
    }
  ]
});

// 主持人贡献榜单
Mock.mock(/compere_contribution_list/, {
  "status": 0,
  "userList|20": [
    {
      "uid|9999-91000000" : 123456,
      "nick" : "带少妇先走",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000
    }
  ]
});

// 公会阶段
Mock.mock(/guild_group_step_list/, {
  "status": 0,
  "guildList|20":[
    {
      "sid|80000000-89999999": 87814665,
      "asid|100-999" : 87814665,
      "name" : "交友昵称交友昵称交友昵称交友昵称交友昵称交友昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000
    }
  ]
});

// 公会
Mock.mock(/guild_list/, {
  "status": 0,
  "guildList|30":[
    {
      "sid|80000000-89999999": 87814665,
      "asid|100-999" : 87814665,
      "name" : "交友昵称交友昵称交友昵称交友昵称交友昵称交友昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000
    }
  ]
});

// 公会贡献
Mock.mock(/guild_contribution_list/, {
  "status": 0,
  "userList|20": [
    {
      "uid|9999-91000000" : 123456,
      "nick" : "带少妇先走",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000
    }
  ]
});

// 最佳公会
Mock.mock(/guild_compete_step_list/, {
  "status": 0,
  "guildStep1|16":[
    {
      "groupname": 'B3',
      "sid|80000000-89999999": 87814665,
      "asid|100-99999" : 87814665,
      "name" : "交友昵称交友昵称交友昵称交友昵称交友昵称交友昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000,
      "win": false
    }
  ],
  "guildStep2|8":[
    {
      "sid|80000000-89999999": 87814665,
      "asid|100-99999" : 87814665,
      "name" : "交友昵称交友昵称交友昵称交友昵称交友昵称交友昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000,
      "win": false
    }
  ],
  "guildStep3|4":[
    {
      "sid|80000000-89999999": 87814665,
      "asid|100-99999" : 87814665,
      "name" : "交友昵称交友昵称交友昵称交友昵称交友昵称交友昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000,
      "win": false
    }
  ],
  "guildStep4|2":[
    {
      "sid|80000000-89999999": 87814665,
      "asid|100-99999" : 87814665,
      "name" : "交友昵称交友昵称交友昵称交友昵称交友昵称交友昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000,
      "win": false
    }
  ]
});

// 查询公会排名
Mock.mock(/guild_rank_info/, {
  "status":0,
  "group":'B',
  "rank":11
});



// 主持阶段榜单
Mock.mock(/compere_stage_list/, {
  "status": 0,
  "compereList|15": [
    {
      "uid" : 123456,
      "nick" : "交友昵称交友昵称交友昵称交友昵称交友昵称交友昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000,
      "sid" : 87814665,
      "ssid" : 87814665,
      "contractSid" : 86
    }
  ]
});

// 主持阶段榜单
Mock.mock(/dark_horse_list/, {
  "status": 0,
  "darkHorseList|3": [
    {
      "uid" : 123456,
      "nick" : "交友昵称交友昵称交友昵称交友昵称交友昵称交友昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value|9999-91000000" : 10000,
      "sid" : 87814665,
      "ssid" : 87814665,
      "contractSid" : 86
    }
  ]
});

// 王者榜单
Mock.mock(/rich_man_list/, {
  "status": 0,
  "richList|30": [
    {
      "uid" : 123456,
      "nick" : "王者昵称王者昵称王者昵称王者昵称王者昵称王者昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "nobleGrade" : 100,
      "value|9999-91000000" : 10000
    }
  ]
});

// 管理榜单
Mock.mock(/admin_info_list/, {
  "status": 0,
  "adminList|30": [
    {
      "uid" : 123456,
      "nick" : "管理昵称管理昵称管理昵称管理昵称管理昵称管理昵称管理昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "nobleGrade" : 100,
      "value|9999-91000000" : 10000
    }
  ]
});

// Y阅实时战报
Mock.mock(/queryWithCount/, {
  "code": 1,
  "list": [
    {
      "content": "http://zymsc.bs2cdn.yy.com/e10d6c8b-0e1d-4116-85a5-c17928b21973",
      "contentView": "http://zymsc.bs2cdn.yy.com/ab4d6aeb-5aed-41f8-a3ac-ecd8e23e3a26",
      "createDate": 1480493954000,
      "id": 52703,
      "isPopSend": "S02",
      "messageSource": "S02",
      "messageUrl": "http://yue.yy.com/msg/52703?from=jiaoyou",
      "msgDesc": "6080开业活动期间，一个月的黄马价格已经上升到5200块。高昂的价格背后是美女交友类的尊贵服务。",
      "msgImg": "http://zymsc.bs2cdn.yy.com/e3c92c61-572b-4292-ab69-aec6010eda0e",
      "msgImgMd5": "f49715d4a0b4175fb47e4f31c9ed7db4",
      "msgImgView": "http://zymsc.bs2cdn.yy.com/9f9d648d-ad48-4565-a3b6-e8632d9175c9",
      "msgImgViewShow": "S02",
      "msgListImg": "http://zymsc.bs2cdn.yy.com/f732c9f5-6775-4899-ade5-bab228f171d3",
      "msgTitle": "6080黄马价格创历史新高",
      "msgType": "S02",
      "publisherId": 148,
      "publisherName": "YY交友",
      "readAmount": 898,
      "sendDate": 1480493952000,
      "sentAmount": 445559,
      "status": "S04",
      "topicId": 241,
      "volumeControl": 0
    }
  ]
});

// 时段冠军
Mock.mock(/hour_champion/, {
  "status": 0,
  "compereChampion": [
    {
      "uid" : 123456,
      "nick" : "主持昵称主持昵称主持昵称主持昵称主持昵称主持昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value" : 10000,
      "sid" : 87814665,
      "ssid" : 87814665,
      "contractSid" : 86
    }
  ],
  "guildChampion": [
    {
      "uid" : 123456,
      "nick" : "公会昵称公会昵称公会昵称公会昵称公会昵称公会昵称",
      "avatarInfo" : "http://s1.yy.com/guild/header/10001.jpg",
      "value" : 10000,
      "sid" : 87814665,
      "ssid" : 87814665,
      "contractSid" : 86
    }
  ]
});


// 点亮
Mock.mock(/settailight/, {
  status: 0
});