# -------------------------
# 创建一个窗口，添加两个文本按钮，要求：
# 1、一个账号，一个密码
# 2、点击登录按钮，获取账号和密码信息
# 3、对账号和密码进行验证，正确账号sz，密码sun
# 4、如果账号错误，清空账号框，如果密码错误，则清空密码框
# -------------------------

from PyQt5.Qt import *
import sys
import typing


class UserLoginQValidator(QValidator):
    def validate(self, text: str, pos: int) -> typing.Tuple['QValidator.State', str, int]:
        # return QValidator.Acceptable, text, pos
        if 3 <= len(text) <= 8 or len(text) == 0:
            print('合格长度')
            return QValidator.Acceptable, text, pos
        elif len(text) < 3:
            print('长度不够，可以更改')
            return QValidator.Intermediate, text, pos
        else:
            print('长度超出')
            return QValidator.Invalid, text, pos

    def fixup(self, text: str) -> str:
        return text.ljust(3, '-')


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
        # 用户名控件
        self.line_username = QLineEdit(self)
        self.line_username.setPlaceholderText('用户名')
        self.line_username.setClearButtonEnabled(True)
        # 添加自动完成器
        completer = QCompleter(['sun', 'sun2', 'han'], self.line_username)
        self.line_username.setCompleter(completer)
        # 添加用户验证器
        # validator = UserLoginQValidator()
        validator = QIntValidator(10, 888)
        self.line_username.setValidator(validator)
        # 密码控件
        self.line_password = QLineEdit(self)
        self.line_password.setPlaceholderText('密码')
        self.line_password.setClearButtonEnabled(True)
        self.line_password.setEchoMode(2)
        toggle_action = QAction(self.line_password)
        self.line_password.addAction(toggle_action, 1)
        toggle_action.setIcon(QIcon('../../source/images/show.png'))
        toggle_action.triggered.connect(self.slot_toggle_show)
        # 提交按钮控件
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

    def slot_toggle_show(self):
        sender = self.sender()
        state = sender.parent().echoMode()
        if state == 0:
            sender.setIcon(QIcon('../../source/images/show.png'))
            sender.parent().setEchoMode(2)
        if state == 2:
            sender.setIcon(QIcon('../../source/images/no_show.png'))
            sender.parent().setEchoMode(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
