from PyQt6 import QtCore
from PyQt6.QtCore import Qt, QEvent, QTimer, QDate
from PyQt6.QtGui import QKeyEvent, QFont, QGuiApplication, QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, \
    QLineEdit, QPushButton, QGridLayout

import countdown
import end_screen
import keyboard
import words
import multiplayer_statistics
from utils import utils


class PlayerScreen(QWidget):
    count_players = 0

    def __init__(self, isMultiplayer):
        super().__init__()
        self.shift_pressed = False
        self.caps_pressed = False
        self.count_points = 0
        self.count_words = 0
        self.countdown = 5
        self.date = QDate().currentDate()
        self.isMultiplayer = isMultiplayer

        if isMultiplayer:
            PlayerScreen.count_players += 1
        else:
            if PlayerScreen.count_players % 2 == 0:
                PlayerScreen.count_players = 0
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.setWindowTitle('Click-Click Training')
        self.setWindowIcon(QIcon('pictures/заставка.png'))
        pixmap = QPixmap('pictures/background.png')

        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, 1200, 600)
        background_label.lower()

        # Создаем строку с текстом, который будет выводиться в окне
        self.words = words.Words()
        self.words.download_words()
        self.word = self.words.get_word()

        # Создание кнопки "Выйти из игры"
        self.button_end = QPushButton("Завершить игру")
        self.button_end.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_end.clicked.connect(self.close)
        self.button_end.setFixedSize(100, 50)
        grid.addWidget(self.button_end, 0, 0)

        # Создаю элемент интерфейса для отображения счетчика
        self.counter = QLabel(self)
        self.counter.setText(f"Набрано очков: "
                             f"<font color='green'>"
                             "0"
                             f"</font>")
        self.counter.setFont(QFont("Lucida Sans Unicode", 25))
        self.counter.setFixedSize(500, 50)
        self.counter.setFixedWidth(self.counter.sizeHint().width())
        grid.addWidget(self.counter, 0, 11, 1, 2)
        grid.setAlignment(self.counter, Qt.AlignmentFlag.AlignRight)

        # Создаем элемент интерфейса для отображения слова
        self.lblWord = QLabel(self)
        self.lblWord.setText(self.word)
        self.lblWord.setFont(QFont("Lab Grotesque", 35))
        grid.addWidget(self.lblWord, 2, 0, 1, 15)
        grid.setAlignment(self.lblWord, Qt.AlignmentFlag.AlignHCenter)

        # Создаем элемент интерфейса для ввода символов
        self.txtInput = QLineEdit(self)
        self.txtInput.textChanged.connect(self.handleInput)
        self.txtInput.setFixedHeight(65)
        self.txtInput.setFont(QFont("Lab Grotesque", 25))
        grid.addWidget(self.txtInput, 3, 0, 2, 15)

        self.timer_value = QLabel(f'Осталось {self.countdown} секунд')
        self.timer_value.setFixedSize(500, 50)
        self.timer_value.setFont(QFont("Lucida Sans Unicode", 25))
        grid.addWidget(self.timer_value, 0, 5, 1, 2)

        self.keyboard = keyboard.Keyboard(grid)
        self.keyboard.signal.connect(self.line_edit)
        self.setFixedSize(1200, 600)
        self.center()

    def center(self):
        geometry = QGuiApplication.primaryScreen().availableGeometry()
        window_size = self.frameGeometry()
        x = int((geometry.width() - window_size.width()) / 2)
        y = int((geometry.height() - window_size.height()) / 2)
        self.move(x, y)

    def line_edit(self, text):
        if text == "backspace":
            self.txtInput.backspace()
        elif text == "Tab":
            self.txtInput.cursorForward(False, 4)
        else:
            self.txtInput.setText(self.txtInput.text() + text)

    def handleInput(self, text):

        if len(text) == 0:
            self.lblWord.setText(self.word)
            return
        if text == self.word[:len(text)]:
            self.lblWord.setText(f"<font color='green'>"
                                 f"{self.word[:len(text)]}"
                                 f"</font>"
                                 f"{self.word[len(text):]}")
            self.count_points += 1
            if len(text) == len(self.word):
                self.count_words += 1
                self.word = self.words.get_word()
                self.lblWord.setText(self.word)
                self.counter.setText(f"Набрано очков: "
                                     f"<font color='green'> \
                                     {self.count_points}"
                                     f"</font>")
                self.txtInput.clear()

    def keyPressEvent(self, event):
        if event.modifiers() == (QtCore.Qt.KeyboardModifier.ShiftModifier |
                                 QtCore.Qt.KeyboardModifier.AltModifier):
            self.keyboard.switch_keyboard_layout()

        elif event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self.shift_pressed = True
            self.keyboard.switch_letters_size()

        elif self.shift_pressed:
            self.process_shifted_key(event)
            self.shift_pressed = False

        elif event.key() == Qt.Key.Key_CapsLock and not self.caps_pressed:
            self.caps_pressed = True
            self.keyboard.keyboardKeyPressEvent(event)

        elif event.key() == Qt.Key.Key_CapsLock and self.caps_pressed:
            self.caps_pressed = False
            self.keyboard.keyboardKeyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_CapsLock:
            event.accept()
        if event.key() == Qt.Key.Key_Shift:
            self.keyboard.keyboardKeyPressEvent(event)

    def process_shifted_key(self, event):
        text = event.text().upper()
        new_event = QKeyEvent(
            QEvent.Type.KeyPress,
            event.key(),
            event.modifiers(),
            text,
            event.isAutoRepeat(),
            event.count(),
        )
        super().keyPressEvent(new_event)

    def closeEvent(self, event):
        if PlayerScreen.count_players == 1:
            self.countdown = countdown.Countdown()
            self.countdown.start()
        elif PlayerScreen.count_players == 2:
            self.multiplayer_statistics = multiplayer_statistics.MultiPlayerStatistics()
            self.multiplayer_statistics.setVisible(True)
        else:
            self.end_screen = end_screen.EndScreen()
            self.end_screen.show()
            event.accept()

    def update_countdown(self):
        self.countdown -= 1
        if self.countdown == 0:
            self.timer.stop()
            if not self.isMultiplayer:
                data = utils.readFromJson("utils/statistics.json")
                data['count_characters_entered'].append(self.count_points)
                data['count_words_entered'].append(self.count_words)
                data['print_speed'].append(self.count_points / 60)
                data['training_dynamics'][str(self.date.day())] += 1

                utils.writeToJson("utils/statistics.json", data)
                self.close()
            else:
                data = utils.readFromJson("utils/multiplayer_statistics.json")
                if PlayerScreen.count_players % 2 == 1:
                    data['statistic_first_player'].append(self.count_points)
                if PlayerScreen.count_players % 2 == 0:
                    data['statistic_second_player'].append(self.count_points)
                utils.writeToJson("utils/multiplayer_statistics.json", data)
                self.close()
        self.timer_value.setText(f'Осталось {self.countdown} секунд')

    def start(self):
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start()
        self.show()
