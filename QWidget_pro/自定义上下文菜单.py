from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('')
        self.resize(500, 500)
        self.move(400, 400)
        self.setup_ui()

    def contextMenuEvent(self, e: QtGui.QContextMenuEvent) -> None:
        print('类方法点击右键菜单')
        menu = QMenu(self)
        menu_lv2 = QMenu(menu)
        menu_lv2.setTitle('最近打开')
        action1 = QAction()
        action1.setText('新建')
        action1.triggered.connect(lambda: print('新建'))
        action2 = QAction()
        action2.setText('打开')
        action2.triggered.connect(lambda: print('打开'))
        action_recent_open = QAction('最近打开')
        menu_lv2.addAction(action_recent_open)
        menu.addAction(action1)
        menu.addSeparator()
        menu.addAction(action2)
        menu.addMenu(menu_lv2)
        menu.exec(e.globalPos())

    def setup_ui(self):
        pass


def right_click_show(point):
    print('信号点击右键菜单', point)
    menu = QMenu(window)
    menu_lv2 = QMenu(menu)
    menu_lv2.setTitle('最近打开')
    action1 = QAction()
    action1.setText('新建')
    action1.triggered.connect(lambda: print('新建'))
    action2 = QAction()
    action2.setText('打开')
    action2.triggered.connect(lambda: print('打开'))
    action_recent_open = QAction('最近打开')
    menu_lv2.addAction(action_recent_open)
    menu.addAction(action1)
    menu.addSeparator()
    menu.addAction(action2)
    menu.addMenu(menu_lv2)
    dest_point = window.mapToGlobal(point)
    menu.exec(dest_point)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    # window.setContextMenuPolicy(Qt.CustomContextMenu)
    # window.customContextMenuRequested.connect(right_click_show)
    window.show()
    sys.exit(app.exec())
