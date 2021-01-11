#-*- coding:utf-8 _*- 
""" 
@file: gui2.py 
@time: 2021/01/06
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
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIcon,  QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #设置提示框字体
        QToolTip.setFont(QFont('SansSerif',10))

        #设置提示框内容
        self.setToolTip('test button demo')

        #设置button
        btn = QPushButton('click',self)
        # 重写提示框内容
        btn.setToolTip('This is a <b>QWidget</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,500)

        #程序退出按钮
        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(500,500)


        self.setGeometry(600,600,600,600)  #设置窗口屏幕坐标的x、y和窗口大小的宽、高
        self.setWindowTitle('GUI-Icon')
        self.setWindowIcon(QIcon('./1.jpeg')) #图标
        self.setAutoFillBackground(True)

        self.center() #调用窗口居中
        self.show()

    #添加退出确认
    def closeEvent(self,event):
        # 我们创建了一个消息框，上面有俩按钮：Yes和No.
        # 第一个字符串显示在消息框的标题栏，
        # 第二个字符串显示在对话框，
        # 第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的。
        # 返回值在变量reply里
        reply = QMessageBox.question(self,'Message','你确定要退出吗',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def center(self):
        #QDesktopWidget 提供了用户的桌面信息，包括屏幕大小
        qr = self.frameGeometry() #获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center() #获得显示器的分辨率，然后得到屏幕中间点的位置

        self.move(qr.topLeft()) #通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())