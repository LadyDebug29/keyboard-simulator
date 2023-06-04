from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, \
    QLineEdit, QWidget, QPushButton, QGridLayout
import sys
import display_text


class Keyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet('background-color: white;')

        grid = QGridLayout()
        self.setLayout(grid)

        self.buttons = []
        self.rows = [["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "Backspace"],
                     ["Tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\"],
                     ["Caps", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "Enter"],
                     ["Shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/"],
                     ["Ctrl", "Alt", " "]]

        y, x = 0, 0
        for row in self.rows:
            for label in row:
                button = QPushButton(label)
                button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                self.buttons.append(button)
                grid.addWidget(button, y, x)
                x += 1
            x = 0
            y += 1

        self.move(200, 500)

    def keyPressEvent(self, event):
        key = event.text()
        for button in self.buttons:
            if button.text() == key:
                button.animateClick()
            if event.key() == Qt.Key.Key_Backspace and button.text() == "Backspace":
                button.animateClick()
            if event.key() == Qt.Key.Key_Tab and button.text() == "Tab":
                button.animateClick()
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    keyboard = Keyboard()
    keyboard.show()
    sys.exit(app.exec())
