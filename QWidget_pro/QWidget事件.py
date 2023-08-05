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

    # def moveEvent(self, e: QtGui.QMoveEvent) -> None:
    #     print(e.pos())

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        print(e.key())

    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        print('获取焦点')
        print(e.gotFocus())

    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:
        print('失去焦点')

    def setup_ui(self):
        label = QLabel(self)
        label.setText('焦点获取')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
