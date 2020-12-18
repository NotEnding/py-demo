# -*- coding:utf-8 _*-
""" 
@file: server.py 
@time: 2020/10/13
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

import socket

BUF_SIZE = 1024
host = 'localhost'
port = 8083

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)  # 接收的连接数
client, address = server.accept()  # 因为设置了接收连接数为1，所以不需要放在循环中接收
while True:  # 循环收发数据包，长连接
    data = client.recv(BUF_SIZE)
    print(data.decode())  # python3 要使用decode
    # client.close() #连接不断开，长连接