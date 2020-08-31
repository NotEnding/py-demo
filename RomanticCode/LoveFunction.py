#-*- coding:utf-8 _*- 
""" 
@file: LoveFunction.py 
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
import numpy as np
import time
import matplotlib.pyplot as plt


def plot_love(numbers):
    plt.clf()
    for k in range(numbers):
        time.sleep(0.05)

        def f(x, love=50):
            y = x ** (2 / 3) + 0.9 * np.sqrt(3.3 - x ** 2) * np.sin(love * np.pi * x)
            return y

        x = np.linspace(0, 2, 1500)
        y = [f(i, k) for i in x]

        plt.plot(x, y, color='red', linewidth=5)
        plt.plot(-x, y, color='red', linewidth=5)
        plt.xlim(-2, 2)


        plt.show()


plot_love(100)
