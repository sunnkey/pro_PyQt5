from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class MyQLabel(QLabel):
    def __init__(self, parent=None, mode=1):
        super(MyQLabel, self).__init__(parent)
        self.parent = parent
        self.mode = mode

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.mode == 1:
            self.parent.setWindowState(Qt.WindowMinimized)
        elif self.mode == 2:
            self.parent.setWindowState(Qt.WindowMaximized)
        elif self.mode == 3:
            self.parent.setWindowState(Qt.WindowFullScreen)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('')
        self.resize(500, 500)
        self.move(400, 400)
        self.setup_ui()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    label1 = MyQLabel(window, 1)
    label1.setText('最小化')
    label2 = MyQLabel(window, 2)
    label2.setText('最大化')
    label2.move(100, 0)
    label3 = MyQLabel(window, 3)
    label3.setText('全屏')
    label3.move(200, 0)
    window.show()
    sys.exit(app.exec())
