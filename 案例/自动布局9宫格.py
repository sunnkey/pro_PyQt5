from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self, colors):
        super(Window, self).__init__()
        self.setMaximumSize(1200, 1200)
        self.setMinimumSize(400, 400)
        self.resize(900, 900)
        self.move(500, 500)
        self.colors = colors
        self.set_ui()

    def set_ui(self):
        layout = QGridLayout(self)  # 使用QGridLayout作为父窗口的布局管理器
        for i in range(3):
            for j in range(3):
                color = self.colors[i * 3 + j]
                son = QWidget(self)
                son.setStyleSheet(f'background-color:{color};')
                layout.addWidget(son, i, j)  # 将子窗口添加到布局中

        self.setLayout(layout)  # 设置父窗口的布局


if __name__ == '__main__':
    colors = ['cyan', 'red', 'blue', 'yellow', 'green', 'black', 'gold', 'snow', 'grey']
    app = QApplication(sys.argv)
    window = Window(colors)
    window.show()

    sys.exit(app.exec())
