# -------------------------
# 创建一个窗口，添加两个文本按钮，要求：
# 1、一个账号，一个密码
# 2、点击登录按钮，获取账号和密码信息
# 3、对账号和密码进行验证，正确账号sz，密码sun
# 4、如果账号错误，清空账号框，如果密码错误，则清空密码框
# -------------------------

from PyQt5.Qt import *
import sys


class CheckAccount:
    ACCOUNT_ERROR = 1
    PWD_ERROR = 2
    ALL_ERROR = 3
    SUCCESS = 4

    @classmethod
    def check_login(self, account, pwd):
        if account == 'sz' and pwd == 'sun':
            return self.SUCCESS
        if account == 'sz' and pwd != 'sun':
            return self.PWD_ERROR
        if account != 'sz' and pwd == 'sun':
            return self.ACCOUNT_ERROR
        if account != 'sz' and pwd != 'sun':
            return self.ALL_ERROR


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.message = None
        self.result = None
        self.button_submit = None
        self.line_password = None
        self.line_username = None
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('提交密码')
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        info = QLabel('sz, sun')
        self.line_username = QLineEdit(self)
        self.line_username.setPlaceholderText('用户名')
        self.line_username.setClearButtonEnabled(True)
        self.line_password = QLineEdit(self)
        self.line_password.setPlaceholderText('密码')
        self.button_submit = QPushButton('Submit', self)
        self.button_submit.clicked.connect(self.slot_submit)
        self.result = QLabel('wait', self)

        layout.addWidget(info)
        layout.addWidget(self.line_username)
        layout.addWidget(self.line_password)
        layout.addWidget(self.button_submit)
        layout.addWidget(self.result)
        self.setLayout(layout)

    def slot_submit(self):
        username = self.line_username.text()
        password = self.line_password.text()
        result = CheckAccount.check_login(username, password)
        print(result)
        if result == CheckAccount.SUCCESS:
            self.result.setText('ok')
        if result == 2:
            self.line_password.setText('')
            self.result.setText('Password error!')
        if result == 1:
            self.line_username.setText('')
            self.result.setText('Username error!')
        if result == 3:
            self.line_password.setText('')
            self.line_username.setText('')
            self.result.setText('All error!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    print(CheckAccount.check_login('sz', 'sun'))
    sys.exit(app.exec())
