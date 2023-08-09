# -------------------------
# 创建一个窗口，添加两个文本按钮，要求：
# 1、一个账号，一个密码
# 2、点击登录按钮，获取账号和密码信息
# 3、对账号和密码进行验证，正确账号sz，密码sun
# 4、如果账号错误，清空账号框，如果密码错误，则清空密码框
# -------------------------

from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
