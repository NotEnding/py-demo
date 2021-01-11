# -*- coding:utf-8 _*-
""" 
@file: layout3.py 
@time: 2021/01/07
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
利用QGridLayout 类创建一个网格布局
'''

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #创建一个网格按钮
        grid = QGridLayout()
        self.setLayout(grid)

        # 按钮的标签
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position,name in zip(positions,names):

            if name == "":
                continue
            #绑定按钮名称
            button = QPushButton(name)
            #添加到布局中
            grid.addWidget(button,*position)


        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
