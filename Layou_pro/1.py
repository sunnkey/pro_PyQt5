from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        button1 = QPushButton('按钮1', self)
        button2 = QPushButton('按钮2', self)
        button3 = QPushButton('按钮3', self)

        layout.addWidget(button1, 1)
        layout.addWidget(button2, 2)
        layout.addWidget(button3, 3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
