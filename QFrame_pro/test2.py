from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QTextTableFormat, QTextLength
from PyQt5.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        text_area = QTextEdit(self)
        layout.addWidget(text_area)

        cursor = text_area.textCursor()

        rows = 3
        cols = 4

        # 插入表格
        cursor.insertTable(rows, cols)

        # 设置列宽度约束
        table = cursor.currentTable()
        column_constraints = [QTextLength(QTextLength.FixedLength, 20 * (col + 1)) for col in range(cols)]
        tableFormat = table.format()
        tableFormat.setColumnWidthConstraints(column_constraints)
        table.setFormat(tableFormat)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
