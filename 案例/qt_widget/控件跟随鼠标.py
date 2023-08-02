# -------------------------
# 鼠标进入窗体的控件后，控件跟随鼠标移动，且鼠标变换形状
# -------------------------
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('')
        self.resize(500, 500)
        self.move(400, 400)
        self.setMouseTracking(True)
        self.label = None
        self.mouse_picture_path = '../../source/images/add.png'
        self.cursor = self.my_cursor(self.mouse_picture_path)
        self.setCursor(self.cursor)
        self.setup_ui()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        self.label.move(e.x(), e.y())

    def my_cursor(self, path):
        cursor_map = QPixmap(path).scaled(45, 45)
        my_cursor = QCursor(cursor_map)
        return my_cursor

    def setup_ui(self):
        label = QLabel(self)
        label.setText('我是需要跟踪鼠标的控件')
        label.move(100, 100)
        self.label = label


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())
