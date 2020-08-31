#-*- coding:utf-8 _*- 
""" 
@file: LoveTree.py 
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

import turtle
import random

turtle.bgcolor('peachpuff')
turtle.bgpic(r"./yourname.gif")

#在(x,y)处画爱心
def love(x,y):
    lv=turtle.Turtle()

    lv.hideturtle()

    lv.up()

    # 定位到(x,y)
    lv.goto(x,y)

    # 画圆弧
    def curvemove():
        for i in range(20):
            lv.right(10)
            lv.forward(2)
    lv.color('red','pink')

    lv.speed(10000000)

    lv.pensize(1)

    #开始画爱心

    lv.down()

    lv.begin_fill()

    lv.left(140)

    lv.forward(22)

    curvemove()

    lv.left(120)

    curvemove()

    lv.forward(22)

    lv.write("小仙女",font=("Arial",12,"normal"),align="center")

    lv.left(140)#画完复位

    lv.end_fill()

def tree(branchLen,t):
    if branchLen > 5:#剩余树枝太少要结束递归
        if branchLen<20:

            t.color("green")

            t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))

            t.down()

            t.forward(branchLen)

            love(t.xcor(),t.ycor())#传输现在turtle的坐标

            t.up()

            t.backward(branchLen)
            t.color("brown")

            return

        t.pensize(random.uniform((branchLen + 5) / 4 - 2, (branchLen + 6) / 4 + 5))

        t.down()

        t.forward(branchLen)

        # 以下递归

        ang = random.uniform(15, 45)

        t.right(ang)

        tree(branchLen - random.uniform(12, 16), t)  # 随机决定减小长度

        t.left(2 * ang)

        tree(branchLen - random.uniform(12, 16), t)  # 随机决定减小长度

        t.right(ang)

        t.up()

        t.backward(branchLen)


myWin = turtle.Screen()

t = turtle.Turtle()

t.hideturtle()

t.speed(10000)

t.left(90)

t.up()

t.backward(200)

t.down()

t.color("brown")

t.pensize(32)

t.forward(60)

tree(100, t)

myWin.exitonclick()

