from PyQt5.Qt import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    button = QPushButton(window)
    button.setText('Menu')
    button.setFlat(True)
    menu = QMenu()
    menu_lv2 = QMenu(menu)
    menu_lv2.setTitle('最近打开')
    action_new = QAction()
    action_new.setText('新建')
    action_new.triggered.connect(lambda: print('新建'))
    action_open = QAction()
    action_open.setText('打开')
    action_open.triggered.connect(lambda: print('打开'))
    action_recent_open = QAction('最近打开')
    menu_lv2.addAction(action_recent_open)
    menu.addAction(action_new)
    menu.addSeparator()
    menu.addAction(action_open)
    menu.addMenu(menu_lv2)
    button.setMenu(menu)

    # -------------------------
    tool_button_up_arrow = QToolButton(window)
    tool_button_up_arrow.move(100, 0)
    menu2 = QMenu()
    action1 = QAction()
    action1.setText('1')
    action2 = QAction()
    action2.setText('2')
    action3 = QAction()
    action3.setText('3')
    menu2.addAction(action1)
    menu2.addAction(action2)
    menu2.addAction(action3)
    tool_button_up_arrow.setMenu(menu2)
    tool_button_up_arrow.setText('Menu')
    tool_button_up_arrow.setPopupMode(QToolButton.MenuButtonPopup)
    # -------------------------

    window.show()
    sys.exit(app.exec())