import tornado.ioloop
import tornado.web
from handler import *
from common import Db, Redis
from route import route
from tornado.gen import coroutine
from tornado.concurrent import Future
def hello_timer():
    #print("hello timer")
    pass
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
    iol = tornado.ioloop.IOLoop.current()
    #定时器 毫秒为单位
    tornado.ioloop.PeriodicCallback(
        hello_timer,1000
    ).start()
    print('app start on',8000)
    iol.start()

