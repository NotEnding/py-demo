#-*- coding:utf-8 _*- 
""" 
@file: Animation.py 
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
import requests
import base64

'''
人像动漫化
'''




# 二进制方式打开图片文件
f = open('./hx.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '[调用鉴权接口获取的token]'

request_url = f'https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime?access_token={access_token}'

headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    content = response.json()
    img_str = content['image']
    img_data = base64.b64decode(img_str)
    # 注意：如果是"data:image/jpg:base64,"，那你保存的就要以png格式，如果是"data:image/png:base64,"那你保存的时候就以jpg格式。
    with open('./hx_animation.png', 'wb') as f:
        f.write(img_data)
    print('transmission complete')