from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtGui import QTextTableFormat, QTextCursor, QTextLength
from PyQt5.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        text_area = QTextEdit(self)
        self.setCentralWidget(text_area)
        cursor = text_area.textCursor()

        rows = 3
        cols = 4

        # 插入表格
        cursor.insertTable(rows, cols)
        table = cursor.currentTable()

        self.table_widths = [30 * (col + 1) for col in range(cols)]
        self.is_resizing = False
        self.resize_col = -1

        text_area.mousePressEvent = self.mouse_press_event
        text_area.mouseMoveEvent = self.mouse_move_event
        text_area.mouseReleaseEvent = self.mouse_release_event

        self.show()

    def mouse_press_event(self, event):
        cursor = self.centralWidget().textCursor()
        cursor.select(QTextCursor.TableCell)
        cell_rect = cursor.selectionRect()

        x_pos = event.x()
        col = 0
        for width in self.table_widths:
            if x_pos < cell_rect.left() + width:
                self.is_resizing = True
                self.resize_col = col
                break
            col += 1

    def mouse_move_event(self, event):
        if self.is_resizing:
            new_width = event.x() - self.centralWidget().textCursor().selectionRect().left()
            self.table_widths[self.resize_col] = new_width
            self.update_table_widths()

    def mouse_release_event(self, event):
        if self.is_resizing:
            self.is_resizing = False

    def update_table_widths(self):
        cursor = self.centralWidget().textCursor()
        cursor.movePosition(QTextCursor.StartOfBlock)
        cursor.movePosition(QTextCursor.EndOfBlock, QTextCursor.KeepAnchor)
        cursor.removeSelectedText()

        table_format = QTextTableFormat()
        column_constraints = [QTextLength(QTextLength.FixedLength, width) for width in self.table_widths]
        table_format.setColumnWidthConstraints(column_constraints)
        cursor.insertTable(1, 1, table_format)
        cursor.movePosition(QTextCursor.StartOfBlock)
        cursor.movePosition(QTextCursor.NextBlock, QTextCursor.KeepAnchor, 3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
