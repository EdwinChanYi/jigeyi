db_config = {
    'master' : {
        'host'      : 'localhost',
        'user'      : 'root',
        'password'  : 'root',
        'db'        : 'test',
        'port'      : 3306,
        'charset'   : 'utf8',
        'num'       : 5 #连接池连接数
    },

    'slave' : {
        'host'      : 'localhost',
        'user'      : 'root',
        'password'  : 'root',
        'db'        : 'test',
        'port'      : 3306,
        'charset'   : 'utf8',
        'num'       : 5 #连接池连接数
    }
}

redis_config = {
    'redis' : {
        'host'      : 'localhost',
        'port'      : 6379,
        'db'        : 0,
        'password'  : 'lzh'
    }
}