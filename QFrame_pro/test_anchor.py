from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        text_area = QTextEdit(self)
        text_area.setHtml('*' * 200 + '''<a name='anchor_1' href='#'>这是内容</a>''' + '+' * 200)

        button = QPushButton('转到锚点', self)
        button.move(20, 300)
        button.clicked.connect(self.to_anchor_1)

    def to_anchor_1(self):
        text_area = self.findChild(QTextEdit)
        text_area.scrollToAnchor('anchor_1')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
