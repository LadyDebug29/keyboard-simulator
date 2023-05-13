from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt6.QtGui import QKeyEvent, QFont, QGuiApplication
from PyQt6.QtCore import Qt, QEvent
import keyboard
import words
import threading


class DisplayText(QWidget):
    def __init__(self):
        super().__init__()
        self.shift_pressed = None
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # Создаем строку с текстом, который будет выводиться в окне
        self.words = words.Words()
        thread = threading.Thread(target=self.words.download_words())
        thread.start()
        while thread.is_alive():
            continue
        self.word = self.words.get_word()

        # Создание кнопки "Выйти из игры"
        self.button_end = QPushButton("Выйти из игры")
        self.button_end.clicked.connect(self.close)
        self.button_end.setFixedSize(100, 50)
        grid.addWidget(self.button_end, 0, 0)

        # Создаю элемент интерфейса для отображения счетчика
        self.counter = QLabel(self)
        self.counter.setText("Набрано очков: 0")
        self.counter.setFont(QFont("Lab Grotesque", 25))
        grid.addWidget(self.counter, 0, 12, 1, 2)
        grid.setAlignment(self.counter, Qt.AlignmentFlag.AlignRight)

        # Создаем элемент интерфейса для отображения слова
        self.lblWord = QLabel(self)
        self.lblWord.setText(self.word)
        self.lblWord.setFont(QFont("Lab Grotesque", 30))
        grid.addWidget(self.lblWord, 2, 0, 1, 14)
        grid.setAlignment(self.lblWord, Qt.AlignmentFlag.AlignHCenter)

        # Заводим переменную для количества набранных очков
        self.count_points = 0

        # Создаем элемент интерфейса для ввода символов
        self.txtInput = QLineEdit(self)
        self.txtInput.textChanged.connect(self.handleInput)
        grid.addWidget(self.txtInput, 3, 0, 1, 14)

        self.keyboard = keyboard.Keyboard(grid)
        self.keyboard.signal.connect(self.line_edit)
        self.setGeometry(0, 0, 1200, 400)
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
            self.txtInput.setText(self.txtInput.text() + "    ")
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
                self.word = self.words.get_word()
                self.lblWord.setText(self.word)
                len_current_counter = len(self.counter.text().split()[-1])
                self.change_counter(len_current_counter)
                self.txtInput.clear()

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self.shift_pressed = True
        else:
            if hasattr(self, 'shift_pressed') and self.shift_pressed:
                self.process_shifted_key(event)
                self.shift_pressed = False
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

    def change_counter(self, len_previous_counter):
        self.counter.setText(self.counter.text()
                             [:len(self.counter.text()) - len_previous_counter]
                             + str(self.count_points))
