# -------------------------
# 要求：
# 1、点击标签，标签变色
# 2、不使用自定义子类
# -------------------------
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.set_ui()
        self.all_children = self.children()  # 只获取EnhancedQLabel子类的控件
        self.count_green = len(self.all_children)
        self.count_red = 0

    def set_ui(self):
        for i in range(3):
            for j in range(3):
                label = EnhancedQLabel(self)
                label.setText(f'{i}----{j}')
                label.move(i * 120 + 30, j * 120 + 30)
                label.setStyleSheet('border: 1px solid black;background: green;')

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.childAt(e.x(), e.y()) is not None:
            self.updateChildColors(self.childAt(e.x(), e.y()))

    def updateChildColors(self, child):
        if child.tag == 0:
            child.setStyleSheet('background: red;')
            child.tag = 1
            self.count_green -= 1
            self.count_red += 1
        else:
            child.setStyleSheet('background: green;')
            child.tag = 0
            self.count_green += 1
            self.count_red -= 1


class EnhancedQLabel(QLabel):
    def __init__(self, parent=None):
        super(EnhancedQLabel, self).__init__(parent)
        self.tag = 0

    def changeTag(self):
        return self.tag ^ 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle('点击控件变色')
    window.resize(600, 600)
    window.move(500, 500)

    window.show()
    sys.exit(app.exec())
