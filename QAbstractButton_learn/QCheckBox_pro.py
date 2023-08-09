from PyQt5.Qt import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.button_group_chooses = None
        self.button_all = None
        self.buttons = None
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('复选框')
        self.initUi()

    def initUi(self):
        layout = QVBoxLayout()
        buttons_name = ['button1', 'button2', 'button3']
        self.button_all = QCheckBox('全选', self)
        layout.addWidget(self.button_all)
        self.buttons = {}
        for index, name in enumerate(buttons_name):
            button = QCheckBox(name, self)
            button.toggled.connect(self.SingleClicked)
            self.buttons[name] = button
            layout.addWidget(button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.button_all.clicked.connect(self.AllClicked)

    def AllClicked(self, c):
        for btn in self.buttons.values():
            btn.setCheckState(2 if c else 0)

    def SingleClicked(self):
        all_checked = all(btn.isChecked() for btn in self.buttons.values())
        any_checked = any(btn.isChecked() for btn in self.buttons.values())
        if all_checked:
            self.button_all.setCheckState(2)
        elif any_checked:
            self.button_all.setCheckState(1)
        else:
            self.button_all.setCheckState(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
