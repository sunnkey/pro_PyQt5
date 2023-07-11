from PyQt5.Qt import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setCursor(Qt.ClosedHandCursor)
    window.show()

    sys.exit(app.exec())