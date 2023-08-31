from PyQt5.Qt import *
import sys


class MySpinBox(QSpinBox):
    def textFromValue(self, v: int) -> str:
        return f'第 {str(v)} 月'


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.spin_box = MySpinBox(self)
        self.setup_ui()

    def setup_ui(self):
        self.spin_box.setWrapping(True)
        self.spin_box.setPrefix('第 ')
        self.spin_box.setSuffix(' 周')
        self.spin_box.setSpecialValueText('First week')
        self.spin_box.valueChanged.connect(lambda: print(self.spin_box.cleanText()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
