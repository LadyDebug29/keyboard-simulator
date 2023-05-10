import sys
import keyboard
import display_text
from PyQt6.QtWidgets import QApplication

def close_all_windows():
    app.closeAllWindows()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    keyboard = keyboard.Keyboard()
    display_text = display_text.DisplayText()
    keyboard.signal.connect(display_text.line_edit)

    keyboard.show()
    display_text.show()
    keyboard.activateWindow()
    sys.exit(app.exec())