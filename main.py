import sys
from random import randint
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF


class First(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
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
