from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QVBoxLayout, QPushButton,
    QGridLayout, QHBoxLayout
)
from PySide6.QtCore import Qt


class electricityDialog(QDialog):
    def __init__(self, price, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Enter Electricity ID")
        self.setFixedSize(490, 370)

        self.current_input = ""
        self.price = price

        main_layout = QVBoxLayout()
        
        right_layout = QVBoxLayout()
       

        button_layout = QGridLayout()
        button_layout.setSpacing(0)
        button_layout.setContentsMargins(0, 0, 0, 0)

        # Create number buttons
        buttons = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2),
            "4": (1, 0), "5": (1, 1), "6": (1, 2),
            "7": (2, 0), "8": (2, 1), "9": (2, 2),
            "0": (3, 0, 1, 2)
        }

        for text, pos in buttons.items():
            btn = QPushButton(text)
            btn.setStyleSheet("background: grey;")
            btn.setFixedSize(150, 50)
            btn.clicked.connect(self.append_number)
            if len(pos) == 2:
                button_layout.addWidget(btn, *pos)
            else:
                button_layout.addWidget(btn, *pos)

        # Erase button
        erase_button = QPushButton("⌫")
        erase_button.setStyleSheet("background: red;")
        erase_button.setFixedSize(150, 50)
        erase_button.clicked.connect(self.erase_last_digit)
        button_layout.addWidget(erase_button, 3, 1)

       

        label = QLabel("Please enter electricity ID number to proceed with amount")
        label.setStyleSheet("padding: 5px; font-weight: bold; font-size: 13px;")
        right_layout.addWidget(label)

        self.id_label = QLineEdit()
        self.id_label.setStyleSheet("font-size: 30px;")
        self.id_label.setMinimumHeight(55)
        self.id_label.setReadOnly(True)
        right_layout.addWidget(self.id_label)

        main_layout.addLayout(right_layout, stretch=1)

        dialog_btns = QHBoxLayout()
        dialog_btns.setContentsMargins(0, 0, 0, 0)
        dialog_btns.setSpacing(2.5)
        dialog_btns.setAlignment(Qt.AlignRight)

        cancel_button = QPushButton("Cancel")
        cancel_button.setMaximumHeight(55)
        cancel_button.setMaximumWidth(100)
        cancel_button.setStyleSheet("padding: 10px; background: red; border-radius: 3px;")
        cancel_button.clicked.connect(self.handle_cancel)
        dialog_btns.addWidget(cancel_button)

        self.ok_button = QPushButton("OK")
        self.ok_button.setMaximumHeight(55)
        self.ok_button.setMaximumWidth(100)
        self.ok_button.setShortcut("Enter")
        self.ok_button.setStyleSheet("padding: 10px; border-radius: 3px; background: white; color: black;")
        self.ok_button.clicked.connect(self.handle_ok)
        dialog_btns.addWidget(self.ok_button)

        right_layout.addLayout(button_layout)
        main_layout.addLayout(dialog_btns)
        self.setLayout(main_layout)

    def handle_ok(self):
        self.current_input = self.id_label.text()
        self.confirm_selection()

    def handle_cancel(self):
        self.close()

    def append_number(self):
        number = self.sender().text()
        self.current_input += number
        self.update_list()

    def erase_last_digit(self):
        self.current_input = self.current_input[:-1]
        self.update_list()

    def update_list(self):
        self.id_label.setText(self.current_input)

    def confirm_selection(self):
        account_number = self.id_label.text()
        if account_number:
            price = self.price
            main_window = self.parent()
            item_name = f"Electricity"
            main_window.items.append((item_name, price))
            main_window.view.addItem(f"{item_name}: R{price:.2f}")
            main_window.total += price
            main_window.total_label.setText(f"Total: R{main_window.total:.2f}")
            self.accept()
        else:
            # QMessageBox.warning(self, "Input Error", "Please enter a valid account number.")
            print()
