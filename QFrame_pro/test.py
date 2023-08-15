from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet('background-color: cyan;')
        frame.setFrameShadow(QFrame.Raised)
        frame.setLineWidth(10)
        frame.setMidLineWidth(20)
        frame.move(200, 200)
        frame.resize(300, 300)
        frame.setFrameRect(QRect(100, 100, 300, 300))
        print(frame.frameRect())
        button = QPushButton(frame)
        button.resize(120, 80)
        button.setText('Push Button')
        layout.addWidget(button)
        frame.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
