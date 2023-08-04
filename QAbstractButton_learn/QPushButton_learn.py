from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.menu = None
        self.button = None
        self.setWindowTitle('QPushButton')
        self.resize(500, 500)
        self.move(400, 400)
        ######
        ######
        self.setup_ui()

    def setup_ui(self):
        self.button = QPushButton(self)
        self.button.setText('Menu')
        self.button.setStyleSheet('QPushButton:pressed {background-color:red}')

        # 创建menu对象
        self.menu = QMenu()
        # 创建action对象
        action1 = QAction()
        action2 = QAction()
        action1.setText('新建')
        action2.setText('打开')
        action1.setIcon(QIcon('../source/images/add.png'))
        # 将action对象添加到menu对象中
        self.menu.addAction(action1)
        self.menu.addAction(action2)

        # 将menu添加到button中
        self.button.setMenu(self.menu)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
