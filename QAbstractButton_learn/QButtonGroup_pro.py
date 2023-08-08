from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('')
        self.resize(500, 500)
        self.move(400, 400)
        self.setup_ui()

    def setup_ui(self):
        button_yes = QRadioButton('Yes', self)
        button_yes.move(10, 10)
        button_no = QRadioButton('No', self)
        button_no.move(10, 50)
        choose_button_group = QButtonGroup(self)
        choose_button_group.addButton(button_yes)
        choose_button_group.addButton(button_no)
        button_male = QRadioButton('Male', self)
        button_male.move(110, 10)
        button_female = QRadioButton('Female', self)
        button_female.move(110, 50)
        sex_button_group = QButtonGroup(self)
        sex_button_group.addButton(button_male)
        sex_button_group.addButton(button_female)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
