from PyQt5.Qt import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300, 300)
    obj = QObject(window)
    w = QWidget(window)
    btn = QPushButton(window)
    label = QLabel(window)

    objs = [obj, w, btn, label]

    for o in objs:
        print(o.isWidgetType())

    window.show()

    sys.exit(app.exec())
