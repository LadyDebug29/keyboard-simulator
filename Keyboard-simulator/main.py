import sys
import display_text

try:
    from PyQt6.QtWidgets import QApplication
except ImportError:
    import subprocess
    subprocess.check_call(["pip", "install", "PyQt6"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    display_text = display_text.DisplayText()
    display_text.show()
    sys.exit(app.exec())