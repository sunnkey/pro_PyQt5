from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # 生成QFontDialog对象
        font = QFont()
        font.setFamily('宋体')
        font.setPointSize(20)
        font_dialog = QFontDialog(font, self)
        # 添加QColorDialog对象
        color_dialog = QColorDialog(self)
        # 添加button
        # button_font
        button_font = QPushButton('编辑字体', self)
        button_font.setGeometry(50, 50, 80, 60)
        # button_color
        button_color = QPushButton('设置颜色', self)
        button_color.setGeometry(150, 50, 80, 60)
        # button_other
        button_other = QPushButton('点击测试', self)
        button_other.setGeometry(250, 50, 80, 60)
        # 添加label对象
        label = QLabel('测试字体', self)
        label.setGeometry(50, 200, 450, 200)
        # 添加信号
        button_font.clicked.connect(lambda: font_dialog.open())
        button_color.clicked.connect(lambda: color_dialog.show())
        # font_dialog.currentFontChanged.connect(lambda val: label.setFont(val))
        # font_dialog.currentFontChanged.connect(self.set_select_font)
        font_dialog.fontSelected.connect(self.set_select_font)
        color_dialog.colorSelected.connect(self.set_background_color)
        button_other.clicked.connect(lambda: print(color_dialog.customCount()))
        result = color_dialog.getColor()
        print(result)

    def set_select_font(self, font):
        label = self.findChild(QLabel)
        label.setFont(font)

    def set_background_color(self, color):
        palette = QPalette()
        palette.setColor(QPalette.Background, color)
        self.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
