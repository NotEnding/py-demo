# -*- coding:utf-8 _*-
""" 
@file: login_wechat.py 
@time: 2020/08/31
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

from wxpy import Bot
import time
import os
import math
from PIL import Image
import io
import sys

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

# 解决cmd编码的不兼容utf-8，若要解决这问题，改一下python的默认编码成'gb18030'就行
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

bot = Bot(cache_path=True)

my_friends = bot.friends()
# 输出列表，列表第一个元素为自己
print(f"my_friends:{my_friends}")

stas = my_friends.stats_text()
print(f"stas:{stas}")


# # 发送信息
# friends = my_friends.search('你想要发送的人名')[0]
# friends.send('你想要发送的信息')
#
# # 群发信息
# my_friends = bot.friends()
# for i in my_friends[1:]:
#     a = i.name
#     friend = my_friends.search(a)[0]
#     print('正在发送', friend)
#     friend.send('')  # 你想要发送的内容
#     print('ok')
#     time.sleep(random.random() * 2)  # 由于发送消息太快最后加上一个延迟
#
# # 消息轰炸
# friends = my_friends.search('你想要发送的人名')[0]
# for i in range(50):
#     friends.send('你想要发送的信息')


# 获得好友头像
def CREATE_PICPATHT():
    path = os.getcwd() + "\\pic\\"
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def IMAGE_SAVE(path):
    my_friends = bot.friends()
    num = 0
    for friend in my_friends:
        print(friend.name)
        friend.get_avatar(path + '\\' + str(num) + ".jpg")
        num = num + 1


path = CREATE_PICPATHT()
IMAGE_SAVE(path)


# 头像拼接
def PJ_IMAGE(path):
    length = len(os.listdir(path))
    image_size = 2560
    each_size = math.ceil(2560 / math.floor(math.sqrt(length)))
    x_lines = math.ceil(math.sqrt(length))
    y_lines = math.ceil(math.sqrt(length))
    image = Image.new('RGB', (each_size * x_lines, each_size * y_lines))
    x = 0
    y = 0
    for (root, dirs, files) in os.walk(path):
        for pic_name in files:
            try:
                with Image.open(path + pic_name) as img:
                    img = img.resize((each_size, each_size))
                    image.paste(img, (x * each_size, y * each_size))
                    x += 1
                    if x == x_lines:
                        x = 0
                        y += 1
            except IOError:
                print("头像读取失败")
        img = image.save(os.getcwd() + "/wechat.png")
        print('已完成')


PJ_IMAGE(path)
