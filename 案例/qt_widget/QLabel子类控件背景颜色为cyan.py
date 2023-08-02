from PyQt5.Qt import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    q_label1 = QLabel(widget)
    q_label1.setText('label1')
    q_label2 = QLabel(widget)
    q_label2.move(100, 0)
    q_label2.setText('label2')
    q_label3 = QLabel(widget)
    q_label3.move(200, 0)
    q_label3.setText('label3')
    q_btn = QPushButton(widget)
    q_btn.move(20, 100)
    q_btn.setText('按钮')

    for sub_widget in widget.findChildren(QLabel):
        print(sub_widget)
        sub_widget.setStyleSheet('background: cyan; border:1px solid red')

    widget.resize(1200, 960)
    widget.show()

sys.exit(app.exec())
