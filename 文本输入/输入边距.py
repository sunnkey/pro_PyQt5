from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        line_edit = QLineEdit(self)
        line_edit.resize(200, 200)
        line_edit.setTextMargins(30, 30, 30, 30)
        line_edit.setAlignment(Qt.AlignTop)
        print(line_edit.getTextMargins())
        print(line_edit.alignment())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
