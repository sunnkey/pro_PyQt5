# -------------------------
# 1、实现滑块
# 2、滑块内部显示数值，拖动时显示，停止时隐藏
# 3、数值处于滑块中间位置
# -------------------------
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Slider(QSlider):
    def __init__(self, parent=None):
        super(Slider, self).__init__(parent)
        self.setTickPosition(QSlider.TicksBothSides)
        self.label = QLabel(self)
        self.label.setText('0\n0')
        self.label.setStyleSheet('border:1px solid red;')

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        super(Slider, self).mousePressEvent(ev)
        print(self.width(), self.label.width())


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        slider = Slider(self)
        slider.setGeometry(100, 100, 60, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
