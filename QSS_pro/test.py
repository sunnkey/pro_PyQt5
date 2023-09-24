import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('Gradient Background Example')
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        for i in range(5):
            label = QLabel(f'Label_{i}', self)
            layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    # Apply QSS style to set the gradient background
    qss = """
    Window {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 white, stop:0.4 gray, stop:1 green);
    }
    """
    window.setStyleSheet(qss)

    sys.exit(app.exec())
