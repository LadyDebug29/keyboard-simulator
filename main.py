import subprocess
import main_screen
import sys

if __name__ == "__main__":
    try:
        from PyQt6.QtWidgets import QApplication
    except ImportError:
        subprocess.run(["pip", "install", "-r", "requirements.txt"])

    app = QApplication(sys.argv)
    main_screen = main_screen.MainScreen()
    main_screen.show()
    sys.exit(app.exec())
