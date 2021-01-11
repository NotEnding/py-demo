#-*- coding:utf-8 _*- 
""" 
@file: test_tclient_new.py
@time: 2020/08/27
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

# 实现了客户端用于发送数据并打印接收到 server 端处理后的数据
import grpc
from PythonRpc.proto_py import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT) # 监听频道
    client = data_pb2_grpc.FormatDataStub(channel=conn) # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    response = client.DoFormat(data_pb2.Data(text='hello,world!'))  # 返回的结果就是proto中定义的类
    print("received: " + response.text)

if __name__ == '__main__':
    run()