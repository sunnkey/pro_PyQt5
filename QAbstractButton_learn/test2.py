from PyQt5.Qt import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    button = QPushButton(window)
    button.setText('Menu')
    menu = QMenu()
    action1 = QAction()
    action1.setText('新建')
    action2 = QAction()
    action2.setText('打开')
    menu.addAction(action1)
    menu.addAction(action2)

    button.setMenu(menu)

    window.show()
    sys.exit(app.exec())
