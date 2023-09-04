from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # 生成QFontDialog对象
        font = QFont()
        font.setFamily('宋体')
        font.setPointSize(20)
        font_dialog = QFontDialog(font, self)
        # 添加button
        button = QPushButton('编辑字体', self)
        button.setGeometry(50, 50, 80, 60)
        button.clicked.connect(lambda: font_dialog.open())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
