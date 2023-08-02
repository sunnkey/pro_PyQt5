from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('监控用户输入组合键')
        self.resize(500, 500)
        self.move(500, 500)
        self.set_ui()

    def set_ui(self):
        pass

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == Qt.Key_NumLock:
            print('ok!')
        if e.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and e.key() == Qt.Key_S:
            print('按下了ctrl+shift+s')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
