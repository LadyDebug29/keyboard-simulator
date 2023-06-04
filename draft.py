from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QTimer, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # создание QLabel
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter) # выравнивание по центру
        self.label.setStyleSheet("font-size: 100px") # размер шрифта

        # добавление QLabel на центральный виджет
        self.setCentralWidget(self.label)

        # установка фиксированного размера окна
        self.setFixedSize(1200, 600)

        # создание таймера для обратного отсчета
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_label)
        self.timer.start()

        # начальное значение счетчика
        self.counter = 10

        # первое отображение счетчика
        self.update_label()

    def update_label(self):
        self.label.setText(str(self.counter))

        # завершение счетчика
        if self.counter == 0:
            self.timer.stop()
            self.label.setText("Finish!")
        else:
            self.counter -= 1

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
