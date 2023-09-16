from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        colors = ['red', 'black', 'cyan', 'white', 'yellow', 'gold', 'pink', 'green', 'blue']

        # 添加堆叠布局
        stacked_layout = QStackedLayout()
        stacked_layout.setStackingMode(QStackedLayout.StackAll)
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)

        # 添加label控件
        for i in range(9):
            label = QLabel(f'第{i + 1}个控件', self)
            label.resize(300, 300)
            label.setStyleSheet(f'background-color: {colors[i]}; font-size:30px;')
            stacked_layout.addWidget(label)

        button = QPushButton('变换颜色', self)
        button.clicked.connect(self.change_label)

        v_layout.addLayout(stacked_layout)
        v_layout.addWidget(button)

    def change_label(self):
        stacked_layout = self.findChild(QStackedLayout)
        timer = QTimer(self)
        timer.timeout.connect(
            lambda: stacked_layout.setCurrentIndex((stacked_layout.currentIndex() + 1) % stacked_layout.count()))
        timer.start(1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
