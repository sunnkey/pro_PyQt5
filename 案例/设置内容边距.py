from PyQt5.Qt import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(600, 600)
    son = QLabel(window)
    son.resize(250, 250)
    son.setStyleSheet('background:blue;')
    # window.setContentsMargins(100, 100, 100, 100)
    son.setText('测试边距内容')
    son.setContentsMargins(50, 50, 50, 50)
    print(son.getContentsMargins())

    window.show()
    sys.exit(app.exec())
