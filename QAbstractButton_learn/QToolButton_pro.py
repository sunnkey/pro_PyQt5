from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.tool_button = None
        self.setWindowTitle('')
        self.resize(500, 500)
        self.move(400, 400)
        self.setup_ui()

    def setup_ui(self):
        self.tool_button = QToolButton(self)
        self.tool_button.setText('新建')
        self.tool_button.setIcon(QIcon('../source/images/add.png'))
        self.tool_button.setToolTip('新建')
        self.tool_button.setToolButtonStyle(Qt.ToolButtonTextOnly)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
