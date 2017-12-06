import tornado.ioloop
import tornado.web
from controller import *
from common import Db, Redis

# 当做是基类控制器测试
class MainHandler(tornado.web.RequestHandler):

    def _param_filter(self):
        return {}

    # 初始化
    def prepare(self):
        pass

    # 获取参数
    def _get_param(self):
        param = {}  # 所有参数字典
        args = self.request.arguments
        for key in args:
            param[key] = self.get_argument(key)
        filter = self._param_filter().get(self.request.method)
        if (filter != None):
            print('None')

        print(filter)
        return param

    # 清理和日志
    def on_finish(self):
        pass

    def get(self):
        self._get_param()
        self.write("Hello, world")

    def post(self):
        self._get_param()
        self.write("post")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    settings = {
        'debug': True,
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    }
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/test", TestHandler),
        (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler,
         dict(autoreload=True, serve_traceback=True)),
    ], **settings)
    # app = make_app()
    app.listen(8888)
    Db.init()       #初始化db连接池
    Redis.init()    #初始化redis连接池
    print('app start1')
    tornado.ioloop.IOLoop.current().start()