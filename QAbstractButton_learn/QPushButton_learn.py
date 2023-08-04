from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = None
        self.setWindowTitle('QPushButton')
        self.resize(500, 500)
        self.move(400, 400)
        self.setup_ui()

    def setup_ui(self):
        self.button = QPushButton(self)
        self.button.setText('click')
        # button.setStyleSheet('QPushButton:pressed {background-color:red}')
        # button.setCheckable(True)

        # 创建menu对象
        menu = QMenu()
        # 创建action对象
        action = QAction()
        action.setText('新建')
        action.setIcon(QIcon('../source/images/add.png'))
        # 将action对象添加到menu对象中
        menu.addAction(action)
        # 将menu添加到button中
        self.button.setMenu(menu)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
