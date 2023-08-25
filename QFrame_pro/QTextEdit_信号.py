from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('QTextEdit信号')
        self.setup_ui()

    def setup_ui(self):
        text_area = QTextEdit(self)
        button = QPushButton('show', self)
        button.move(20, 300)
        text_area.mousePressEvent = self.show_info
        text_area.insertHtml('*' * 200 + '''<a href='https://www.baidu.com'>转到网址</a>''')
        plain_text_area = QPlainTextEdit(self)

    def show_info(self, e):
        print(e.pos())
        print(self)
        url = self.findChild(QTextEdit).anchorAt(e.pos())
        QDesktopServices.openUrl(QUrl(url))
        super().mousePressEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
