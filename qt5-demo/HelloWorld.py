#-*- coding:utf-8 _*- 
""" 
@file: HelloWorld.py 
@time: 2021/01/05
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
import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(300,200)
    w.move(400,400)
    w.setWindowTitle('HelloWorld')
    w.show()

    sys.exit(app.exec_())
