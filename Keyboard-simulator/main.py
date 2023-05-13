import sys
import display_text
from PyQt6.QtWidgets import QApplication

# try:
#     from PyQt6.QtWidgets import QApplication
# except:

if __name__ == "__main__":
    app = QApplication(sys.argv)
    display_text = display_text.DisplayText()
    display_text.show()
    sys.exit(app.exec())