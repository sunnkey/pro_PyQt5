from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.line_copy = None
        self.line_edit = None
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('赋值文本框')
        self.setup_ui()

    def setup_ui(self):
        self.line_edit = QLineEdit(self)
        self.line_copy = QLineEdit(self)
        self.button = QPushButton('点击赋值', self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
