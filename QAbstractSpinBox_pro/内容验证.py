from PyQt5.Qt import *
import sys


class MyAbstractSpinBox(QAbstractSpinBox):
    def __init__(self, parent=None, num=0):
        super(MyAbstractSpinBox, self).__init__(parent)
        self.setGeometry(200, 200, 80, 40)
        self.lineEdit().setText(str(num))

    def setEnabled(self, a0: bool) -> None:
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, steps: int) -> None:
        self.lineEdit().setText('10')


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        abstract_spin_box = MyAbstractSpinBox(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
