import subprocess
import main_screen
import sys

if __name__ == "__main__":
    subprocess.run(['pip', 'install', 'requests'])
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main_screen = main_screen.MainScreen()
    main_screen.show()
    sys.exit(app.exec())
