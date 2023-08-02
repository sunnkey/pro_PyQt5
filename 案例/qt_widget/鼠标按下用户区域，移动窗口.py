from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.mouse_x = None
        self.mouse_y = None
        self.origin_x = None
        self.origin_y = None
        self.setWindowTitle('测试点击移动')
        self.resize(500, 500)
        self.move(500, 500)
        self.set_ui()

    def set_ui(self):
        pass

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.origin_x = self.x()
        self.origin_y = self.y()
        self.mouse_x = e.globalX()
        self.mouse_y = e.globalY()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        move_x = e.globalX() - self.mouse_x
        move_y = e.globalY() - self.mouse_y
        self.move(self.origin_x + move_x, self.origin_y + move_y)

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        print('鼠标释放了')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
