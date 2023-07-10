from PyQt5.Qt import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(800, 800)
    red_window = QWidget(window)
    red_window.resize(100, 100)
    red_window.move(0, 400)
    red_window.setStyleSheet('background:red')
    green_window = QWidget(window)
    green_window.resize(100, 100)
    green_window.move(300, 0)
    green_window.setStyleSheet('background-color: green')

    window.show()
    # window.adjustSize()
    sys.exit(app.exec())
