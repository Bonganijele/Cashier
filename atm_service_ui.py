from PySide6.QtWidgets import (
    QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout,
    QStackedWidget, QWidget
)
from PySide6.QtGui import QFont
from functools import partial


class AtmServiceUi(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ATM Services")
        self.setFixedSize(500, 345)

        atm_layout = QVBoxLayout(self)

        self.content = QStackedWidget()
        atm_layout.addWidget(self.content)

        self.pages = {
            "atm_service_ui": self.create_main_menu(),
            "bank_selection_ui": self.create_bank_selection(),
            "method_selection_ui": self.create_method_selection()
        }

        for page in self.pages.values():
            self.content.addWidget(page)

        self.content.setCurrentWidget(self.pages["atm_service_ui"])

    def hanlde_close(self):
        self.close()

    def create_main_menu(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        title = QLabel("Select Service")
        font = QFont()
        font.setPointSize(15)
        title.setFont(font)
        layout.addWidget(title)

        for btn_label in ["E-Wallet", "Cash Send"]:
            btn = QPushButton(btn_label)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: ghostwhite;
                    color: black;
                    font-style: Arial;
                }
                QPushButton:hover {
                    background: gray;
                }
            """)
            btn.setFixedHeight(60)
            btn.clicked.connect(partial(self.switch_page, "bank_selection_ui"))
            layout.addWidget(btn)

        close_btn = QPushButton("Close")
        close_btn.setMaximumWidth(110)
        close_btn.setStyleSheet("""
            QPushButton {
                padding: 14px;
                margin: 10px;
                background: darkred;
            }
            QPushButton:hover {
                background: red;
            }
        """)
        close_btn.clicked.connect(self.hanlde_close)
        layout.addWidget(close_btn)

        return page

    def create_bank_selection(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        label = QLabel("Select Bank")
        label.setStyleSheet("padding: 12px; font-size: 15px;")
        layout.addWidget(label)

        banks = ["FNB", "Capitec", "ABSA", "Standard Bank", "Nedbank"]
        for bank in banks:
            btn = QPushButton(bank)
            btn.setFixedHeight(50)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: ghostwhite;
                    color: black;
                }
                QPushButton:hover {
                    background-color: gray;
                }
            """)
            btn.clicked.connect(partial(self.switch_page, "method_selection_ui"))
            layout.addWidget(btn)

        back_btn = QPushButton("Back")
        back_btn.setMaximumWidth(110)
        back_btn.setStyleSheet("""
            QPushButton {
                padding: 14px;
                margin: 10px;
                background: darkred;
            }
            QPushButton:hover {
                background: red;
            }
        """)
        back_btn.clicked.connect(partial(self.switch_page, "atm_service_ui"))
        layout.addWidget(back_btn)

        return page

    def create_method_selection(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        label = QLabel("Select withdrawal method")
        label.setStyleSheet("padding: 12px; font-size: 15px;")
        layout.addWidget(label)

        btns_layout = QHBoxLayout()
        for method in ["ID Method", "Card Method"]:
            btn = QPushButton(method)
            btn.setMaximumHeight(55)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: ghostwhite;
                    color: black;
                }
                QPushButton:hover {
                    background-color: gray;
                }
            """)
            btns_layout.addWidget(btn)

        layout.addLayout(btns_layout)

        back_btn = QPushButton("Back")
        back_btn.setMaximumWidth(110)
        back_btn.setStyleSheet("""
            QPushButton {
                padding: 14px;
                margin: 10px;
                background: darkred;
            }
            QPushButton:hover {
                background: red;
            }
        """)
        back_btn.clicked.connect(partial(self.switch_page, "bank_selection_ui"))
        layout.addWidget(back_btn)

        return page

    def switch_page(self, page_name):
        if page_name in self.pages:
            self.content.setCurrentWidget(self.pages[page_name])
