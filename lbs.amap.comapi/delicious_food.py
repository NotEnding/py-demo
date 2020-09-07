# -*- coding:utf-8 _*-
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


def queryDelicious(keywords: str, city: str, key: str):
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
            top_10_list = []
            for poi in response['pois']:
                poi_dict = {
                    "name": poi['name'],  # 店名
                    "type": poi['type'],  # 餐厅类别,
                    "tag": poi['tag'],  # 标签
                    "cost": poi['biz_ext'].get('cost', '0.00'),  # 人均消费
                    "rating": poi['biz_ext'].get("rating", '0.0'),  # 评分
                    "tel": poi['tel'],  # 联系电话
                    "pname": poi['pname'],  # 省
                    "cityname": poi['cityname'],  # 市
                    "adname": poi['adname'],  # 区
                    "address": poi['address'],  # 位置
                }
                top_10_list.append(poi_dict)
        except (json.JSONDecodeError, adapters.SSLError, requests.exceptions.ReadTimeout, IndexError):
            time.sleep(random.random() * 2)
            continue
        else:
            break
    else:
        return None
    return top_10_list


if __name__ == '__main__':
    keyword = "美食"
    city = '武汉市'
    key = "高德api key"
    top_10_list = queryDelicious(keyword, city, key)
    if not top_10_list:
        print('未查询到该城市的美食')
    else:
        for t in top_10_list:
            print(t)
