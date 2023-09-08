from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        lcd1 = QLCDNumber(5, self)
        lcd1.setGeometry(50, 50, 200, 80)
        lcd1.display('100')
        lcd2 = QLCDNumber(5, self)
        lcd2.setGeometry(50, 150, 200, 80)
        lcd2.display('100')
        lcd3 = QLCDNumber(5, self)
        lcd3.setGeometry(50, 250, 200, 80)
        lcd3.display('100')
        lcd1.setSegmentStyle(QLCDNumber.Outline)
        lcd2.setSegmentStyle(QLCDNumber.Filled)
        lcd3.setSegmentStyle(QLCDNumber.Flat)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
