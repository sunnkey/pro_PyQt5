from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QAbstractSpinBox, QVBoxLayout, QWidget
import sys


class MySpinBox(QAbstractSpinBox):
    valueChanged = pyqtSignal(int)  # 自定义信号

    def __init__(self, parent=None):
        super(MySpinBox, self).__init__(parent)

    def stepBy(self, steps):
        self.setValue(self.value() + steps)

    def setValue(self, value):
        super().setValue(value)
        self.valueChanged.emit(value)  # 在值变化时发射信号


class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        spin_box = MySpinBox()
        layout.addWidget(spin_box)
        self.setLayout(layout)

        spin_box.valueChanged.connect(self.value_changed)

    def value_changed(self, new_value):
        print("Value changed:", new_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
