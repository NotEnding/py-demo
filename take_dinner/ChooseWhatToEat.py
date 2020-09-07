# -*- coding:utf-8 _*-
""" 
@file: ChooseWhatToEat.py 
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
import json
import time
import random

# 随机食物
import requests
from requests import adapters

food = ['土馍', '郏县饸烙面', '舞钢热豆腐', '郏县豆腐菜', '鲁山揽锅菜', '酱焖鸡', '三郎庙牛肉', '宝丰买根烧鸡', '丁记羊汤', '羊肉冲汤', '叶县烩面', '麻辣烫', '麻辣香锅', '冒菜',
        '炸鸡柳', '关东煮', '盖浇饭', '便当', '泡面', '炒菜', '卤丸子', '面条', '馒头', 'KFC', '麦当劳']


def welcome():  # 欢迎语
    print('欢迎小仙女使用小双鱼瞎写的“点餐助手”')
    time.sleep(random.random())
    print('今天中午吃什么呢？\n1.随便吃点\n2.下馆子\n3.自定义三选一\n4.退出')


def print_choice(a):  # 选择
    if a in top_10_names:
        print(f"小双鱼帮您选择了 ** {a} **,小仙女，这家店的信息如下：")
        print()
        for poi in top_10_list:
            if poi['店名'] == a:
                for k, v in poi.items():
                    print(f"{k}:{v}")
    else:
        print(f"小双鱼帮您选择了** {a} **")
    print()
    print('小仙女满意么？满意请输入1，不满意请输入2：')


def end_choice(a):  # 结束语
    print('小仙女的选择是%s,小双鱼想你哦，多吃点！' % a)
    print('10秒后，将会自动关闭系统哦，小仙女再见了~~~~')
    time.sleep(20)


def get_res():  # 取得餐厅列表
    res_reserve = []
    print('请输入您心仪的三家餐厅')
    for i in range(3):
        a = input('请输入第%s家餐厅：' % (i + 1))
        res_reserve.append(a)
    return (res_reserve)


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
                    "店名": poi['name'],  # 店名
                    "餐厅类别": poi['type'],  # 餐厅类别,
                    "标签": poi['tag'],  # 标签
                    "人均消费": poi['biz_ext'].get('cost', '0.00'),  # 人均消费
                    "评分": poi['biz_ext'].get("rating", '0.0'),  # 评分
                    "联系电话": poi['tel'],  # 联系电话
                    "省": poi['pname'],  # 省
                    "市": poi['cityname'],  # 市
                    "区": poi['adname'],  # 区
                    "详细地址": poi['address'],  # 位置
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


# 欢迎
welcome()

# 获取高德poi
key = "高德api key"
top_10_list = queryDelicious('美食', '平顶山市', key)
top_10_names = [top['店名'] for top in top_10_list]

main_choice = int(input('请选择：'))
while main_choice == 1:
    food_try = random.choice(food)
    print_choice(food_try)
    a = int(input('请选择：'))
    if a == 1:
        end_choice(food_try)
        break

while main_choice == 2:
    print()
    print('为你找到新华区附近的Top10美食:\n')
    for name in top_10_names:
        print(name)
    print()
    print('.....小仙女稍等哦，小双鱼正在帮您做选择.....')
    print()
    res_try = random.choice(top_10_names)
    print_choice(res_try)
    a = int(input('请选择：'))
    if a == 1:
        end_choice(res_try)
        break

if main_choice == 3:
    res3 = get_res()
    while True:
        res_try = random.choice(res3)
        print_choice(res_try)
        a = int(input('请选择：'))
        if a == 1:
            end_choice(res_try)
            break

elif main_choice == 4:
    end_choice('“结束”')
