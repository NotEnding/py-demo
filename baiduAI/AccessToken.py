#-*- coding:utf-8 _*- 
""" 
@file: AccessToken.py 
@time: 2020/09/04
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

'''
获取百度access_token
'''

import requests


# 获取百度授权access_token
def access_token(client_id,client_secret):
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
    headers = {
        'Content-Type':'application/json; charset=UTF-8'
    }
    response = requests.get(host,headers=headers)
    if response:
        content = response.json()
        access_token = content['access_token']
        print(access_token)
        return access_token


if __name__ == '__main__':
    client_id = "xxxx"
    client_secret = "xxxxxx"
    access_token(client_id,client_secret)