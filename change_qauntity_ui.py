from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QVBoxLayout, QPushButton,
    QGridLayout, QHBoxLayout
)
from PySide6.QtCore import Qt


class ChangeQuantity(QDialog):
    def __init__(self,  parent=None):
        super().__init__(parent)

        self.setWindowTitle("Enter quantity")
        self.setFixedSize(300, 370)

        # self.current_input = ""
        # self.price = price

        main_layout = QVBoxLayout(self)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(40)
        self.display.setStyleSheet("font-size: 18px; padding: 8px;")
        main_layout.addWidget(self.display)

        button_layout = QGridLayout()
        button_layout.setSpacing(1)

        # Create number buttons
        buttons = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2),
            "4": (1, 0), "5": (1, 1), "6": (1, 2),
            "7": (2, 0), "8": (2, 1), "9": (2, 2),
            "0": (3, 0, 1, 2)
        }

        for text, pos in buttons.items():
            btn = QPushButton(text)
            btn.setStyleSheet("background-color: grey; font-size: 16px;")
            btn.setFixedSize(100, 50)
            btn.clicked.connect(lambda checked, num=text: self.append_number(num))
            if len(pos) == 2:
                button_layout.addWidget(btn, *pos)
            else:
                button_layout.addWidget(btn, *pos)

        # Delete button
        del_btn = QPushButton("Del")
        del_btn.setStyleSheet("background-color: darkred; color: white;")
        del_btn.setFixedSize(100, 50)
        del_btn.clicked.connect(self.delete_last)
        button_layout.addWidget(del_btn, 3, 2)

        # Clear button
        clear_btn = QPushButton("Clear")
        clear_btn.setStyleSheet("background-color: orange; color: black;")
        clear_btn.setFixedHeight(40)
        clear_btn.clicked.connect(self.clear_input)
        main_layout.addWidget(clear_btn)

        main_layout.addLayout(button_layout)

        # Confirm button
        # confirm_btn = QPushButton(f"Confirm Purchase - R{self.price}")
        # confirm_btn.setStyleSheet("background-color: green; color: white; font-size: 16px;")
        # confirm_btn.setFixedHeight(45)
        # confirm_btn.clicked.connect(self.confirm)
        # main_layout.addWidget(confirm_btn)

    def append_number(self, number):
        self.current_input += number
        self.display.setText(self.current_input)

    def delete_last(self):
        self.current_input = self.current_input[:-1]
        self.display.setText(self.current_input)

    def clear_input(self):
        self.current_input = ""
        self.display.setText("")

    def confirm(self):
        # You can handle the confirmation logic here
        print(f"Purchasing electricity with ID: {self.current_input} and amount: R{self.price}")
        self.accept()
