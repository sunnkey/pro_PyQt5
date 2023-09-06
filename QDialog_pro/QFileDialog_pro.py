from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # 添加按钮
        button_get_file = QPushButton('选择单个文件', self)
        button_get_file.setGeometry(50, 50, 120, 50)
        button_get_files = QPushButton('选择多个文件', self)
        button_get_files.setGeometry(200, 50, 120, 50)
        # 添加信号槽事件
        button_get_file.clicked.connect(
            lambda: QFileDialog.getOpenFileName(self, '选择文档', '../', 'All(*.*);;python(*.py)', 'All(*.*)'))
        button_get_files.clicked.connect(
            lambda: print(QFileDialog.getOpenFileNames(self, '选择文档', '../', 'All(*.*);;python(*.py)', 'All(*.*)')))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
