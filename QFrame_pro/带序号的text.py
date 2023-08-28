from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        plain_text_area = QPlainTextEdit(self)
        plain_text_area.setPlaceholderText('请输入信息')
        plain_text_area.setGeometry(100, 100, 400, 300)
        index_line = QWidget(self)
        index_line.setGeometry(70, 100, 30, 300)
        index_line.setStyleSheet('background-color:cyan;')
        index_line_label = QLabel(index_line)
        index_line_label.setText('\n'.join([str(i) for i in range(1, 101)]))
        index_line_label.move(0, 6)
        index_line_label.adjustSize()
        plain_text_area.updateRequest.connect(
            lambda rect, dy: index_line_label.move(0, index_line_label.y() + dy))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
