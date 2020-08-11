# -*- coding:utf-8 _*-
""" 
@file: address_decode.py
@time: 2020/08/03
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


def queryAddress(address:str):
    """
    :key: 高德地图开放API key 'dc05e6ec151250ce99dd14143a5354bd'
    :param court_name:
    :return:
    """

    api = f'https://restapi.amap.com/v3/geocode/geo?address={address}&output=JSON&key=dc05e6ec151250ce99dd14143a5354bd'
    for retry in range(3):
        try:
            response = requests.get(api).json()
            if response['status'] != "1":
                continue
            result = {
                "province": response['geocodes'][0]['province'],
                "city": response['geocodes'][0]['city'],
                "district": response['geocodes'][0]['district'],
                "address":response['geocodes'][0]['formatted_address']
            }
        except (json.JSONDecodeError, adapters.SSLError, requests.exceptions.ReadTimeout,IndexError):
            time.sleep(random.random() * 2)
            continue
        else:
            break
    else:
        return None
    return result




if __name__ == '__main__':
    court_name = "江苏省丰县人民法院"
    json_data = queryAddress(court_name)
    print(json_data)
