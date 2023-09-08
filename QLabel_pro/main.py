from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # label
        label_user = QLabel('User(&u)', self)
        label_user.setGeometry(50, 50, 120, 40)
        label_password = QLabel('Password(&p)', self)
        label_password.setGeometry(50, 100, 120, 40)
        line_edit_user = QLineEdit(self)
        line_edit_user.setPlaceholderText('请输入用户名')
        line_edit_user.setGeometry(180, 50, 160, 40)
        line_edit_user.setFrame(False)
        line_edit_password = QLineEdit(self)
        line_edit_password.setPlaceholderText('请输入密码')
        line_edit_password.setGeometry(180, 100, 160, 40)
        line_edit_password.setFrame(False)
        label_user.setBuddy(line_edit_user)
        label_password.setBuddy(line_edit_password)
        label_href = QLabel('''<a href='https://www.baidu.com'>百度</a>''', self)
        label_href.setOpenExternalLinks(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
