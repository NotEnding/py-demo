# -*- coding:utf-8 _*-
""" 
@file: weatherInfo.py 
@time: 2020/08/07
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

import random
import time

import requests
import json

from requests import adapters


def queryWeather(city_code: str):
    """
    :key: 高德地图开放API key 'dc05e6ec151250ce99dd14143a5354bd'
    :param court_name:
    :return:
    """

    api = f'https://restapi.amap.com/v3/weather/weatherInfo?city={city_code}&output=JSON&key=dc05e6ec151250ce99dd14143a5354bd'
    for retry in range(3):
        try:
            response = requests.get(api).json()
            if response['status'] != "1":
                continue
        except (json.JSONDecodeError, adapters.SSLError, requests.exceptions.ReadTimeout, IndexError):
            time.sleep(random.random() * 2)
            continue
        else:
            break
    else:
        return None
    return response


if __name__ == '__main__':
    city_code = '420100'
    res = queryWeather(city_code)
    print(res)
