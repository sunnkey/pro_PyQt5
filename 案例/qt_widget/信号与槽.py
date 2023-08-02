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
        self.fun_title()

    def make_btn(self):
        btn1 = QPushButton(self)
        btn1.setText('点击按钮')
        btn1.objectNameChanged.connect(self.slot_btn_change_name)
        btn1.clicked.connect(self.slot_btn_click)
        btn1.setObjectName('newName')

    def fun_title(self):
        self.windowTitleChanged.connect(self.slot_window_title_change)

    def slot_btn_change_name(self):
        print('改变名字')

    def slot_btn_click(self):
        print('被点击了')

    def slot_window_title_change(self):
        self.blockSignals(True)  # 阻止信号传递
        new_title = 'sun' + self.windowTitle()
        # print(new_title)
        self.setWindowTitle(new_title)
        self.blockSignals(False)  # 恢复信号传递


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.setWindowTitle('11')
    win.setWindowTitle('121')
    win.show()
    sys.exit(app.exec())