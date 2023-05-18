import PyQt6.QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QPushButton
from enum import Enum
import keyboard_layout


class KeyboardLayout(Enum):
    RUSSIAN_LETTERS = 1
    CAPITAL_RUSSIAN_LETTERS = 2
    ENGLISH_LETTERS = 3
    CAPITAL_ENGLISH_LETTERS = 4


class Keyboard(QWidget):
    signal = PyQt6.QtCore.pyqtSignal(str)

    def __init__(self, grid):
        super().__init__()
        self.grid = grid
        self.current_keyboard_layout = KeyboardLayout.ENGLISH_LETTERS
        self.buttons = []
        self.keyboard_layout = keyboard_layout.KeyboardLayout()
        self.initUI()

    def initUI(self):
        self.set_keyboard_layout(self.keyboard_layout.english_letters)

    def keyboardKeyPressEvent(self, event):
        key = event.text()
        for button in self.buttons:
            if button.text() == key:
                button.animateClick()

            if event.key() == Qt.Key.Key_Backspace and \
                    button.text() == "Backspace":
                self.emit_signal("backspace")
                button.animateClick()
                break

            if event.key() == Qt.Key.Key_Tab and button.text() == "Tab":
                self.emit_signal("Tab")
                button.animateClick()
                break

            if event.key() == Qt.Key.Key_Alt and button.text() == "Alt":
                button.animateClick()

            if event.key() == Qt.Key.Key_Shift and button.text() == "Shift":
                button.animateClick()
                self.switch_letters_size()
                break

            if event.key() == Qt.Key.Key_Control and button.text() == "Ctrl":
                button.animateClick()

            if event.key() == Qt.Key.Key_CapsLock and button.text() == "Caps":
                button.animateClick()
                self.switch_letters_size()
                break

            if event.key() == Qt.Key.Key_Return and button.text() == "Enter":
                button.animateClick()

        self.emit_signal(key)
        event.accept()

    def emit_signal(self, text):
        self.signal.emit(text)

    def set_keyboard_layout(self, letters):
        y, x = 4, 0
        for row in letters:
            if y == 8:
                x += 1
            for label in row:
                button = QPushButton(label)
                button.setFixedHeight(50)
                button.setFont(QFont("Lab Grotesque", 15))
                button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                self.buttons.append(button)
                if label == "Shift":
                    button.setFixedWidth(153)
                    self.grid.addWidget(button, y, x, 1, 2)
                    x += 2
                    continue
                if label == " ":
                    button.setFixedWidth(487)
                    self.grid.addWidget(button, y, x, 1, 5)
                    continue
                if label == "Backspace" or label == "\\" or label == "Enter":
                    button.setFixedWidth(150)
                    self.grid.addWidget(button, y, x, 1, 2)
                    x += 1
                    continue
                self.grid.addWidget(button, y, x)
                x += 1
            x = 0
            y += 1

    def switch_keyboard_layout(self):
        if self.current_keyboard_layout == KeyboardLayout.ENGLISH_LETTERS or \
                self.current_keyboard_layout == \
                KeyboardLayout.CAPITAL_ENGLISH_LETTERS:
            self.set_keyboard_layout(self.keyboard_layout.russian_letters)
            self.current_keyboard_layout = KeyboardLayout.RUSSIAN_LETTERS

        elif self.current_keyboard_layout == KeyboardLayout.RUSSIAN_LETTERS or \
                self.current_keyboard_layout == \
                KeyboardLayout.CAPITAL_RUSSIAN_LETTERS:
            self.set_keyboard_layout(self.keyboard_layout.english_letters)
            self.current_keyboard_layout = KeyboardLayout.ENGLISH_LETTERS

    def switch_letters_size(self):
        if self.current_keyboard_layout == KeyboardLayout.ENGLISH_LETTERS:
            self.set_keyboard_layout(
                self.keyboard_layout.capital_english_letters)
            self.current_keyboard_layout = \
                KeyboardLayout.CAPITAL_ENGLISH_LETTERS

        elif self.current_keyboard_layout == \
                KeyboardLayout.CAPITAL_ENGLISH_LETTERS:
            self.set_keyboard_layout(self.keyboard_layout.english_letters)
            self.current_keyboard_layout = KeyboardLayout.ENGLISH_LETTERS

        elif self.current_keyboard_layout == KeyboardLayout.RUSSIAN_LETTERS:
            self.set_keyboard_layout(
                self.keyboard_layout.capital_russian_letters)
            self.current_keyboard_layout = \
                KeyboardLayout.CAPITAL_RUSSIAN_LETTERS

        elif self.current_keyboard_layout == \
                KeyboardLayout.CAPITAL_RUSSIAN_LETTERS:
            self.set_keyboard_layout(
                self.keyboard_layout.russian_letters)
            self.current_keyboard_layout = \
                KeyboardLayout.RUSSIAN_LETTERS
