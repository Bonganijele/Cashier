from PySide6.QtCore  import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from login.login_ui import LoginWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()

    app.exec()