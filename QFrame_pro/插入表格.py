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
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignCenter)
        ttf.setColumnWidthConstraints((QTextLength(1, 20), QTextLength(1, 30), QTextLength(1, 40), QTextLength(1, 50)))
        cursor = text_area.textCursor()
        cursor.insertTable(4, 3, ttf)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
