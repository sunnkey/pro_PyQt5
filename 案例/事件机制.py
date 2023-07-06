from PyQt5 import QtCore
from PyQt5.Qt import *
import sys


class APP(QApplication):
    def __init__(self, argv):
        super(APP, self).__init__(argv)

    def notify(self, receiver: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if receiver.inherits('QPushButton') and event.type() == QEvent.MouseButtonPress:
            print(receiver, event)
        return super().notify(receiver, event)


app = APP(sys.argv)
window = QWidget()
window.resize(800, 600)
window.move(1200, 960)

btn_test = QPushButton(window)
btn_test.setText('测试按钮')

window.show()
sys.exit(app.exec())
