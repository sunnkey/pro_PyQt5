from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('')
        self.resize(500, 500)
        self.move(400, 400)
        self.setup_ui()

    def setup_ui(self):
        button = QPushButton(self)
        button.setText('1111')
        print(button.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
