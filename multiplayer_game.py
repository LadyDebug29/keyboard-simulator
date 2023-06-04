from PyQt6.QtWidgets import QWidget
import countdown


class MultiplayerGame(QWidget):
    def __init__(self):
        super().__init__()
        self.countdown = countdown.Countdown()

    def start(self):
        self.countdown.start()
