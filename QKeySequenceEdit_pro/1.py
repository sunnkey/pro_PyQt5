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
        keys1 = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_V)
        keys2 = QKeySequence().Cut
        keys3 = QKeySequence().Save
        short_cut_keys.setKeySequence(keys3)

        button = QPushButton('获取快捷键', self)
        button.move(20, 100)
        button.clicked.connect(lambda: print(self.findChild(QKeySequenceEdit).keySequence().toString()))
        short_cut_keys.editingFinished.connect(lambda: print(0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
