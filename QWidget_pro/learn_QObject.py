from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('QT学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.test_q_object()

    @staticmethod
    def test_q_object():
        # mros = QObject.mro()
        # for mro in mros:
        #     print(mro)
        obj = QObject()
        obj.setObjectName('sun')
        print(obj.objectName())
        obj.setProperty('name', 'liu')
        obj.setProperty('age', 20)
        print(obj.property('age'))
        print(obj.property('name'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())
