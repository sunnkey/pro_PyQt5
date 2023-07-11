from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


def my_cursor(path):
    mouse_map = QPixmap(path)
    mouse_map = mouse_map.scaled(50, 50)
    my_mouse = QCursor(mouse_map)
    return my_mouse


class MyWindow(QWidget):
    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        print(e.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    cursor = my_cursor('../source/images/add.png')
    window.setCursor(cursor)
    window.setMouseTracking(True)

    window.show()

    sys.exit(app.exec())
