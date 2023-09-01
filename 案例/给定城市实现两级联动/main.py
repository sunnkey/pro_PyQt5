# -------------------------
# 1、给定城市数据
# 2、实现两级联动效果
# -------------------------


from PyQt5.Qt import *
import sys

city_dic = {
    '北京': {
        '东城': '001',
        '西城': '002',
        '朝阳': '003',
        '丰台': '004',
    },
    '上海': {
        '黄埔': '005',
        '徐汇': '006',
        '长宁': '007',
        '静安': '008',
        '松江': '009',
    },
    '广东': {
        '广州': '010',
        '深圳': '011',
        '湛江': '012',
        '佛山': '013',
    },
}


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(1400, 600, 600, 600)
        self.setWindowTitle('')
        self.setup_ui()

    def setup_ui(self):
        # 市级选择框
        city_combox_box = QComboBox(self)
        city_combox_box.setObjectName('city_selector')
        city_combox_box.setGeometry(100, 100, 120, 30)
        # 县区选择框
        town_combo_box = QComboBox(self)
        town_combo_box.setObjectName('town_selector')
        town_combo_box.setGeometry(280, 100, 120, 30)
        # 增加城市变动信号
        city_combox_box.currentIndexChanged.connect(self.slot_city_changed)
        # 增加县区变动信号
        town_combo_box.currentIndexChanged.connect(self.slot_town_changed)
        # 市级选择框增加选项
        for key in city_dic.keys():
            city_combox_box.addItem(key)

    def slot_city_changed(self):
        city = self.findChild(QComboBox, 'city_selector')
        town = self.findChild(QComboBox, 'town_selector')
        town.clear()
        for key, value in city_dic[city.currentText()].items():
            town.addItem(key, value)
        # print(city.currentText())
        # print(town.currentText())
        # print(town.currentData())

    def slot_town_changed(self):
        city = self.findChild(QComboBox, 'city_selector')
        town = self.findChild(QComboBox, 'town_selector')
        if town.currentText():
            print(city.currentText())
            print(town.currentText())
            print(town.currentData())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
