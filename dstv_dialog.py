from PySide6.QtWidgets import (
   QDialog,
   QLabel,
   QLineEdit,
   QVBoxLayout,
   QPushButton,
   QGridLayout,
   QDialogButtonBox,
   QMessageBox,
   QListWidget,
   QHBoxLayout
   
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont



class dstvDialog(QDialog):
    def __init__(self, price, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Dstv Service")
        self.setFixedSize(500, 390)

        self.current_input = ""
        self.customer_id = []
        
        self.price = price
        
        button_layout = QGridLayout()
        button_layout.setSpacing(0)
        button_layout.setContentsMargins(0,0, 0, 0)
        
        
        main_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        
        buttons = {
                "1": (0, 0), "2": (0, 1), "3": (0, 2),
                "4": (1, 0), "5": (1, 1), "6": (1, 2),
                "7": (2, 0), "8": (2, 1), "9": (2, 2),
                "0": (3, 0, 1, 3)
            }

        for text, pos in buttons.items():
                btn = QPushButton(text)
                # btn.clicked.connect()
                btn.setStyleSheet("background:  grey;")
                btn.setFixedSize(150, 50)
                btn.clicked.connect(self.append_number)
                if len(pos) == 2:
                    button_layout.addWidget(btn, *pos)
                else:
                    button_layout.addWidget(btn, *pos)

            # Erase button (removes the last number)
        erase_button = QPushButton("⌫")
        erase_button.setStyleSheet("background: red ;")
        erase_button.setFixedSize(130, 50)
        erase_button.clicked.connect(self.erase_last_digit)
        button_layout.addWidget(erase_button, 3, 1)
        
        
        
        label = QLabel("Please enter customer id number to proceed further with amount")
        label.setStyleSheet("padding: 5px; font-weight: bold; font-size: 13px;")
        right_layout.addWidget(label)
        

        self.id_label = QLineEdit()
        self.id_label.setPlaceholderText("Enter Customer ID")
        self.id_label.setReadOnly(True)
        self.id_label.setMaximumHeight(55)
        right_layout.addWidget(self.id_label)
        
        
        right_layout.addLayout(button_layout)
        main_layout.addLayout(right_layout, stretch=1)
        # funeral_covers.setLayout(grid_layout)
        
        dialog_btns = QHBoxLayout()
        dialog_btns.setContentsMargins(0,0,0,0)
        dialog_btns.setSpacing(0)
        dialog_btns.setAlignment(Qt.AlignJustify | Qt.AlignRight)
        
        
        cancel_button = QPushButton("Cencel")
        cancel_button.setMaximumWidth(110)
        cancel_button.setStyleSheet(
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
        cancel_button.setMaximumWidth(100)
        cancel_button.clicked.connect(self.handle_cancel)
        dialog_btns.addWidget(cancel_button)
        
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
        ok_button.clicked.connect(self.handle_ok)
        dialog_btns.addWidget(ok_button)
        
        
        main_layout.addLayout(dialog_btns)
        
            
        self.setLayout(main_layout)    
        
    
    def handle_ok(self):
       self.confirm_selection() 
    
    def handle_cancel(self):
        self.reject()
    
    def append_number(self):
        sender = self.sender()
        self.self_current_txt = self.id_label.text()
        self.id_label.setText(self.self_current_txt + sender.text())
        
        
        
    def update_list(self):
       self.id_label.setText(self.current)
        
    
    def erase_last_digit(self):
        self.current = self.id_label.text()
        self.id_label.setText(self.current[:-1])
        
    
    def confirm_selection(self):
        funeral_id = self.id_label.text()
        if funeral_id:
            # Assume parent is the main window with .items, .view, .total
            main_window = self.parent()
            item_name = f"Dstv :"
            # item_name = f"Dstv ID: {funeral_id}"
            main_window.items.append((item_name, self.price))
            main_window.view.addItem(f"{item_name}: R{self.price:.2f}")
            main_window.total += self.price
            main_window.total_label.setText(f"Total: R{main_window.total:.2f}")
            self.accept()
        else:
            print("Please enter a valid Funeral ID.")   
  
    