# -------------------------
# 创建一个窗口包含一个标签。
# 要求：1、鼠标进入标签时，展示“欢迎光临”
#      2、鼠标离开标签时，展示“谢谢惠顾”
# -------------------------
from PyQt5 import QtCore, QtGui
from PyQt5.Qt import *
import sys


class MyLabel(QLabel):
    def __init__(self, parent=None, text: dict = None):
        super(MyLabel, self).__init__(parent)
        self.enter_text = text.get('enter')
        self.leave_text = text.get('leave')

    def enterEvent(self, e: QtCore.QEvent) -> None:
        self.setText(self.enter_text or '')

    def leaveEvent(self, e: QtCore.QEvent) -> None:
        self.setText(self.leave_text or '')

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setText('...')


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('鼠标进入退出案例')
        self.resize(500, 500)
        self.set_ui()

    def set_ui(self):
        self.make_label()

    def make_label(self):
        label = MyLabel(self, {'enter': '欢迎光临', 'leave': '谢谢惠顾'})
        label.resize(100, 30)
        label.setText('...')
        label.setStyleSheet('border: 1px solid black;')
        label.move(200, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())
