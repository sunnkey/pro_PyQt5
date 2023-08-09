from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = None
        self.line_copy = None
        self.line_edit = None
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('赋值文本框')
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.line_edit = QLineEdit(self)
        self.line_copy = QLineEdit(self)
        self.line_copy.setEnabled(False)
        self.button = QPushButton('复制', self)
        self.button.clicked.connect(self.ButtonClicked)
        for son in self.children():
            if isinstance(son, QWidget):
                print(son)
                layout.addWidget(son)
        self.setLayout(layout)

    def ButtonClicked(self):
        text = self.line_edit.text()
        self.line_copy.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
