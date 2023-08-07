from PyQt5.Qt import *
import sys


class MyMenu(QToolButton):
    def __init__(self, parent=None):
        super(MyMenu, self).__init__(parent)
        menu = QMenu(self)
        action1 = QAction(self)
        action1.setText('1')
        action2 = QAction()
        action2.setText('2')
        action3 = QAction()
        action3.setText('3')
        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)
        self.setMenu(menu)
        self.setText('Menu2')
        self.setPopupMode(QToolButton.MenuButtonPopup)
        self.clicked.connect(self.showMenu, Qt.QueuedConnection)  # Connect the clicked signal with QueuedConnection

    def showMenu(self):
        print("MyMenu clicked")  # Debug print statement
        self.menu().exec_(self.mapToGlobal(self.rect().bottomLeft()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    button = QToolButton(window)
    button2 = MyMenu(window)
    # -------------------------
    menu = QMenu()
    action1 = QAction()
    action1.setText('1')
    action2 = QAction()
    action2.setText('2')
    action3 = QAction()
    action3.setText('3')
    menu.addAction(action1)
    menu.addAction(action2)
    menu.addAction(action3)
    button.setMenu(menu)
    button.setText('Menu')
    button.setPopupMode(QToolButton.MenuButtonPopup)
    # -------------------------
    layout = QVBoxLayout()
    layout.addWidget(button)
    layout.addWidget(button2)
    window.setLayout(layout)  # Add the layout to the window
    window.show()
    sys.exit(app.exec())
