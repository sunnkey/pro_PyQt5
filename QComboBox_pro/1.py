from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # 生成下拉框
        combo_box = QComboBox(self)
        combo_box.setGeometry(150, 150, 160, 30)
        # 增加下拉选项
        combo_box.addItem(QIcon('../source/images/add.png'), '选项一', {'name': 'test'})
        combo_box.addItem('选项二')
        combo_box.addItem('选项三')
        combo_box.addItem('选项四')
        combo_box.insertSeparator(3)
        combo_box.insertSeparator(5)

        combo_box.addItem(QIcon('../source/images/add.png'), '选项五')
        combo_box.addItems(['选项六', '选项七'])
        # 修改指定下拉框
        combo_box.setItemText(0, '选项1')
        combo_box.setEditText('选项三')
        # 生成按钮
        button = QPushButton('点击', self)
        # 获取信息
        button.clicked.connect(lambda: print(self.findChild(QComboBox).itemData(0)))
        # 信号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
