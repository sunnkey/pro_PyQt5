from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button_female = None
        self.button_male = None
        self.setWindowTitle('')
        self.resize(500, 500)
        self.move(400, 400)
        self.setup_ui()

    def setup_ui(self):
        self.button_male = QRadioButton('男', self)
        self.button_male.setIcon(QIcon('../source/images/add.png'))
        self.button_male.setChecked(True)
        self.button_male.setShortcut('Alt+m')
        self.button_female = QRadioButton('女', self)
        self.button_female.move(0, 50)
        self.button_female.setShortcut('Alt+f')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
