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

import time
import random

# 随机食物
food = ['土馍', '郏县饸烙面', '舞钢热豆腐', '郏县豆腐菜', '鲁山揽锅菜', '酱焖鸡', '三郎庙牛肉', '宝丰买根烧鸡', '丁记羊汤', '羊肉冲汤', '叶县烩面', '麻辣烫', '麻辣香锅', '冒菜',
        '炸鸡柳', '关东煮', '盖浇饭', '便当', '泡面', '炒菜', '卤丸子', '面条', '馒头', 'KFC', '麦当劳']

# top 10餐厅
top_10 = {
    "虾先森火锅": {
        "name": "虾先森火锅",
        "addr": "长安大道和盛时代广场西北",
        "time": "09:30-14:00 17:00-21:30"
    },
    "焖菜青年": {
        "name": "焖菜青年",
        "addr": "卫东区开源路与大众路交叉口鹰城世贸7.1视界购物中心5楼",
        "time": "10:00-20:00"
    },
    "爱鱼味烤全鱼": {
        "name": "爱鱼味烤全鱼",
        "addr": "和盛时代广场顺德路与望湖路交叉口",
        "time": "10:00-21:30"
    },
    "恋尚私房蛋糕(新城区店)": {
        "name": "恋尚私房蛋糕(新城区店)",
        "addr": "未来路蓝湾新城区苏宁小店东行50m",
        "time": "08:00-20:00"
    },
    "燃星人时尚烤肉": {
        "name": "燃星人时尚烤肉",
        "addr": "中兴路13号基泰城5楼",
        "time": "10:00-22:00"
    },
    "胡桃里音乐酒馆": {
        "name": "胡桃里音乐酒馆",
        "addr": "园林路与凌云路交叉口向西50米",
        "time": "10:00-14:00;17:00-21:00"
    },
    "西部大盘鸡(平顶山新城区总店)": {
        "name": "西部大盘鸡(平顶山新城区总店)",
        "addr": "湖滨路街道平顶山学院医学院市卫校西门对面往南50米",
        "time": "11:00-02:00"
    },
    "领鲜潮牛(湛南路店)": {
        "name": "领鲜潮牛(湛南路店)",
        "addr": "河南省平顶山市湛河区湛河南路与西苑东路交口东行80米",
        "time": "09:30-14:00 16:30-22:00"
    },
    "豫上一品": {
        "name": "豫上一品",
        "addr": "河南省平顶山市新华区公园北街与锦绣街交叉口文化宫南门檀宫2楼",
        "time": "10:30-14:00;17:30-21:00"
    },
    "杏花楼(开源路店)": {
        "name": "杏花楼(开源路店)",
        "addr": "开源路与南环路交叉口向北180米路东(平顶山市十三中对面向北70米)",
        "time": "10:00-14:00;17:00-21:00"
    }
}


def welcome():  # 欢迎语
    print('欢迎小仙女使用小双鱼瞎写的“点餐助手”')
    time.sleep(random.random())
    print('今天中午吃什么呢？\n1.随便吃点\n2.下馆子\n3.自定义三选一\n4.退出')


def print_choice(a):  # 选择
    if a in top_10.keys():
        print(f"小双鱼帮您选择了 ** {a} **")
        print(f"店名:{top_10[a]['name']}，地址是:{top_10[a]['addr']}，营业时间:{top_10[a]['time']}")
    else:
        print(f"小双鱼帮您选择了** {a} **")
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


welcome()
main_choice = int(input('请选择：'))
while main_choice == 1:
    food_try = random.choice(food)
    print_choice(food_try)
    a = int(input('请选择：'))
    if a == 1:
        end_choice(food_try)
        break

while main_choice == 2:
    print('为你找到新华区附近的Top10美食:\n')
    top_10_names = list(top_10.keys())
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
