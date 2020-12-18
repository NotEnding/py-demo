#-*- coding:utf-8 _*- 
""" 
@file: monitor.py 
@time: 2020/12/15
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
监控茅台库存量
'''


import threading
import time
from concurrent.futures._base import wait, ALL_COMPLETED
from concurrent.futures.thread import ThreadPoolExecutor

import requests
import json
import re


all_num = 0
lock = threading.Lock()  # 创建一个锁

def requests_url(url):
    headers = {
        "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36"
        }
    for i in range(1, 11):  # 设置重新请求次数
        try:
            # ip_port = self.get_random_proxy()
            # proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
            # response = self.session.get(url, headers=headers, proxies=proxy, timeout=10)
            response = requests.get(url, headers=headers, timeout=5)
            if "rgv587_flag" in response.text:
                continue
            response_dict = json.loads(response.text)
        except Exception as e:
            continue
        else:  # 请求成功
            return response_dict

def check_addr_quantity(area_str):
        area_id,area_name = area_str.split("*")
        # 20739895092飞天茅台  609652081782猪年茅台  610201548194鼠年茅台  609390840832精品茅台  591239141090陈年茅台
        url = f"https://mdskip.m.tmall.com/mobile/queryH5Detail.htm?itemId=20739895092&areaId={area_id}"
        response_dict = requests_url(url)
        try:
            sku_dict = response_dict["skuCore"]["sku2info"]
            for i in sku_dict:
                if i == "0":
                    lock.acquire()
                    print(f"地区：{area_name} area_id:{area_id} 库存:{sku_dict[i]['quantity']}")
                    global all_num
                    all_num += int(sku_dict[i]['quantity'])
                    lock.release()
        except Exception as e:
            print(f"地区：{area_name} area_id：{area_id} 请求出错：{e} ")

def run():
    # 找出每个省的省id
    city_dict = {'440000':'广东省','350000':'福建省','330000':'浙江省',"450000":"广西省","530000":"云南省",
                 "540000":"西藏","510000":"四川省","500000":"重庆市","420000":"湖北省","520000":"贵州省",
                 "430000":"湖南省","360000":"江西省","340000":"安徽省","310000":"上海市","320000":"江苏省",
                 "370000": "山东省", "410000": "河南省","610000":"陕西省","140000":"山西省","620000":"甘肃省",
                 "640000":"宁夏自治区","630000":"青海省","650000":"新疆","150000":"内蒙古",
                 "130000":"河北省","110000":"北京市","120000":"天津市","210000":"辽宁省","220000":"吉林省",
                 "230000":"黑龙江省","460000":"海南省"
                 }
    print(f"共{len(city_dict)}个地区")
    province_list = [key+"*"+city_dict[key] for key in city_dict]
    # 多进程爬每个地区的库存
    executor = ThreadPoolExecutor(max_workers=40)
    all_task = [executor.submit(check_addr_quantity, (area_str)) for area_str in province_list]
    wait(all_task, return_when=ALL_COMPLETED)  # 方法可以让主线程阻塞，要等待所有的任务都结束
    print(f"大陆地区总库存：{all_num}")

if __name__ == "__main__":
    run()