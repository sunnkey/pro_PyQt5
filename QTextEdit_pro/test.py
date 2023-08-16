from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # 定义一个QTextEdit()文本编辑对象，对象名为'text_area'
        text_edit = QTextEdit(self)
        text_edit.setGeometry(50, 50, 200, 200)
        text_edit.setPlaceholderText('请输入信息')
        text_edit.setText('xxx')
        text_edit.setObjectName('text_area')
        # 定义光标对象，并将光标移至末尾
        cursor = text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText('111')
        # text_edit.setTextCursor(cursor)
        # text_edit.insertPlainText('我是新内容')
        # 定义一个按钮，按钮实现一些功能
        button = QPushButton('clicked', self)
        button.clicked.connect(self.insert_text)

    def clear_text(self):
        text = self.findChild(QTextEdit, 'text_area')
        text.clear()

    def insert_text(self):
        text = self.findChild(QTextEdit, 'text_area')
        cursor = text.textCursor()
        cursor.movePosition(QTextCursor.End)
        tc = QTextCharFormat()
        tc.setToolTip('我是样式')
        tc.setFontPointSize(30)
        cursor.insertText('222', tc)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
