from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        text_area = QTextEdit(self)
        text_area.setGeometry(50, 50, 300, 300)
        text_area.setObjectName('text_area')
        text_area.setText('123456789')
        # 删除按钮
        button_del = QPushButton('点击删除', self)
        button_del.move(10, 400)
        button_del.clicked.connect(self.button_clicked)
        # 判断是否在块末尾按钮
        button_at_block_end = QPushButton('光标是否在结尾', self)
        button_at_block_end.move(150, 400)
        button_at_block_end.clicked.connect(self.is_at_block_end)
        # 判断位置的按钮
        button_index = QPushButton('光标位置', self)
        button_index.move(300, 400)
        button_index.clicked.connect(self.show_index)

    def button_clicked(self):
        sender = self.sender()
        target = sender.parent().findChild(QTextEdit, 'text_area')
        print('我是删除按钮')
        cursor = target.textCursor()
        cursor.deleteChar()

    def is_at_block_end(self):
        sender = self.sender()
        target = sender.parent().findChild(QTextEdit, 'text_area')
        cursor = target.textCursor()
        if cursor.atBlockEnd():
            sender.setStyleSheet('background-color:red;')
        else:
            sender.setStyleSheet('background-color:white;')

    def show_index(self):
        sender = self.sender()
        target = sender.parent().findChild(QTextEdit, 'text_area')
        cursor = target.textCursor()
        print(cursor.position())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
