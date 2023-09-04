from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.origin_pos = None
        self.setup_ui()

    def setup_ui(self):
        # 生成checks对象
        for i in range(30):
            check_box = QCheckBox(self)
            check_box.setText(F'{i}')
            check_box.setGeometry(10 + i % 4 * 80, 10 + i // 4 * 50, 60, 30)
        # 生成QRubberRand对象
        rubber_band = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        super(Window, self).mouseMoveEvent(ev)
        rubber_band = self.findChild(QRubberBand)
        self.origin_pos = ev.pos()
        rubber_band.setGeometry(QRect(self.origin_pos, QSize()))
        rubber_band.show()

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        super(Window, self).mouseMoveEvent(ev)
        rubber_band = self.findChild(QRubberBand)
        rubber_band.setGeometry(QRect(self.origin_pos, ev.pos()).normalized())
        rubber_band_rect = rubber_band.geometry()
        for child in self.findChildren(QCheckBox):
            if rubber_band_rect.contains(child.geometry()):
                child.setStyleSheet('color: red;')
            else:
                child.setStyleSheet('color: black;')

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        super(Window, self).mouseMoveEvent(ev)
        rubber_band = self.findChild(QRubberBand)
        rubber_band_rect = rubber_band.geometry()
        for child in self.findChildren(QCheckBox):
            if rubber_band_rect.contains(child.geometry()):
                child.toggle()
        rubber_band.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
