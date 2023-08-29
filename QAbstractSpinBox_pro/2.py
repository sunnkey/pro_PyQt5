from PyQt5.QtWidgets import QApplication, QAbstractSpinBox
import sys


class MyAbstractSpinBox(QAbstractSpinBox):
    def __init__(self, parent=None, num='0', step=1, *args, **kwargs):
        super(MyAbstractSpinBox, self).__init__(parent)
        self._step = step
        self.lineEdit().setText(num)

    def stepEnabled(self) -> 'QAbstractSpinBox.StepEnabled':
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, steps: int) -> None:
        current_num = int(self.text()) + self._step * steps
        self.lineEdit().setText(str(current_num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    spin_box = MyAbstractSpinBox(step=5)

    spin_box.setButtonSymbols(QAbstractSpinBox.NoButtons)  # 先设置为 NoButtons 样式
    spin_box.setButtonSymbols(QAbstractSpinBox.PlusMinus)  # 设置加号和减号按钮文本

    spin_box.show()
    sys.exit(app.exec_())
