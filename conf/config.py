db_config = {
    'jigeyi' : {
        'host'      : 'localhost',
        'user'      : 'root',
        'password'  : '123456',
        'db'        : 'jigeyi',
        'port'      : 3306,
        'charset'   : 'utf8',
        'num'       : 5 #连接池连接数
    },

    'clw' : {
        'host'      : 'localhost',
        'user'      : 'root',
        'password'  : '123456',
        'db'        : 'clw',
        'port'      : 3306,
        'charset'   : 'utf8',
        'num'       : 5 #连接池连接数
    },
    'shop_1234' : {
        'host'      : 'localhost',
        'user'      : 'root',
        'password'  : '123456',
        'db'        : 'shop_1234',
        'port'      : 3306,
        'charset'   : 'utf8',
        'num'       : 5 #连接池连接数
    }
}

redis_config = {
    'redis' : [{
        'host'      : 'localhost',
        'port'      : 6379,
        'db'        : 0,
        'password'  : ''
    },
    {
        'host': 'localhost',
        'port': 6380,
        'db': 0,
        'password': ''
    }]
}