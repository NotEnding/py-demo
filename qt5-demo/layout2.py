#-*- coding:utf-8 _*- 
""" 
@file: layout2.py 
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

"""
pyqt5 的布局管理-----绝对定位
绝对定位有以下限制:
如果我们调整窗口，控件的大小和位置不会改变
在各种平台上应用程序看起来会不一样
如果改变字体，我们的应用程序的布局就会改变
如果我们决定改变我们的布局,我们必须完全重做我们的布局
"""

'''
使用QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局。
'''

import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #设立2个按钮
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        #使用QHBoxLayout和QVBoxLayout，来分别创建横向布局和纵向布局。
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        #添加一个垂直布局
        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






