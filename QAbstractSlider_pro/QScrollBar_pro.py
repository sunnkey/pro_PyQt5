from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        scroll_bar = QScrollBar(Qt.Horizontal, self)
        scroll_bar.setGeometry(100, 100, 200, 30)
        scroll_bar.setPageStep(100)

        dial = QDial(self)
        dial.setRange(0, 200)
        dial.setNotchesVisible(True)
        dial.setNotchTarget(40)
        # dial.setWrapping(True)

        label = QLabel('字体大小设置', self)
        label.move(100, 300)
        label.adjustSize()

        dial.valueChanged.connect(lambda val: set_font_size(val))

        def set_font_size(val):
            label.setStyleSheet(f'font-size:{val}px;')
            label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
