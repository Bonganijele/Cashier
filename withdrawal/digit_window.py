from PySide6.QtWidgets import (
   QDialog,
   QLabel,
   QLineEdit,
   QVBoxLayout,
   QPushButton,
   QGridLayout,
   QDialogButtonBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class DigitWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("10 Digit Window")
        self.setFixedSize(500, 345)


        # self.setLayout()
        self.show()
        