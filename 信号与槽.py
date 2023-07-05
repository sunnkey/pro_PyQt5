from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('test')
        self.resize(500, 500)
        self.move(400, 400)
        self.setup_ui()

    def setup_ui(self):
        self.make_btn()

    @staticmethod
    def slot_click_btn1(self):
        print('改变名字1')

    @staticmethod
    def slot_click_btn2(self):
        print('改变名字2')

    def make_btn(self):
        btn1 = QPushButton(self)
        btn1.setText('点击按钮')
        btn1.objectNameChanged.connect(self.slot_click_btn1)
        btn1.objectNameChanged.connect(self.slot_click_btn2)
        btn1.setObjectName('newName')
        print(btn1.receivers(btn1.objectNameChanged))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
