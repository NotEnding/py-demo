#-*- coding:utf-8 _*- 
""" 
@file: server.py.py 
@time: 2020/09/16
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    # # 检查跨域请求，允许跨域，则直接return True，否则自定义筛选条件
    def check_origin(self, origin):
        return True

    # 建立连接的时候
    def open(self):
        pass

    # 接收并处理客户端发送过来的消息
    def on_message(self, message):
        self.write_message(u"Your message was: " + message)

    # 关闭连接的时候
    def on_close(self):
        pass


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
        (r'/', IndexPageHandler),
        (r'/ws', WebSocketHandler)
        ]

        settings = {"template_path": "."}
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(5600)
    tornado.ioloop.IOLoop.instance().start()
