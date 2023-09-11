import functools
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
        progress_bar.setValue(0)
        # progress_bar.setFormat('当前%v/总计%m')
        progress_bar.setFormat('当前/总计%v%')
        progress_bar.setAlignment(Qt.AlignVCenter)
        # progress_bar.setOrientation(Qt.Vertical)
        # progress_bar.setTextVisible(True)
        # progress_bar.setTextDirection(QProgressBar.TopToBottom)
        button = QPushButton('Start', self)

        # 生成一个QTimer对象
        timer = QTimer(self)

        # 添加信号和槽
        button.clicked.connect(functools.partial(self.slot_progress_start, timer))

    def slot_time_out(self, timer):
        progress_bar = self.findChild(QProgressBar)
        if progress_bar.value() > 100:
            timer.stop()
        progress_bar.setValue(progress_bar.value() + 1)

    def slot_progress_start(self, timer):
        progress_bar = self.findChild(QProgressBar)
        progress_bar.reset()
        timer.timeout.connect(functools.partial(self.slot_time_out, timer))
        timer.start(10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
