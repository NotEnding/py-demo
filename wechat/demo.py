# -*- coding:utf-8 _*-
""" 
@file: demo.py 
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
from wxpy import *
import os
import tkinter as tk
import tkinter
import math
from PIL import Image
import time
import random
import io
import sys


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

# 解决cmd编码的不兼容utf-8，若要解决这问题，改一下python的默认编码成'gb18030'就行
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

window = tkinter.Tk()
window.title('微信')
window.geometry("800x480")
bot = Bot(cache_path=True)
l1 = tk.Label(window, text="第一行输入用户名第二行输入信息",
              font=("黑体", 10))
l1.pack()
ask_text = tk.Entry(background='orange')
ask_text.pack()
ask_text1 = tk.Entry(background='pink')
ask_text1.pack()


def onclick():
    a = ask_text.get()
    my_friends = bot.friends()
    friends = my_friends.search(a)
    return friends[0]


def onclick1():
    a = ask_text1.get()
    return a


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


def CREATE_TXTPATH():
    a = os.getcwd()
    filename = a + '\用户信息' + '.txt'
    return filename


def GET_FriendSTXT(filenmame):
    my_friend = bot.friends()
    with open(filenmame, 'w',encoding='utf-8') as f:
        f.write(my_friend.stats_text())
    print('ok')


def SEARCH_FRIENDS(name):
    my_friends = bot.friends()
    friends = my_friends.search(name)
    return friends[0]


def SEND_MESSAGES(friends, message):
    friends.send(message)

#获取好友信息分布
def func():
    path = CREATE_TXTPATH()
    GET_FriendSTXT(path)

#获取好友头像
def func1():
    path = CREATE_PICPATHT()
    IMAGE_SAVE(path)
    PJ_IMAGE(path)


#给好友发送信息
def func2():
    a = onclick()
    b = onclick1()
    a.send(b)
    print('发送成功')

#连续轰炸发送信息
def func3():
    for i in range(50):
        time.sleep(random.random() * 2)
        func2()


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


def func4():
    my_friend = bot.friends()
    b = onclick1()
    for i in my_friend[1:]:
        a = i.name
        friend = my_friend.search(a)[0]
        print('正在发送', friend)
        friend.send(b)  # 你想要发送的内容
        print('ok')
        time.sleep(1)


window.bind('<Return>', onclick)
click_button = tkinter.Button(window,
                              text='获取好友信息',
                              background='purple',
                              width=10,
                              height=4,
                              command=func)

click_button.pack(side='left')
click_button1 = tkinter.Button(window,
                               text='获取好友图片',
                               background='green',
                               width=10,
                               height=4,
                               command=func1)
click_button1.pack(side='right')
click_button2 = tkinter.Button(window,
                               text='点击发送信息',
                               background='blue',
                               width=10,
                               height=4,
                               command=func2)
click_button2.pack(side='top')
click_button3 = tkinter.Button(window,
                               text='连续发送五十',
                               background='pink',
                               width=10,
                               height=4,
                               command=func3)
click_button3.pack()
click_button4 = tkinter.Button(window,
                               text='群发信息',
                               background='grey',
                               width=10,
                               height=4,
                               command=func4)

click_button4.pack(side='bottom')
window.mainloop()
