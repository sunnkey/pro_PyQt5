from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('QT学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.test_QObject()

    def test_q_object(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())
