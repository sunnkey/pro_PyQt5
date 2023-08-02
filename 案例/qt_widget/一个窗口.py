# -------------------------
# 要求：
# 1、标签默认隐藏，文本框和按钮显示，按钮设置为不可用状态
# 2、党文本框有内容时，让按钮可以用，否则不可用
# 3、当文本框内容为Sz时，点击按钮则显示标签，并展示文本为登录成功，否则为失败
# -------------------------

from PyQt5.Qt import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # 定义标签、文本框、按钮
        self.button = None
        self.text_box = None
        self.label = None
        # 初始化窗口
        self.setWindowTitle('一个窗口')
        self.resize(500, 500)
        self.move(400, 400)
        # 装在状态栏
        self.statusBar()
        # 装载其他控件
        self.setup_ui()

    def setup_ui(self):
        # 生成标签
        self.label = QLabel(self)
        self.label.setVisible(False)
        self.label.setText('登录成功')
        self.label.move(50, 150)
        # self.label.resize(200, 100)
        # 生成文本框
        self.text_box = QLineEdit(self)
        self.text_box.move(50, 50)
        self.text_box.textChanged.connect(self.slot_text_change)
        # 生成按钮
        self.button = QPushButton(self)
        self.button.setText('显示标签')
        self.button.setEnabled(False)
        self.button.move(50, 100)
        self.button.setToolTip('我是按钮')
        # self.button.setToolTipDuration(500)
        self.button.clicked.connect(self.slot_button_clicked)

    def slot_text_change(self):
        if self.text_box.text():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

    def slot_button_clicked(self):
        print(1)
        if self.text_box.text() == 'Sz':
            self.label.setVisible(True)
            self.label.setText('登录成功')
        else:
            self.label.setVisible(True)
            self.label.setText('登录失败')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
