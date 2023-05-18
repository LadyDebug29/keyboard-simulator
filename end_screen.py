from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

import display_text
import main_screen
import statistics


class EndScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.setWindowTitle('Click-Click Training')
        self.setWindowIcon(QIcon('pictures/заставка.png'))

        # устанавливаем фон виджета
        background_label = QLabel(self)
        pixmap = QPixmap('pictures/background.png')
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, 1200, 600)
        background_label.lower()

        self.name_game = QLabel(self)
        self.name_game.setText('           Click-Click Training')

        self.button_start_game = QPushButton('Начать заново')
        self.button_statistics = QPushButton('Посмотреть статистику')
        self.button_main_screen = QPushButton('Главное меню')

        self.name_game.setFixedSize(500, 200)
        self.button_start_game.setFixedSize(500, 50)
        self.button_statistics.setFixedSize(500, 50)
        self.button_main_screen.setFixedSize(500, 50)

        self.name_game.setFont(QFont("Lab Grotesque", 25))
        self.button_start_game.setFont(QFont("Lab Grotesque", 25))
        self.button_statistics.setFont(QFont("Lab Grotesque", 25))
        self.button_main_screen.setFont(QFont("Lab Grotesque", 25))

        self.button_start_game.clicked.connect(self.show_game)
        self.button_statistics.clicked.connect(lambda: statistics.Statistics().setVisible(True))
        self.button_main_screen.clicked.connect(self.show_main_screen)

        vbox.addWidget(self.name_game)
        vbox.addWidget(self.button_start_game)
        vbox.addWidget(self.button_statistics)
        vbox.addWidget(self.button_main_screen)

        vbox.setSpacing(25)
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setFixedSize(1200, 600)

    def show_game(self):
        self.close()
        self.game = display_text.DisplayText()
        self.game.show()

    def show_main_screen(self):
        self.close()
        self.main_screen = main_screen.MainScreen()
        self.main_screen.show()
