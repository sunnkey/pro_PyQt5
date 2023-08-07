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
        self.button = QPushButton(self)
        self.button.setText('Menu')
        self.button.setFlat(True)
        self.menu = QMenu()
        menu_lv2 = QMenu(self.menu)
        menu_lv2.setTitle('最近打开')
        action1 = QAction()
        action1.setText('新建')
        action1.triggered.connect(lambda: print('新建'))
        action2 = QAction()
        action2.setText('打开')
        action2.triggered.connect(lambda: print('打开'))
        action_recent_open = QAction('最近打开')
        menu_lv2.addAction(action_recent_open)
        self.menu.addAction(action1)
        self.menu.addSeparator()
        self.menu.addAction(action2)
        self.menu.addMenu(menu_lv2)
        self.button.setMenu(self.menu)
        print('1')  # 添加这行用于调试
        ######


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
