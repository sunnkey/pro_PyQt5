from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        short_cut_keys = QKeySequenceEdit(self)
        button = QPushButton('获取快捷键', self)
        button.move(20, 100)
        button.clicked.connect(lambda: print(self.findChild(QKeySequenceEdit).keySequence()))
        QKeySequence


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
