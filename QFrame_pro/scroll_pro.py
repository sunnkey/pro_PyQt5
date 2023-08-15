from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('滚动条功能测试')
        self.setup_ui()

    def setup_ui(self):
        text_area = QTextEdit(self)
        text_area.setGeometry(50, 50, 200, 200)

        horizontal_scrollbar = QScrollBar(self)
        text_area.setHorizontalScrollBar(horizontal_scrollbar)
        text_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        text_area.setLineWrapMode(QTextEdit.NoWrap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
