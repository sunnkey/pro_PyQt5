from PyQt5.Qt import *
import sys


class MyAbstractSpinBox(QAbstractSpinBox):
    def __init__(self, parent=None, num='0', step=2, *args, **kwargs):
        super(MyAbstractSpinBox, self).__init__(parent)
        self.step = step
        self.lineEdit().setText(num)

    def stepEnabled(self) -> 'QAbstractSpinBox.StepEnabled':
        current_num = int(self.text())
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, steps: int) -> None:
        current_num = int(self.text()) + steps * self.step
        self.lineEdit().setText(str(current_num))


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()
        self.button1 = None
        self.button2 = None

    def setup_ui(self):
        spin_box = MyAbstractSpinBox(self)
        spin_box.setAccelerated(True)
        spin_box.setFrame(True)
        spin_box.move(100, 100)
        spin_box.resize(80, 30)
        self.button1 = QPushButton('cancel borders', self)
        self.button2 = QPushButton('show borders', self)
        self.button2.move(0, 60)
        self.button1.clicked.connect(lambda: spin_box.setFrame(False))
        self.button2.clicked.connect(lambda: spin_box.setFrame(True))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
