import tornado.ioloop
import tornado.web
from handler import *
from common import Db, Redis
from route import route

if __name__ == "__main__":
    settings = {
        'debug': True,
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    }
    app = tornado.web.Application(route, **settings)

    # app = make_app()
    app.listen(8000)
    Db.instance()       #初始化db连接池
    Redis.init()    #初始化redis连接池
    print('app start on',8000)
    tornado.ioloop.IOLoop.current().start()

