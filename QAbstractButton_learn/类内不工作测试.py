from PyQt5.QtWidgets import QApplication, QToolButton, QMenu, QAction, QVBoxLayout, QWidget
import sys


class CustomMenuButton(QToolButton):
    def __init__(self, parent=None):
        super(CustomMenuButton, self).__init__(parent)
        self.setText('Menu')
        self.setPopupMode(QToolButton.MenuButtonPopup)

        menu = QMenu(self)
        action1 = QAction('Option 1', self)
        action2 = QAction('Option 2', self)
        action3 = QAction('Option 3', self)
        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)

        self.setMenu(menu)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout()

    custom_button = CustomMenuButton(window)
    layout.addWidget(custom_button)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
