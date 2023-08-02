# 要求
# 字体25px，颜色灰色，边框圆角8px
# 信息提示级别：正常-绿边框，绿色字，警告-黄边框，黄色字，错误-红边框，红色字

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('QT学习')
        self.resize(500, 500)
        self.move(400, 400)
        self.setup_ui()

    def setup_ui(self):
        self.test_q_object()

    def test_q_object(self):
        with open('../../object.qss') as f:
            qApp.setStyleSheet(f.read())
        label1 = QLabel(self)
        label1.setText('第一个label')
        label1.setObjectName('notice')
        label1.setProperty('leave', 'normal')

        label2 = QLabel(self)
        label2.setText('第二个label')
        label2.move(150, 0)
        label2.setObjectName('notice')
        label2.setProperty('leave', 'waring')

        label3 = QLabel(self)
        label3.setText('第三个label')
        label3.move(300, 0)
        label3.setObjectName('notice')
        label3.setProperty('leave', 'error')

        btn1 = QPushButton(self)
        btn1.move(0, 50)
        btn1.setText('我是按钮1')
        btn1.setObjectName('waring')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window1 = Window()
    window1.resize(1200, 1200)
    window2 = Window()
    window2.resize(800, 800)
    window2.setParent(window1)

    window1.show()
    window2.show()

    sys.exit(app.exec())
