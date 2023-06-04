from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import main_screen
from utils import utils


class MultiPlayerStatistics(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.setWindowTitle('Click-Click Training')
        self.setWindowIcon(QIcon('pictures/заставка.png'))

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        hide_button = QPushButton('Скрыть статистику')
        hide_button.clicked.connect(self.show_main_screen)

        self.setFixedSize(1200, 600)

        data = utils.readFromJson("utils/multiplayer_statistics.json")
        x, y_first_player, y_second_player = [], [], []
        x.extend([i for i in range(len(data['statistic_first_player']))])
        for item1, item2 in zip(data['statistic_first_player'], data['statistic_second_player']):
            y_first_player.append(item1)
            y_second_player.append(item2)

        plt.xticks(range(0, len(x), 1))

        ax1 = self.figure.add_subplot(2, 2, 1, title="Статистика 1 игрока")
        ax2 = self.figure.add_subplot(2, 2, 2, title="Статистика 2 игрока")

        ax1.plot(x, y_first_player)
        ax2.plot(x, y_second_player)

        vbox.addWidget(self.canvas)
        vbox.addWidget(hide_button)

        self.canvas.draw()

    def show_main_screen(self):
        self.setVisible(False)
        self.main_screen = main_screen.MainScreen()
        self.main_screen.show()