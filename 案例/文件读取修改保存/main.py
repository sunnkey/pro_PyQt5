from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # 添加按钮，打开，保存
        button_open = QPushButton('打开文件', self)
        button_open.setGeometry(150, 50, 80, 50)
        button_save = QPushButton('保存文件', self)
        button_save.setGeometry(300, 50, 80, 50)
        # 添加text_area
        text_area = QTextEdit(self)
        text_area.setGeometry(100, 150, 400, 350)
        # 添加信号
        button_open.clicked.connect(self.open_file)
        button_save.clicked.connect(self.save_file)

    def open_file(self):
        text_area = self.findChild(QTextEdit)
        file_path = \
            QFileDialog.getOpenFileName(self, '选择文件', './',
                                        'All(*.*);;python(*.py);;图片(*.png *.jpeg *.gif);;文档(*.txt)')[0]
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if content:
                text_area.setPlainText(content)

    def save_file(self):
        text_area = self.findChild(QTextEdit)
        file_path = \
            QFileDialog.getSaveFileName(self, '选择文件', './',
                                        'All(*.*);;python(*.py);;图片(*.png *.jpeg *.gif);;文档(*.txt)')[0]
        with open(file_path, 'w', encoding='utf-8') as file:
            content = text_area.toPlainText()
            file.write(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
