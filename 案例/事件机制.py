from PyQt5 import QtCore, QtGui
from PyQt5.Qt import *
import sys


class APP(QApplication):
    def __init__(self, argv):
        super(APP, self).__init__(argv)

    def notify(self, r: QtCore.QObject, e: QtCore.QEvent) -> bool:
        if r.inherits('QPushButton') and e.type() == QEvent.MouseButtonDblClick:
            print(e.type())
        return super().notify(r, e)


class BTN(QPushButton):
    def event(self, e: QtCore.QEvent) -> bool:
        if e.type() == QEvent.MouseButtonPress:
            print(e.type())
        return super().event(e)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        print('鼠标被点击了')


app = APP(sys.argv)
window = QWidget()
window.resize(800, 600)
window.move(1200, 960)

btn_test = BTN(window)
btn_test.setText('测试按钮')

window.show()
sys.exit(app.exec())
