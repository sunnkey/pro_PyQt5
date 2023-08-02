from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__()
        self.setWindowTitle('Timer')
        self.resize(500, 500)
        self.move(400, 400)
        self.counter = args[0]
        self.clock = None
        self.timer_id = None
        self.setup_ui()

    def setup_ui(self):
        self.label_clock()

    def label_clock(self):
        self.clock = QLabel(self)
        self.clock.setText(str(self.counter))
        self.clock.move(100, 100)
        self.clock.setStyleSheet('font-size:50px; border:1px solid black;')

    def add_timer(self, ms):
        self.timer_id = self.startTimer(ms)

    def timerEvent(self, event: 'QTimerEvent') -> None:
        current_counter = int(self.clock.text())
        current_counter -= 1
        self.clock.setText(str(current_counter))
        if current_counter == 0:
            self.killTimer(self.timer_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window(5)
    window.add_timer(1000)
    window.show()
    sys.exit(app.exec())
