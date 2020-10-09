#-*- coding:utf-8 _*- 
""" 
@file: client.py 
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
# import websocket
#
#
# def on_message(ws, message):
#     print(ws)
#     print(message)
#
#
# def on_error(ws, error):
#     print(ws)
#     print(error)
#
#
# def on_close(ws):
#     print(ws)
#     print("### closed ###")
#
#
# websocket.enableTrace(True)
# ws = websocket.WebSocketApp("ws://192.168.9.31:8080/ws",
#                             on_message=on_message,
#                             on_error=on_error,
#                             on_close=on_close)
#
# ws.run_forever()


from websocket import create_connection
ws = create_connection("ws://192.168.9.26:8080/status")
print("Sending ‘Hello, World‘...")
# ws.send("这是我需要呵呵才能够")
# print("Sent")
# print("Receiving...")
result =  ws.recv()
print("Received ‘%s‘" % result)
ws.close()