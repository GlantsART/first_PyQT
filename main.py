import sys
from random import randint
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF


class First(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.pushButton.clicked.connect(self.run)

    def initUI(self):
        self.setGeometry(100, 100, 750, 600)
        self.setWindowTitle('Рисование кругов')
        self.pushButton = QPushButton('Это кнопка!', self)
        self.pushButton.resize(120, 100)
        self.pushButton.move(40, 50)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            coords = randint(20, 250)
            qp.drawEllipse(QPointF(400, 300), coords, coords)
        self.flag = False

    def run(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = First()
    ex.show()
    sys.exit(app.exec())
