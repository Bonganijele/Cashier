# from PySide6.QtWidgets import (
#     QDialog,
#     QLabel,
#     QVBoxLayout,
#     QPushButton,
#     QDialogButtonBox
# )
# from PySide6.QtCore import Qt
# from PySide6.QtGui import QFont

# class vochourDialog(QDialog):
#     def __init__(self, price, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Select Voucher Network")
#         self.setFixedSize(500, 345)

#         font = QFont()
#         font.setPointSize(15)

#         self.price = price

#         self.network_name = None  # To store the selected network name

#         vochour_layout = QVBoxLayout()
#         vochour_layout.setSpacing(1)
#         vochour_layout.setContentsMargins(0, 0, 0, 0)

#         vochour_label = QLabel("Select Network")
#         vochour_label.setFont(font)
#         vochour_layout.addWidget(vochour_label)


#         self.network_codes = {
#             "Mtn": "MTN-001",
#             "Vodacom": "VOD-002",
#             "Telcom": "TEL-003",
#             "Any network": "ANY-000"
#         }

#         for btn_text in self.network_codes.keys():
#             btn = QPushButton(btn_text)
#             btn.setStyleSheet("""
#                           QPushButton {
                              
#                               background: ghostwhite;
#                               color: black;
                              
#                           }
#                           QPushButton:hover {
#                              background: gray; 
                              
#                           }
                          
#                           """)
#             btn.setFixedHeight(60)

#             # Connect to a lambda that passes btn_text
#             btn.clicked.connect(lambda checked, name=btn_text: self.handle_selection(name))
#             vochour_layout.addWidget(btn)

#         dialog_btns = QDialogButtonBox(QDialogButtonBox.Cancel)
#         dialog_btns.setStyleSheet("padding: 10px; margin: 10px;")
#         dialog_btns.rejected.connect(self.reject)
#         vochour_layout.addWidget(dialog_btns)

#         self.setLayout(vochour_layout)

#     def handle_selection(self, network_name):
#         self.network_name = network_name
#         # code = self.network_codes.get(network_name, "Unknown Network")
#         # # self.network_code_label.setText(f"Network Code: {code}")
#         self.confirmed_selection()

#     def confirmed_selection(self):
#         if not self.network_name:
#             return

#         price = self.price
#         main_window = self.parent()

#         item_name = f"Voucher ({self.network_name})"
#         main_window.items.append((item_name, price))
#         main_window.view.addItem(f"{item_name}: R{price:.2f}")
#         main_window.total += price
#         main_window.total_label.setText(f"Total: R{main_window.total:.2f}")
#         self.accept()


from PySide6.QtWidgets import (
    QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QStackedWidget, QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from functools import partial

class vochourDialog(QDialog):
    def __init__(self, price, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Network Options")
        self.setFixedSize(560, 400)

        self.price = price
        
        self.check_selected = False
        self.saving_selected = False

        main_layout = QVBoxLayout(self)
        self.content = QStackedWidget()
        main_layout.addWidget(self.content)

        self.pages = {}
        self.pages["network_option"] = self.create_payment_option_page()
        self.pages["payment_ui"] = self.create_payment_ui()
        self.pages["vochour_ui"] = self.create_vochour_ui()

        for page in self.pages.values():
            self.content.addWidget(page)

        self.content.setCurrentWidget(self.pages["network_option"])

        

    def create_payment_option_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        layout.setAlignment(Qt.AlignVCenter)

        label = QLabel("Choose options")
        label.setStyleSheet("padding: 10px; font-size: 25px;")
        layout.addWidget(label)

        button_row_layout = QHBoxLayout()

        pay_btn = QPushButton("Airtime")
        pay_btn.setMaximumHeight(55)
        pay_btn.setStyleSheet("""
                          QPushButton {
                              
                              background: ghostwhite;
                              color: black;
                              padding: 15px;
                              border-radius: 5px;
                              
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
        
        pay_btn.clicked.connect(partial(self.switch_page, "payment_ui",))
        button_row_layout.addWidget(pay_btn)

        cash_btn = QPushButton("Vochour")
        cash_btn.setMaximumHeight(55)
        cash_btn.setStyleSheet("""
                          QPushButton {
                              
                              background: ghostwhite;
                              color: black;
                              padding: 15px;
                              border-radius: 5px;
                              
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
        # Connect if needed
        cash_btn.clicked.connect(partial(self.switch_page, "vochour_ui"))
        button_row_layout.addWidget(cash_btn)

        layout.addLayout(button_row_layout)

        return page
    
    

    def create_payment_ui(self):
        page = QWidget()
        self.payment_layout = QVBoxLayout(page)
        self.payment_layout.setSpacing(1)
        self.payment_layout.setContentsMargins(0, 0, 0, 0)
        
        

        
        font = QFont()
        font.setPointSize(15)
        
        

        vochour_label = QLabel("Select Network")
        vochour_label.setFont(font)
        self.payment_layout.addWidget(vochour_label)


        self.network_codes = {
            "Mtn": "MTN-001",
            "Vodacom": "VOD-002",
            "Telcom": "TEL-003",
            "Any network": "ANY-000"
        }

        for btn_text in self.network_codes.keys():
            btn = QPushButton(btn_text)
            btn.setStyleSheet("""
                          QPushButton {
                              
                              background: ghostwhite;
                              color: black;
                              
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
            btn.setFixedHeight(60)

            # Connect to a lambda that passes btn_text
            btn.clicked.connect(lambda checked, name=btn_text: self.handle_selection(name))
            self.payment_layout.addWidget(btn)
            
            

        
    
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
        back_btn.clicked.connect(partial(self.switch_page, "network_option"))
        self.payment_layout.addWidget(back_btn)
        
        

        return page


    def create_vochour_ui(self):
        page = QWidget()
        ui_layout = QVBoxLayout(page)
        
        font = QFont()
        font.setPointSize(15)
        
        label = QLabel("Select Vochour Network")
        label.setFont(font)
        ui_layout.addWidget(label)
        
        
        
        self.network_codes = {
            "HollyWood": "HollyWood-001",
            "BetXchange": "BetXchange-002",
            "Any network vochour": "ANY-000"
        }

        for btn_text in self.network_codes.keys():
            btn = QPushButton(btn_text)
            btn.setStyleSheet("""
                          QPushButton {
                              
                              background: ghostwhite;
                              color: black;
                              
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
            btn.setFixedHeight(60)

            # Connect to a lambda that passes btn_text
            btn.clicked.connect(lambda checked, name=btn_text: self.handle_vochor_selection(name))
            ui_layout.addWidget(btn)
            
            
        
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
        back_btn.clicked.connect(partial(self.switch_page, "network_option"))
        ui_layout.addWidget(back_btn)
        
        
        return page
         


    def toggle_check(self):
        self.check_selected = not self.check_selected
        self.check_btn.setChecked(self.check_selected)
        self.update_card_machine_status()

    def toggle_saving(self):
        self.saving_selected = not self.saving_selected
        self.saving_btn.setChecked(self.saving_selected)
        self.update_card_machine_status()

    def update_card_machine_status(self):
        if self.check_selected and self.saving_selected:
            self.status_label.setText("Card Machine Selected")
        else:
            self.status_label.setText("")

    def switch_page(self, page_name):
        if page_name in self.pages:
            self.content.setCurrentWidget(self.pages[page_name])

    def handle_selection(self, network_name):
        self.network_name = network_name
        # code = self.network_codes.get(network_name, "Unknown Network")
        # # self.network_code_label.setText(f"Network Code: {code}")
        self.confirmed_selection()

    def confirmed_selection(self):
        if not self.network_name:
            return

        price = self.price
        main_window = self.parent()

        item_name = f"Airtime ({self.network_name})"
        main_window.items.append((item_name, price))
        main_window.view.addItem(f"{item_name}: R{price:.2f}")
        main_window.total += price
        main_window.grant_total_label.setText(f"Total: R{main_window.total:.2f}")
        self.accept()
    
    def confirmed_selection(self):
        if not self.network_name:
            return

        price = self.price
        main_window = self.parent()

        item_name = f"Airtime ({self.network_name})"
        
        # Update the dictionary with the item name as key and price as value
        if item_name in main_window.items:
            # If the item is already in the dictionary, update the price or quantity
            main_window.items[item_name] += price  # This adds the price to the existing entry
        else:
            # If the item doesn't exist, add it with the price
            main_window.items[item_name] = price
        
        # Add the item to the list view
        main_window.view.addItem(f"{item_name}: R{main_window.items[item_name]:.2f}")
        
        # Update the total
        main_window.total += price
        main_window.grant_total_label.setText(f"Total: R{main_window.total:.2f}")
        
        self.accept()


    def handle_vochor_selection(self, vochour_name):
        self.vochour_name = vochour_name
        self.confirmed_vochour_selection()

    def confirmed_vochour_selection(self):
        if not self.vochour_name:
            return

        price = self.price
        main_window = self.parent()

        item_name = f"Vochour ({self.vochour_name})"
        
        # Update the dictionary with the item name as key and price as value
        if item_name in main_window.items:
            # If the item is already in the dictionary, update the price or quantity
            main_window.items[item_name] += price  # This adds the price to the existing entry
        else:
            # If the item doesn't exist, add it with the price
            main_window.items[item_name] = price
        
        # Add the item to the list view
        main_window.view.addItem(f"{item_name}: R{main_window.items[item_name]:.2f}")
        
        # Update the total
        main_window.total += price
        main_window.grant_total_label.setText(f"Total: R{main_window.total:.2f}")
        
        self.accept()

            
            
        