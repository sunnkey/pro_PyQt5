from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        for i in range(5):
            label = QLabel(f'Label_{i}', self)
            layout.addWidget(label)


if __name__ == '__main__':
    with open('QSS/test.qss', 'r') as f:
        content = f.read()
        print(content)
        app = QApplication(sys.argv)
        app.setStyleSheet(content)  # 修改此处
        window = Window()
        window.show()
    sys.exit(app.exec())
