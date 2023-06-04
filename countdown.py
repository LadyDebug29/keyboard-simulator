from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QSizePolicy
from PyQt6.QtCore import QTimer, Qt

import player_screen


class Countdown(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.setWindowTitle('Countdown')
        self.setWindowIcon(QIcon('pictures/заставка.png'))

        self.label = QLabel(self)
        self.label.setFont(QFont("Lab Grotesque", 55))
        self.label.setFixedSize(1200, 600)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox.addWidget(self.label)

        self.setFixedSize(1200, 600)

        # начальное значение счетчика
        self.counter = 10

    def update_label(self):
        self.label.setText(str(self.counter))

        # завершение счетчика
        if self.counter == 0:
            self.timer.stop()
            self.counter = 10
            self.close()
        else:
            self.counter -= 1

    def start(self):
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_label)
        self.timer.start()

        self.show()

    def closeEvent(self, event):
        self.close()
        self.screen_player = player_screen.PlayerScreen(True)
        self.screen_player.start()
        event.accept()
