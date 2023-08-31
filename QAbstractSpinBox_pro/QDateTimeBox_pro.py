from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        dtb = QDateTimeEdit(self)
        dtb.lineEdit().setText('2010/1/1 0:00')
        dtb.setCalendarPopup(True)
        print(dtb.dateTime())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
