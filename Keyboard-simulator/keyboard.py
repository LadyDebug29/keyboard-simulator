import PyQt6.QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton
import display_text

class Keyboard(QWidget):
    signal = PyQt6.QtCore.pyqtSignal(str)

    def __init__(self, grid):
        super().__init__()
        self.initUI(grid)

    def initUI(self, grid):
        self.setStyleSheet('background-color: white;')

        self.buttons = []
        self.rows = [["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "Backspace"],
                     ["Tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\"],
                     ["Caps", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "Enter"],
                     ["Shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/"],
                     ["Ctrl", "Alt", " "]]
        y, x = 4, 0
        for row in self.rows:
            if y == 8:
                x += 1
            for label in row:
                button = QPushButton(label)
                button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                self.buttons.append(button)
                if label == "Shift":
                    grid.addWidget(button, y, x, 1, 2)
                    x += 2
                    continue
                if label == " ":
                    grid.addWidget(button, y, x, 1, 5)
                    continue
                grid.addWidget(button, y, x)
                x += 1
            x = 0
            y += 1

    def keyboardKeyPressEvent(self, event):
        key = event.text()
        for button in self.buttons:
            if button.text() == key:
                button.animateClick()
            if event.key() == Qt.Key.Key_Backspace and button.text() == "Backspace":
                self.emit_signal("backspace")
                button.animateClick()
                return
            if event.key() == Qt.Key.Key_Tab and button.text() == "Tab":
                self.emit_signal("Tab")
                button.animateClick()
                return
            if event.key() == Qt.Key.Key_Alt and button.text() == "Alt":
                button.animateClick()
            if event.key() == Qt.Key.Key_Shift and button.text() == "Shift":
                button.animateClick()
            if event.key() == Qt.Key.Key_Control and button.text() == "Ctrl":
                button.animateClick()
            if event.key() == Qt.Key.Key_CapsLock and button.text() == "Caps":
                button.animateClick()
            if event.key() == Qt.Key.Key_Return and button.text() == "Enter":
                button.animateClick()
        self.emit_signal(key)

    def emit_signal(self, text):
        self.signal.emit(text)
