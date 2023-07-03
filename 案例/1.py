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
        label1 = QLabel(self)
        label1.setText('第一个label')
        label2 = QLabel(self)
        label2.setText('第二个label')
        label2.move(100, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())
