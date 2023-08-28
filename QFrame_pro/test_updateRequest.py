import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit


class TextEditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Text Editor')
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setGeometry(10, 10, 580, 380)

        self.text_edit.updateRequest.connect(self.handleUpdateRequest)

    def handleUpdateRequest(self, rect, dy):
        print(f"Update requested for rect: {rect} with dy: {dy}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEditorWindow()
    window.show()
    sys.exit(app.exec_())
