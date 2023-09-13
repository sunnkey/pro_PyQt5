from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle('提示栏')
        message_box.setText('主要标题')
        message_box.setInformativeText('提示文版')
        check_box = QCheckBox(message_box)
        message_box.setDetailedText('11')
        message_box.setCheckBox(check_box)
        message_box.addButton(QMessageBox.StandardButton.Yes)
        message_box.addButton(QMessageBox.StandardButton.No)
        message_box.addButton(QMessageBox.StandardButton.Discard)
        message_box.show()
        # yes_btn = message_box.button(QMessageBox.StandardButton.Yes)
        # no_btn = message_box.button(QMessageBox.StandardButton.No)
        # discard_btn = message_box.button(QMessageBox.StandardButton.Discard)

        def slot_clicked(btn):
            print(message_box.buttonRole(btn))
            # if btn == yes_btn:
            #     print('yes')
            # elif btn == no_btn:
            #     print('no')
            # else:
            #     print('discard')

        message_box.buttonClicked.connect(slot_clicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
