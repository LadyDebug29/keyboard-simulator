from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QGridLayout, QProgressBar
from PyQt6.QtCore import Qt

class SplashScreen(QtWidgets.QSplashScreen):
    def __init__(self):
        pix_map = QtGui.QPixmap('Kosmicheskij-zagruzochnyj-ekran-v-Brawl-Stars.jpg')
        new_size = QtCore.QSize(600, 400)
        resized_pix_map = pix_map.scaled(new_size)
        super().__init__(resized_pix_map)
        grid = QGridLayout()
        self.setLayout(grid)

        # Создаем прогресс бар и добавляем его на экран загрузки
        self.progress_bar = QProgressBar()
        self.progress_bar.setWindowModality(Qt.WindowModality.WindowModal)
        grid.addWidget(self.progress_bar)
