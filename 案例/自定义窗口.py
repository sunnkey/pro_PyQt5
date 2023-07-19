# -------------------------
# 要求：
# 1、无边框，无标题栏
# 2、窗口半透明那
# 3、自定义最大化，最小化，关闭按钮
# 4、支持拖拽用户区移动
# -------------------------
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


# class MyButton(QPushButton):
#     def __init__(self, parent=None, mode=1):
#         super(MyButton, self).__init__(parent)
#         self.mode = mode
#
#     def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
#         super(MyButton, self).mousePressEvent(e)
#         if self.mode == 1:
#             self.parent().showMinimized()
#         elif self.mode == 2:
#             self.parent().showMaximized()
# elif self.mode == 3:
#     self.parent().close()
# e.accept()


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.mouse_y = None
        self.mouse_x = None
        self.origin_y = None
        self.origin_x = None
        self.min_button = None
        self.max_normal_button = None
        self.close_button = None
        self.setWindowTitle('自定义窗口')
        self.resize(500, 500)
        self.move(400, 400)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setup_ui()

    def slot_max_normal_window(self):
        if self.isMaximized():
            print(1)
            self.max_normal_button.setText('最大化')
            self.showNormal()
        else:
            print(2)
            self.max_normal_button.setText('恢复')
            self.showMaximized()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.origin_x = self.x()
        self.origin_y = self.y()
        self.mouse_x = e.globalX()
        self.mouse_y = e.globalY()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        move_x = e.globalX() - self.mouse_x
        move_y = e.globalY() - self.mouse_y
        self.move(self.origin_x + move_x, self.origin_y + move_y)

    def setup_ui(self):
        self.min_button = QPushButton(self)
        self.min_button.setText('最小化')
        self.min_button.clicked.connect(self.showMinimized)

        self.max_normal_button = QPushButton(self)
        self.max_normal_button.setText('最大化')
        self.max_normal_button.move(120, 0)
        self.max_normal_button.clicked.connect(self.slot_max_normal_window)

        self.close_button = QPushButton(self)
        self.close_button.setText('关闭')
        self.close_button.move(240, 0)
        self.close_button.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
