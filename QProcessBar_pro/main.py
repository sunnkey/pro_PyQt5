import time

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # 添加进度条和按钮
        progress_bar = QProgressBar(self)
        progress_bar.setGeometry(50, 50, 200, 30)
        progress_bar.setRange(0, 100)
        progress_bar.setValue(50)
        button = QPushButton('Start', self)

        # 添加信号和槽
        button.clicked.connect(self.slot_progress_start)

    def slot_progress_start(self):
        progress_bar = self.findChild(QProgressBar)
        progress_bar.reset()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
