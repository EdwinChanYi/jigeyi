import tornado.ioloop
import tornado.web
from handler import *
from common import Db, Redis

if __name__ == "__main__":
    settings = {
        'debug': True,
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    }
    app = tornado.web.Application([
        (r"/", TestHandler),
        (r"/test", TestHandler, None, '测试'),
        (r"/shop", ShopHandler, None, '商店'),
        (r"/user", UserHandler, None, '用户'),
        (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler,
         dict(autoreload=True, serve_traceback=True)),
    ], **settings)
    # app = make_app()
    app.listen(8009)
    Db.instance()       #初始化db连接池
    Redis.init()    #初始化redis连接池
    print('app start on',8009)
    tornado.ioloop.IOLoop.current().start()