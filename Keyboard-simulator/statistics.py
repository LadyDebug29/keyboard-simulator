import sys

from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import utils


class Statistics(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        hide_button = QPushButton('Скрыть статистику')
        hide_button.clicked.connect(lambda : self.setVisible(False))
        vbox.addWidget(self.canvas)
        vbox.addWidget(hide_button)
        self.setLayout(vbox)


        data = utils.readFromJson()
        x, y = [], []
        x.extend([i for i in range(len(data['score']))])
        for item in data['score']:
            y.append(item)

        plt.xticks(range(0, len(x), 1))
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        plt.title('Ваша статистика')
        plt.xlabel('количество попыток')
        plt.ylabel('набранные очки')
        self.canvas.draw()
