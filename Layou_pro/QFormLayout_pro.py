from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # 表单控件
        # 姓名部分
        label_name = QLabel('姓名(&n)', self)
        line_edit_name = QLineEdit(self)
        line_edit_name.setPlaceholderText('请输入姓名')
        label_name.setBuddy(line_edit_name)
        # 密码部分
        label_password = QLabel('密码(&p)', self)
        label_password.setObjectName('label_password')
        line_edit_password = QLineEdit(self)
        line_edit_password.setPlaceholderText('请输入密码')
        label_password.setBuddy(line_edit_password)
        # 年龄部分
        spinbox_age = QSpinBox(self)
        # 性别部分
        label_sex = QLabel('性别', self)
        checkbox_male = QRadioButton('男', self)
        checkbox_female = QRadioButton('女', self)
        layout_sex = QHBoxLayout()
        layout_sex.addWidget(checkbox_male)
        layout_sex.addWidget(checkbox_female)
        # 其他部分
        line_edit_info = QLineEdit(self)
        # 提交部分
        submit = QPushButton('提交', self)
        submit.clicked.connect(self.slot_submit)

        # 布局部分
        layout_form = QFormLayout()
        layout_form.setObjectName('layout_form')
        self.setLayout(layout_form)
        # 添加布局
        layout_form.addRow(label_name, line_edit_name)
        layout_form.addRow(label_password, line_edit_password)
        layout_form.addRow('年龄(&a)', spinbox_age)
        layout_form.addRow(label_sex, layout_sex)
        layout_form.addRow('info', line_edit_info)
        layout_form.addRow(submit)

        # 根据标签修改
        layout_form.labelForField(line_edit_info).setText('Info')

    def slot_submit(self):
        label_password = self.findChild(QLabel, 'label_password')
        layout_form = self.findChild(QFormLayout, 'layout_form')
        print(layout_form)
        print(layout_form.getWidgetPosition(label_password))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
