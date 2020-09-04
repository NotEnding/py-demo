#-*- coding:utf-8 _*- 
""" 
@file: delicious_food.py 
@time: 2020/09/03
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
import json
import time
import random
from requests import adapters


def queryDelicious(keywords:str,city:str,key:str):
    """
    :key: 高德地图开放API key 'xxxxx'
    :param court_name:
    :return:
    """

    api = f'https://restapi.amap.com/v3/place/text?key={key}&keywords={keywords}&city={city}&children=1&offset=10&page=1&extensions=all'
    for retry in range(3):
        try:
            response = requests.get(api).json()
            if response['status'] != "1":
                continue
            top_10_dict = {}
        except (json.JSONDecodeError, adapters.SSLError, requests.exceptions.ReadTimeout,IndexError):
            time.sleep(random.random() * 2)
            continue
        else:
            break
    else:
        return None
    return response




if __name__ == '__main__':
    keyword = "美食"
    city = '平顶山市'
    key = "XXXXXX"
    queryDelicious(keyword,city,key)

