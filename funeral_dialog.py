from PySide6.QtWidgets import (
    QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout,
    QStackedWidget, QWidget, QLineEdit, QGridLayout
)
from PySide6.QtCore import Qt
from functools import partial


class FuneralCoverDialog(QDialog):
    def __init__(self, price, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Funeral Cover Services")
        self.setFixedSize(500, 430)

        self.selected_provider = ""
        self.price = price  # Store the price passed from the main window
        self.pages = {}

        main_layout = QVBoxLayout(self)
        self.content = QStackedWidget()
        main_layout.addWidget(self.content)

        # Pages
        self.pages["select_provider"] = self.create_provider_selection_page()
        self.pages["enter_details"] = self.create_details_entry_page()

        for page in self.pages.values():
            self.content.addWidget(page)

        self.content.setCurrentWidget(self.pages["select_provider"])

    def create_provider_selection_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
       

        label = QLabel("Funeral Cover Provider")
        label.setStyleSheet("font-size: 24px; padding: 10px;")
        layout.addWidget(label)

        providers = ["SFS", "Avbob", "CliteLife", "JD"]
        column = QVBoxLayout()
        column.setContentsMargins(0,0,0,0)
        column.setSpacing(2)
        for provider in providers:
            btn = QPushButton(provider)
            btn.setStyleSheet("""
                          QPushButton {
                              
                              background: white;
                              border-radius: 5px;
                              
                              color: black;
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
            
            btn.setFixedHeight(60)
        
            btn.clicked.connect(partial(self.switch_to_details_page, provider))
            column.addWidget(btn)
            
            cancel_btn = QPushButton("Cancel")
            cancel_btn.setStyleSheet(
            """
            QPushButton {
                padding: 14px;
                margin: 10px;
                background: darkred;
                
            }
            QPushButton:hover {
                background: red;
                
            }
            
            """
        )
            cancel_btn.setMaximumWidth(110)
        

        layout.addLayout(column)
        layout.addWidget(cancel_btn)
        return page

    def create_details_entry_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignTop)

        # Provider label
        self.provider_label = QLabel("Provider: ")
        self.provider_label.setStyleSheet("font-size: 18px; padding: 10px;")
        layout.addWidget(self.provider_label)

        # Funeral ID input
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter Funeral ID")
        self.id_input.setReadOnly(True)
        self.id_input.setStyleSheet("padding: 10px; font-size: 16px;")
        layout.addWidget(self.id_input)

        # Price Label
        self.price_label = QLabel(f"Price: R{self.price}")
        self.price_label.setStyleSheet("font-size: 18px; padding: 10px; color: green;")
        layout.addWidget(self.price_label)

        # Number pad layout
        button_layout = QGridLayout()
        button_layout.setSpacing(2)
        button_layout.setContentsMargins(0, 0, 0, 0)

        buttons = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2),
            "4": (1, 0), "5": (1, 1), "6": (1, 2),
            "7": (2, 0), "8": (2, 1), "9": (2, 2),
            "0": (3, 0, 1, 3)
        }

        for text, pos in buttons.items():
            btn = QPushButton(text)
            btn.setStyleSheet("background: grey; font-size: 18px;")
            btn.setFixedSize(150, 50)
            btn.clicked.connect(self.append_number_to_id)
            button_layout.addWidget(btn, *pos)

        erase_button = QPushButton("⌫")
        erase_button.setStyleSheet("background: red; font-size: 18px;")
        erase_button.setFixedSize(130, 50)
        erase_button.clicked.connect(self.erase_last_id_digit)
        button_layout.addWidget(erase_button, 3, 1)

        layout.addLayout(button_layout)
        
        btn_layout = QHBoxLayout()
        btn_layout.setAlignment(Qt.AlignRight)

        
      

        # Back button
        back_btn = QPushButton("Back")
        back_btn.setMaximumWidth(110)
        back_btn.setStyleSheet(
            """
            QPushButton {
                padding: 14px;
                margin: 10px;
                background: darkred;
                
                
            }
            QPushButton:hover {
                background: red;
                
            }
            
            """
        )
        back_btn.clicked.connect(partial(self.switch_page, "select_provider"))
        btn_layout.addWidget(back_btn)
        
        
        # OK Button
        ok_button = QPushButton("OK")
        ok_button.setMaximumWidth(110)
        ok_button.setStyleSheet(
            """
            QPushButton {
                padding: 14px;
                margin: 10px;
                background: white;
                color: black;
                
            }
            QPushButton:hover {
                background: gray;
                
            }
            
            """
        )
        ok_button.clicked.connect(self.confirm_selection)
        btn_layout.addWidget(ok_button)
        
        
        layout.addLayout(btn_layout)

        return page

    def append_number_to_id(self):
        sender = self.sender()
        self.current = self.id_input.text()
        self.id_input.setText(self.current + sender.text())

    def erase_last_id_digit(self):
        self.current = self.id_input.text()
        self.id_input.setText(self.current[:-1])

    def switch_to_details_page(self, provider):
        self.selected_provider = provider
        self.provider_label.setText(f"Provider: {provider}")
        self.id_input.clear()
        self.switch_page("enter_details")
   
    def update_list(self):
        self.id_input.setText(self.current)

    def confirm_selection(self):
        funeral_id = self.id_input.text()
        if funeral_id:
            # Assume parent is the main window with .items, .view, .total
            main_window = self.parent()
            item_name = f"Funeral ID: {funeral_id}"
            main_window.items.append((item_name, self.price))
            main_window.view.addItem(f"{item_name}: R{self.price:.2f}")
            main_window.total += self.price
            main_window.total_label.setText(f"Total: R{main_window.total:.2f}")
            self.accept()
        else:
            print("Please enter a valid Funeral ID.")

    def switch_page(self, page_name):
        if page_name in self.pages:
            self.content.setCurrentWidget(self.pages[page_name])
