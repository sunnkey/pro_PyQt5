from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('窗口事件')
        self.resize(500, 500)
        self.move(1400, 600)
        self.setup_ui()

    def closeEvent(self, e: QtGui.QCloseEvent) -> None:
        print('窗口被关闭了')

    def showEvent(self, e: QtGui.QShowEvent) -> None:
        print('窗口被打开了')

    def moveEvent(self, e: QtGui.QMoveEvent) -> None:
        print(e.pos())

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
