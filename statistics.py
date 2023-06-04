from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from utils import utils


class Statistics(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.setWindowTitle('Click-Click Training')
        self.setWindowIcon(QIcon('pictures/заставка.png'))

        self.figure = Figure()
        self.figure.subplots_adjust(hspace=0.5)

        self.canvas = FigureCanvas(self.figure)
        hide_button = QPushButton('Скрыть статистику')
        hide_button.clicked.connect(lambda: self.setVisible(False))

        self.setFixedSize(1200, 600)

        data = utils.readFromJson("utils/statistics.json")
        x, y_count_characters, y_count_words, y_print_speed = [], [], [], []
        x_training_dynamics, y_training_dynamics = [], []

        x_training_dynamics.extend([int(i) for i in data['training_dynamics'] if i != "current_date"])
        y_training_dynamics.extend([data['training_dynamics'][i] for i in data['training_dynamics'] if i != "current_date"])

        x.extend([i for i in range(len(data['count_characters_entered']))])
        for count_characters, count_words, print_speed in zip(data['count_characters_entered'],
                                                              data['count_words_entered'],
                                                              data['print_speed']):
            y_count_characters.append(count_characters)
            y_count_words.append(count_words)
            y_print_speed.append(print_speed)

        plt.xticks(range(0, len(x), 1))

        ax1 = self.figure.add_subplot(2, 2, 1, title="Количество попыток")
        ax2 = self.figure.add_subplot(2, 2, 2, title="Количество набранных текстов")
        ax3 = self.figure.add_subplot(2, 2, 3, title="Скорость набора")
        ax4 = self.figure.add_subplot(2, 2, 4, title="Динамика тренировок")

        ax1.plot(x, y_count_characters)
        ax2.plot(x, y_count_words)
        ax3.plot(x, y_print_speed)
        ax4.plot(x_training_dynamics, y_training_dynamics)

        vbox.addWidget(self.canvas)
        vbox.addWidget(hide_button)

        self.canvas.draw()


def initialize_days_in_month(date):
    data = utils.readFromJson("utils/statistics.json")
    if len(data["training_dynamics"]) != 0:
        if data['training_dynamics']['current_date'] == date.toString():
            return
    data['training_dynamics']['current_date'] = date.toString()
    numbers_days = [str(day) for day in range(1, date.daysInMonth() + 1)]
    for number_day in numbers_days:
        data['training_dynamics'][number_day] = 0
    utils.writeToJson("utils/statistics.json", data)
