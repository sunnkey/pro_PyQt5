import typing

from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class MyAbstractSpinBox(QSpinBox):
    def __init__(self, parent=None, num=0):
        super(MyAbstractSpinBox, self).__init__(parent)
        self.setGeometry(200, 200, 80, 40)
        self.lineEdit().setText(str(num))

    def stepEnabled(self) -> 'QAbstractSpinBox.StepEnabled':
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, steps: int) -> None:
        current_num = int(self.text()) + steps
        self.lineEdit().setText(str(current_num))

    def setValue(self, value):
        super().setValue(value)
        self.valueChanged.emit(value)

    def validate(self, input_text: str, pos: int) -> typing.Tuple[QtGui.QValidator.State, str, int]:
        try:
            value = int(input_text)
            if 0 <= value <= 100:
                return QValidator.Acceptable, input_text, pos
            elif value < 0:
                return QValidator.Intermediate, '0', pos
            elif value > 100:
                return QValidator.Intermediate, '100', pos
        except ValueError:
            return QValidator.Intermediate, '0', pos

    def fixup(self, input_text: str) -> str:
        try:
            int(input_text)
            return input_text
        except ValueError:
            return ''


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        abstract_spin_box = MyAbstractSpinBox(self)
        abstract_spin_box.valueChanged.connect(lambda value: print(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    QDesktopServices.openUrl(QUrl('https://www.sunnkey.cn'))

    sys.exit(app.exec())
