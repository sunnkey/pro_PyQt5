from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self, colors):
        super(Window, self).__init__()
        self.sons = None
        self.setMaximumSize(1200, 1200)
        self.resize(900, 900)
        self.move(500, 500)
        self.colors = colors
        self.set_ui()

    def set_ui(self):
        self.sons = []
        for i in range(3):
            for j in range(3):
                color = self.colors[i * 3 + j]
                son = QWidget(self)
                son.resize(int(self.width() / 3), int(self.height() / 3))
                son.move(j * int(self.width() / 3), i * int(self.height() / 3))
                son.setStyleSheet(f'background-color:{color};')
                self.sons.append(son)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        for son in self.sons:
            son.resize(int(self.width() / 3), int(self.height() / 3))
        a0.accept()


if __name__ == '__main__':
    colors = ['cyan', 'red', 'blue', 'yellow', 'green', 'black', 'gold', 'snow', 'grey']
    app = QApplication(sys.argv)
    window = Window(colors)
    window.show()

    sys.exit(app.exec())
