from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

import player_screen
import statistics
import multiplayer_game


class MainScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.date = QDate().currentDate()
        statistics.initialize_days_in_month(self.date)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.setWindowTitle('Click-Click Training')
        self.setWindowIcon(QIcon('pictures/заставка.png'))

        # Устанавливаю фон виджета
        background_label = QLabel(self)
        pixmap = QPixmap('pictures/background.png')
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, 1200, 600)
        background_label.lower()

        self.name_game = QLabel(self)
        self.name_game.setText('           Click-Click Training')

        self.button_start_game = QPushButton('Начать тренировку')
        self.button_multiplayer = QPushButton('Соревнование с другом')
        self.button_statistics = QPushButton('Посмотреть статистику')
        self.button_end_game = QPushButton('Выйти из игры')

        self.name_game.setFixedSize(500, 200)
        self.button_start_game.setFixedSize(500, 50)
        self.button_multiplayer.setFixedSize(500, 50)
        self.button_statistics.setFixedSize(500, 50)
        self.button_end_game.setFixedSize(500, 50)

        self.name_game.setFont(QFont("Lab Grotesque", 25))
        self.button_start_game.setFont(QFont("Lab Grotesque", 25))
        self.button_multiplayer.setFont(QFont("Lab Grotesque", 25))
        self.button_statistics.setFont(QFont("Lab Grotesque", 25))
        self.button_end_game.setFont(QFont("Lab Grotesque", 25))

        self.button_start_game.clicked.connect(self.show_game)
        self.button_multiplayer.clicked.connect(self.show_multiplayer_game)
        self.button_statistics.clicked.connect(
            lambda: statistics.Statistics().setVisible(True))
        self.button_end_game.clicked.connect(self.close)

        vbox.addWidget(self.name_game)
        vbox.addWidget(self.button_start_game)
        vbox.addWidget(self.button_multiplayer)
        vbox.addWidget(self.button_statistics)
        vbox.addWidget(self.button_end_game)

        vbox.setSpacing(25)
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setFixedSize(1200, 600)

    def show_game(self):
        self.close()
        self.game = player_screen.PlayerScreen(False)
        self.game.start()

    def show_multiplayer_game(self):
        self.close()
        self.multiplayer_game = multiplayer_game.MultiplayerGame()
        self.multiplayer_game.start()
