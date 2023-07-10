from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self, colors):
        super(Window, self).__init__()
        self.resize(900, 900)
        self.move(500, 500)
        self.colors = colors
        self.set_ui()

    def set_ui(self):
        print(self.colors)
        sons = []
        for i in range(3):
            for j in range(3):
                color = self.colors[i * 3 + j]
                son = QWidget(self)
                son.resize(300, 300)
                son.move(i * 300, j * 300)
                son.setStyleSheet(f'background-color:{color};')
                sons.append(son)


if __name__ == '__main__':
    colors = ['cyan', 'red', 'blue', 'yellow', 'green', 'black', 'gold', 'snow', 'grey']
    app = QApplication(sys.argv)
    window = Window(colors)
    window.show()

    sys.exit(app.exec())
