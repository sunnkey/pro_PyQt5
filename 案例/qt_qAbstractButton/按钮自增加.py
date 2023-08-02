from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('按钮增加数字')
        self.resize(500, 500)
        self.move(400, 400)
        self.button = QPushButton(self)
        self.count = 0
        self.setup_ui()

    def setup_ui(self):
        button_icon = QIcon('../../source/images/add.png')
        self.button.setText(f'{self.count}')
        self.button.setIcon(button_icon)
        self.button.setIconSize(QSize(100, 100))
        self.button.setShortcut('Alt+b')
        self.button.setAutoRepeat(True)
        self.button.setAutoRepeatInterval(500)
        self.button.setAutoRepeatDelay(1000)
        # self.shortcut = QShortcut(QKeySequence('Alt+b'), self)
        # self.shortcut.activated.connect(self.add_num)
        self.button.clicked.connect(self.add_num)

    def add_num(self):
        self.count += 1
        self.button.setText(str(self.count))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
