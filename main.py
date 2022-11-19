import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.f = False
        self.setWindowTitle('Желтые круги')
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.setBrush(QColor(255, 255, 0))
            a = random.randint(10, 130)
            qp.drawEllipse(random.randint(100, 600), random.randint(100, 400), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())