from PyQt5 import QtGui
from PyQt5.Qt import *
import sys


class SnakeGame(QMainWindow):
    def __init__(self):
        super(SnakeGame, self).__init__()
        self.initUI()
        # 添加游戏画布
        self.game_board = GameBoard()
        self.setCentralWidget(self.game_board)
        # 初始化游戏

    def initUI(self):
        self.setGeometry(1500, 500, 500, 500)
        self.setWindowTitle('Snake Game')
        self.show()


class GameBoard(QWidget):
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        qp = QPainter(self)
        qp.fillRect(0, 0, self.width(), self.height(), Qt.white)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = SnakeGame()
    sys.exit(app.exec())
