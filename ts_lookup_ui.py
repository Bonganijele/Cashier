
from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QVBoxLayout, QPushButton, QGridLayout,
    QDialogButtonBox, QStackedWidget, QWidget, QHBoxLayout, QListWidget,
    QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class TsLookUpUi(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ts Lookup")
        self.setFixedSize(600, 450)

        # Main layout
        main_layout = QVBoxLayout(self)

        # Top layout for category buttons and product list
        top_layout = QHBoxLayout()

        # Grid layout for category buttons
        ts_look_up_layout = QGridLayout()
        ts_look_up_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        ts_look_up_layout.setContentsMargins(5, 5, 5, 5)

        # Create buttons
        for i, ts_btn in enumerate(["Home", "Snacks", "Drinks", "Liqour", "Food", "Barthing", "Toys"]):
            btn = QPushButton(ts_btn)
            btn.setStyleSheet("""
                QPushButton {
                    background: orange;
                    color: ghostwhite;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background: darkorange;
                }
            """)
            btn.setFixedSize(120, 50)
            if ts_btn == "Snacks":
                btn.clicked.connect(self.handle_snacks)

            ts_look_up_layout.addWidget(btn, i, 0)

        # Product list
        self.lst = QListWidget()
        self.lst.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lst.setMinimumHeight(300)

        # Add both button grid and list to top layout
        top_layout.addLayout(ts_look_up_layout)
        top_layout.addWidget(self.lst)

        # Add to main layout
        main_layout.addLayout(top_layout)

        # Close button
        close_btn = QPushButton("Close")
        close_btn.setFixedSize(120, 40)
        close_btn.clicked.connect(self.close)
        main_layout.addWidget(close_btn, alignment=Qt.AlignRight)

    def handle_snacks(self):
        snacks = "Dorritos"
        self.lst.addItem(snacks)
        print("Listed Snacks Items:")
