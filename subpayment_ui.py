from PySide6.QtWidgets import (
    QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QStackedWidget, QWidget
)
from PySide6.QtCore import Qt, Signal
from functools import partial



class SubPaymentUi(QDialog):
    payment_accepted = Signal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Payment Options")
        self.setFixedSize(500, 300)
        
       


        self.check_selected = False
        self.saving_selected = False

        main_layout = QVBoxLayout(self)
        self.content = QStackedWidget()
        main_layout.addWidget(self.content)

        self.pages = {}
        self.pages["payment_option"] = self.create_payment_option_page()
        self.pages["payment_ui"] = self.create_payment_ui()

        for page in self.pages.values():
            self.content.addWidget(page)

        self.content.setCurrentWidget(self.pages["payment_option"])

        

    def create_payment_option_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        # layout.setAlignment(Qt.AlignVCenter)

        label = QLabel("Choose payment options")
        label.setStyleSheet("padding: 10px; font-size: 25px;")
        layout.addWidget(label)

        button_row_layout = QVBoxLayout()
        button_row_layout.setAlignment(Qt.AlignVCenter)
        close_btn_layout = QVBoxLayout()
        
        

        pay_btn = QPushButton("Pay")
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
        pay_btn.clicked.connect(partial(self.switch_page, "payment_ui"))
        # pay_btn.clicked.connect(self.emit_payment_and_continue)

        button_row_layout.addWidget(pay_btn)

        cash_btn = QPushButton("Cash")
        cash_btn.setMaximumHeight(55)
        cash_btn.clicked.connect(self.handle_pay)
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
        button_row_layout.addWidget(cash_btn)
        
        
        
        
        close_btn = QPushButton("Close")
        close_btn.setMaximumWidth(110)
        close_btn.setStyleSheet(
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
        close_btn.clicked.connect(self.handle_close_btn)
        close_btn_layout.addWidget(close_btn)
        

        layout.addLayout(button_row_layout)
        layout.addLayout(close_btn_layout)
        

        return page
    
    def handle_close_btn(self):
        self.close()
        
    def handle_pay(self):
        # ✅ This emits the signal to whoever is listening
        self.payment_accepted.emit()
        self.close()  # Optional: close dialog after clicking pay

    def create_payment_ui(self):
        page = QWidget()
        self.payment_layout = QVBoxLayout(page)

        label = QLabel("Select Account Type")
        label.setStyleSheet("font-size: 20px; padding: 10px;")
        self.payment_layout.addWidget(label)

        # Buttons for "Check" and "Saving"
        btn_row = QHBoxLayout()

        self.check_btn = QPushButton("Check")
        self.check_btn.setCheckable(True)
        self.check_btn.setStyleSheet("""
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
        self.check_btn.clicked.connect(self.toggle_check)
        btn_row.addWidget(self.check_btn)

        self.saving_btn = QPushButton("Saving")
        self.saving_btn.setCheckable(True)
        self.saving_btn.setStyleSheet("""
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
        self.saving_btn.clicked.connect(self.toggle_saving)
        btn_row.addWidget(self.saving_btn)

        self.payment_layout.addLayout(btn_row)

        # Status Label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("padding: 10px; color: green; font-weight: bold;")
        self.payment_layout.addWidget(self.status_label)

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
        back_btn.clicked.connect(partial(self.switch_page, "payment_option"))
        self.payment_layout.addWidget(back_btn)

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
            if page_name == "payment_ui":
                self.payment_accepted.emit()

    