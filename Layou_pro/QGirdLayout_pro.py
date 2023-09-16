from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()
        # self.colors = ['red', 'black', 'cyan', 'white', 'yellow', 'gold', 'pink', 'green', 'blue']

    def setup_ui(self):
        colors = ['red', 'black', 'cyan', 'white', 'yellow', 'gold', 'pink', 'green', 'blue']
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        for i in range(9):
            label = QLabel(f'{i}', self)
            label.resize(50, 50)
            label.setStyleSheet(f'background-color:{colors[i]}')
            label.setObjectName(f'label_{i}')
            if i % 3 == 0:
                grid_layout.addWidget(label, (i // 3) * 2, 0, 1, 2)
                print(f'i:{i}')
                print((i // 3) * 2, 0, 1, 2)
            elif i % 3 == 1:
                grid_layout.addWidget(label, (i // 3) * 2 + 1, 0, 1, 1)
                print(f'i:{i}')
                print((i // 3) * 2 + 1, 0, 1, 1)
            else:
                grid_layout.addWidget(label, (i // 3) * 2 + 1, 1, 1, 1)
                print(f'i:{i}')
                print((i // 3) * 2 + 1, 0, 1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
