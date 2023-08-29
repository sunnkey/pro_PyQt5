from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.spin_box = QSpinBox(self)
        self.setup_ui()

    def setup_ui(self):
        self.spin_box.setWrapping(True)
        self.spin_box.setPrefix('第 ')
        self.spin_box.setSuffix(' 周')
        self.spin_box.setSpecialValueText('First week')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
