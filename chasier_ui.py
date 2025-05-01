
import sys
import cv2
from pyzbar.pyzbar import decode
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QListWidget, QListWidgetItem, QHBoxLayout, QGridLayout, QSizePolicy, QSpacerItem, QTableWidget
)
from PySide6.QtCore import Qt, QThread, Signal, QSize, QTimer
from PySide6.QtGui import QFont, QIcon
from datetime import datetime


from change_qauntity_ui import ChangeQuantity
from electricity_dialog import electricityDialog
from options.option_iu import OptionUi
from search_page_ui import SearchWidget
from setting_ui import SettingUi
from vochour_dailog import vochourDialog
from funeral_dialog import FuneralCoverDialog
from dstv_dialog import dstvDialog
from subpayment_ui import SubPaymentUi
from atm_service_ui import AtmServiceUi
from ts_lookup_ui import TsLookUpUi

# Product database
PRODUCTS = {
    "P123": {"name": "Milk 500ml", "price": 12.50},
    "900961702092": {"name": "Xbox Console", "price": 1000},
    "8718114642871": {"name": "Vaseline 20g", "price": 30.00},
    "6001087005654": {"name": "Vaseline BlueSeal 250ml", "price": 34.99},
    # "6001299016608": {"name": "Tropica Mango 500ml", "price": 16.99},
}

# Barcode scanner thread
import time

class BarcodeScanner(QThread):
    product_scanned = Signal(str, float)
    scanner_status = Signal(str)

    def __init__(self):
        super().__init__()
        self._running = True

    def run(self):
        self.scanner_status.emit("🟡 Starting scanner...")
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            self.scanner_status.emit("🔴 Camera not found.")
            return

        self.scanner_status.emit("🟢 Scanner running. Hold barcode up to camera.")
        scanned_ids = set()

        # # Set camera resolution (optional: reduce resolution for better performance)
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 440)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 380)

        # Initialize a variable to track frame processing
        last_processed_time = time.time()

        while self._running:
            ret, frame = cap.read()
            if not ret:
                continue

            # Process frame only if enough time has passed (to reduce processing load)
            current_time = time.time()
            if current_time - last_processed_time < 0.1:  # Process every 100ms (10 FPS)
                continue

            last_processed_time = current_time

            # Decode the barcode in the frame
            for barcode in decode(frame):
                code_data = barcode.data.decode("utf-8")
                print("Scanned barcode:", code_data)
                if code_data in PRODUCTS and code_data not in scanned_ids:
                    product = PRODUCTS[code_data]
                    self.product_scanned.emit(product['name'], product['price'])
                    scanned_ids.add(code_data)

            # Optional: Add a small delay to avoid overloading the CPU
            # cv2.imshow("Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        cap.release()
        self.scanner_status.emit("⚪ Scanner stopped.")

    def stop(self):
        self._running = False
        self.wait()

# Main UI
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cashier")
        self.resize(1200, 600)

        self.items = {}  # Store items and their quantities
        self.total = 0.0  # Running total
        
        self.tax_rate = 0.15
        self.current_price = "0.00"  # Current price being entered

        # Main horizontal layout
        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Left layout: Item List + Total + Inputs
        left_layout = QVBoxLayout()
        left_layout.setSpacing(5)
        left_layout.setContentsMargins(0, 0, 0, 0)

        font = QFont()
        font.setPointSize(40)

        self.label = QLabel('Cashier')
        self.label.setFont(font)
        self.label.setStyleSheet('padding: 8px;')
        left_layout.addWidget(self.label)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
       
        
        logged_in_user = QLabel("Active Cashier: SIYABONGA NKOSI")
        logged_in_user.setStyleSheet("font-size: 24px; padding: 8px;")
        left_layout.addWidget(logged_in_user)

        date_display = datetime.today().strftime("%Y-%m-%d / %A")
        time_display = datetime.now()
        
        
        

        self.time_label = QLabel(self)
        self.time_label.setText(time_display.strftime("%H:%M:%S"))
        self.time_label.setStyleSheet("font-style: Arial; font-size: 20px; margin: 6px;")
        left_layout.addWidget(self.time_label)

        date = QLabel(f"{date_display}")
        date.setStyleSheet("font-style: Arial; font-size: 14px; margin: 6px;")
        left_layout.addWidget(date)

        # List to show items and prices
        self.view = QListWidget()
        self.view.setStyleSheet("""
                                
                                QListWidget {
                                    font-size: 30px;
                                    padding: 8px;
                                }
                                """)
        self.view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        left_layout.addWidget(self.view)
        

        
        this_btn_layout = QHBoxLayout()
        this_btn_layout.setAlignment(Qt.AlignJustify | Qt.AlignCenter )
        
       

        
        btn = QPushButton("Delete Item")
        btn.setStyleSheet("""
                          QPushButton {
                              background: darkred;
                              border-radius: 5px;
                              
                              }
                              QPushButton:hover {
                              background: red;
                              
                              }
                              
                              """)
        btn.clicked.connect(self.delete_item)
        btn.setFixedSize(130, 50)
        this_btn_layout.addWidget(btn)
        
        
        btn = QPushButton("Discout")
        btn.setStyleSheet("""
                          QPushButton {
                              background: green;
                               border-radius: 5px;
                              
                              }
                              QPushButton:hover {
                              background: darkgreen;
                              
                              }
                              
                              """)
        btn.setFixedSize(130, 50)
        
        this_btn_layout.addWidget(btn)
        
        btn = QPushButton("Quant\n Change")
        btn.setStyleSheet("""
                          QPushButton {
                              background: darkgray;
                               border-radius: 5px;
                              
                              }
                              QPushButton:hover {
                              background: gray;
                              
                              }
                              
                              """)
        btn.setFixedSize(130, 50)
        btn.clicked.connect(self.change_qaunt_ui)
        this_btn_layout.addWidget(btn)
        
        btn = QPushButton("Price\n Change")
        btn.setStyleSheet("""
                          QPushButton {
                              background: darkgray;
                               border-radius: 5px;
                              
                              }
                              QPushButton:hover {
                              background: gray;
                              
                              }
                              
                              """)
        btn.setFixedSize(130, 50)
        this_btn_layout.addWidget(btn)
        
        
    
        left_layout.addLayout(this_btn_layout)
        
        
        
        self.sub_total = QLabel("Sub Total: R0")
        self.sub_total.setStyleSheet("font-size: 30px; background: #333;")
        left_layout.addWidget(self.sub_total)
        
        self.tax_amount_label = QLabel("Tax (15%): 0")
        self.tax_amount_label.setStyleSheet("font-size: 30px; background: #333;")
        left_layout.addWidget(self.tax_amount_label)

        # Total price label
        self.grant_total_label = QLabel("Grand Total: R0.00")
        self.grant_total_label.setStyleSheet("font-size: 35px; background: #333;")
        left_layout.addWidget(self.grant_total_label)

        # Add left layout to main layout
        main_layout.addLayout(left_layout, stretch=2)



        # Right layout: Button Grid
        right_layout = QVBoxLayout()
        right_layout.setSpacing(2)
        right_layout.setContentsMargins(0, 0, 0, 0)


        price_button_layout = QHBoxLayout()
        price_button_layout.setAlignment(Qt.AlignRight | Qt.AlignHCenter)
        
        amount_label = QLabel("R")
        amount_label.setFont(font)
        # amount_label.setStyleSheet("")
       
        price_button_layout.addWidget(amount_label)
        
        # Price display label (as a simple button text showing current price)
        self.price_button = QPushButton(f"0.00")
        self.price_button.setStyleSheet("background: transparent; border: none")
        self.price_button.setFont(QFont("Arial", 30))  # Large font for price
        self.price_button.setEnabled(False)  # Make it unclickable
        price_button_layout.addWidget(self.price_button)
        
        
        

        # Grid layout for number buttons
        button_layout = QGridLayout()
        button_layout.setSpacing(5)
        button_layout.setAlignment(Qt.AlignJustify | Qt.AlignCenter)
        button_layout.setContentsMargins(0, 0, 0, 0)

        buttons = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2),
            "4": (1, 0), "5": (1, 1), "6": (1, 2),
            "7": (2, 0), "8": (2, 1), "9": (2, 2),
            "0": (3, 0, 1, 2)
        }

        for text, pos in buttons.items():
            btn = QPushButton(text)
            btn.setStyleSheet("""
                              QPushButton {
                                  background-color: white;
                                  font-size: 17px;
                                  font-style: arial;
                                  color : grey;
                                 
                                  
                              }
                              QPushButton:hover {
                                  background-color: gray;
                                
                                  
                              }
                              
                              
                              """)
            btn.setFixedSize(100, 100)
            btn.clicked.connect(self.append_number)
            if len(pos) == 2:
                button_layout.addWidget(btn, *pos)
            else:
                button_layout.addWidget(btn, *pos)

        # Erase button (removes the last number)
        erase_button = QPushButton("⌫")
        erase_button.setStyleSheet("""
                                   QPushButton {
                                       background: darkred;
                                       color: grey;
                                   }
                                   QPushButton:hover {
                                       background: red; 
                                   }
                                   """)
        erase_button.setFixedSize(100, 100)
        erase_button.clicked.connect(self.erase_last_digit)
        button_layout.addWidget(erase_button, 3, 1)  # Place it in the bottom-right

        

        
        setting_btn = QPushButton("Options")
        setting_btn.clicked.connect(self.open_option_ui)
        setting_btn.setStyleSheet("""
                          QPushButton {
                              
                              background: ghostwhite;
                              color: darkgray;
                              padding: 15px;
                              border-radius: 5px;
                              
                          }
                          QPushButton:hover {
                             background-color: grey; 
                              
                          }
                          
                          """)
        setting_btn.setFixedSize(130, 50)
        
        
        help_btn = QPushButton("Help")
        help_btn.setStyleSheet("""
                          QPushButton {
                              
                              background: ghostwhite;
                              color: darkgray;
                              padding: 15px;
                              border-radius: 5px;
                              
                          }
                          QPushButton:hover {
                             background-color: grey; 
                              
                          }
                          
                          """)
        help_btn.setFixedSize(130, 50)
        
        
        search_btn = QPushButton("Search Item")
        search_btn.setStyleSheet("""
                          QPushButton {
                              
                              background: ghostwhite;
                              color: darkgray;
                              padding: 15px;
                              border-radius: 5px;
                              
                          }
                          QPushButton:hover {
                             background-color: grey; 
                              
                          }
                          
                          """)
        search_btn.clicked.connect(self.search_page_ui)
        search_btn.setFixedSize(130, 50)
        
        
         
        ts_lookup_btn = QPushButton("TS Lookup")
        ts_lookup_btn.setStyleSheet("""
                          QPushButton {
                              
                              background: ghostwhite;
                              color: darkgray;
                              padding: 15px;
                              border-radius: 5px;
                              
                          }
                          QPushButton:hover {
                             background-color: grey; 
                              
                          }
                          
                          """)
        ts_lookup_btn.clicked.connect(self.ts_lookup_ui)
        ts_lookup_btn.setFixedSize(130, 50)

       
        
        tool_buttons_layout = QVBoxLayout()
        tool_buttons_layout.setSpacing(5)  # Small spacing between buttons
        tool_buttons_layout.setAlignment(Qt.AlignVCenter)
        tool_buttons_layout.addWidget(setting_btn)
        tool_buttons_layout.addWidget(help_btn)
        tool_buttons_layout.addWidget(search_btn)
        tool_buttons_layout.addWidget(ts_lookup_btn)

        tool_buttons_widget = QWidget()
        tool_buttons_widget.setLayout(tool_buttons_layout)

        button_layout.addWidget(tool_buttons_widget, 0, 3, 4, 1)  # Span all 4 rows in column 3
        
      
        
        
        quick_price_btn_layout = QGridLayout()
        quick_price_btn_layout.setSpacing(2)
        quick_price_btn_layout.setContentsMargins(10,10,10,10)
        quick_price_btn_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        
        r_label = QLabel("Quick Cash In (R)")
        r_label.setStyleSheet("color: white; font-size: 15px;")
        quick_price_btn_layout.addWidget(r_label, 2,3)
        
        quick_price_btn = {
            
            "5":(3,3), "10":(3,4),
            "15":(4,3), "20":(4,4),
            "150":(5,3), "200":(5,4),
            
        }
        
        for text, pos in quick_price_btn.items():
            btn = QPushButton(text)
            btn.clicked.connect(self.append_number)
            btn.setMaximumSize(120, 50)
            btn.setStyleSheet("""
                          QPushButton {
                              
                              background: grey;
                              
                              padding: 15px;
                              border-radius: 5px;
                              width: 400px;
                              
                          }
                          QPushButton:hover {
                             background-color: darkgrey; 
                              
                          }
                          
                          """)
            if len(pos) == 1:
                
                quick_price_btn_layout.addWidget(btn, *pos)
            else:
                quick_price_btn_layout.addWidget(btn, *pos)
                
            
            
            quick_price_btn_tool_widget = QWidget()
            quick_price_btn_tool_widget.setLayout(quick_price_btn_layout)
            
            
            button_layout.addWidget(quick_price_btn_tool_widget,   3, 2, 2,4 )
        

    
        self.charge_btn = None
        
        # Control buttons (Clear, Subpayment, etc.)
        control_button_layout = QHBoxLayout()
        control_button_layout.setAlignment(Qt.AlignJustify)
        for label in ["Clear", "Subpayment", "Charge", ]:
            btn = QPushButton(label)
            btn.setStyleSheet("""
                          QPushButton {
                              
                              background: ghostwhite;
                              color: darkgray;
                              padding: 15px;
                              border-radius: 5px;
                              
                          }
                          QPushButton:hover {
                             background-color: grey; 
                              
                          }
                          
                          """)
            btn.setFixedSize(120, 50)
            if label == "Clear":
                btn.clicked.connect(self.clear_items)
                
            if label == "Subpayment":
              btn.clicked.connect(self.open_subpayment)
                
                
            elif label == "Charge":
                self.charge_btn = btn
                self.charge_btn.setEnabled(False) 
                btn.clicked.connect(self.process_payment)  # New button for payment
            control_button_layout.addWidget(btn)

        # Add the number grid and control buttons to right_layout
        right_layout.addLayout(price_button_layout)
        right_layout.addLayout(button_layout)
        right_layout.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))
        right_layout.addLayout(control_button_layout)

        # Start Scanner Button
        start_scanner_button = QPushButton("Start Scanner")
        start_scanner_button.setStyleSheet("""
                          QPushButton {
                              
                              background: rgb(0, 128, 255);
                              border-radius: 5px;
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
        start_scanner_button.setFixedSize(100, 50)
        start_scanner_button.clicked.connect(self.start_scanner)  # Start the scanner
        button_layout.addWidget(start_scanner_button)
        
        start_scanner_button = QPushButton("Stop Scanner")
        start_scanner_button.setStyleSheet("""
                          QPushButton {
                              
                              background: rgb(0, 128, 255);
                              border-radius: 5px;
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
        start_scanner_button.setFixedSize(100, 50)
        start_scanner_button.clicked.connect(self.stop_scanner)  # Start the scanner
        button_layout.addWidget(start_scanner_button)
        
        
        third_row_layout = QHBoxLayout()
        
        self.atm_service_btn = QPushButton("ATM Services")
        self.atm_service_btn.setFixedSize(120, 50)
        self.atm_service_btn.setStyleSheet("""
                          QPushButton {
                              
                              background: rgb(0, 128, 255);
                              border-radius: 5px;
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
        
        self.atm_service_btn.clicked.connect(self.open_atm_service_ui)
        third_row_layout.addWidget(self.atm_service_btn)
        
        
        right_layout.addLayout(third_row_layout)
        
        second_row_layout = QHBoxLayout()
        # second_row_layout.setAlignment(Qt.AlignJustify)
        second_row_layout.setContentsMargins(0,0,0,0)
        
        sfs =QPushButton("Insurences")
        sfs.setFixedSize(120, 50)
        sfs.setStyleSheet("""
                          QPushButton {
                              
                              background: rgb(0, 128, 255);
                              border-radius: 5px;
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
        sfs.clicked.connect(self.open_funeral_dialog)
        second_row_layout.addWidget(sfs)
        
        dstv =QPushButton("Dstv")
        dstv.setFixedSize(120, 50)
        dstv.setStyleSheet("""
                          QPushButton {
                              
                              background: rgb(0, 128, 255);
                              border-radius: 5px;
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
        dstv.clicked.connect(self.open_destv_dialog)
        second_row_layout.addWidget(dstv)
        
        eletricity =QPushButton("Electricty")
        eletricity.setStyleSheet("""
                          QPushButton {
                              
                              background: rgb(0, 128, 255);
                              border-radius: 5px;
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
        eletricity.clicked.connect(self.open_electricity_dialog)
        eletricity.setFixedSize(120, 50)
        second_row_layout.addWidget(eletricity)
        
        vochour =QPushButton("Network services")
        vochour.setStyleSheet("""
                          QPushButton {
                              
                              background: rgb(0, 128, 255);
                              border-radius: 5px;
                          }
                          QPushButton:hover {
                             background: gray; 
                              
                          }
                          
                          """)
        vochour.clicked.connect(self.vochour_dialog)
        vochour.setFixedSize(120, 50)
        second_row_layout.addWidget(vochour)
        
        
        
        right_layout.addLayout(second_row_layout)
        # Add right layout to main layout
        main_layout.addLayout(right_layout, stretch=1)
        self.setLayout(main_layout)

       
        # Initialize the scanner thread
        self.scanner_thread = None


    def update_time(self):
        now = datetime.now()
        
        formatted_time = now.strftime("%H:%M:%S")
        self.time_label.setText(formatted_time)


    def append_number(self):
        """Append number to current price and auto-submit."""
        current_text = self.current_price
        if current_text == "0.00":
            new_text = self.sender().text()  # Get the number from the button clicked
        else:
            new_text = current_text + self.sender().text()

        # Check if the number includes a decimal
        if "." in new_text:
            parts = new_text.split(".")
            if len(parts) > 2:  # Prevent adding multiple decimals
                return

        self.current_price = new_text
        self.price_button.setText(new_text)  # Update the price display button

    def erase_last_digit(self):
        """Erase last digit from the current price and auto-submit."""
        current_text = self.current_price
        if len(current_text) > 1:
            new_text = current_text[:-1]
        else:
            new_text = "0.00"
        self.current_price = new_text
        self.price_button.setText(new_text)  # Update the price display button

    def add_item(self, name, price):
        """Add the scanned item to the list and update total."""
        if name in self.items:
            # If the item is already in the list, increment its quantity
            self.items[name]['quantity'] += 1
            print(name)
        else:
            # If it's a new item, add it with quantity 1
            # TypeError: list indices must be integers or slice
            self.items[name] = {'quantity': 1, 'price': price}
            print(name)

        # Update the item list and total
        self.update_item_list()
        self.update_total()
        

    def update_item_list(self):
        """Update the display of items in the QListWidget."""
        self.view.clear()  # Clear the previous list

        for name, details in self.items.items():
            quantity = details['quantity']
            price = details['price']
            total_price = price * quantity  # Calculate total price for the item

            # Add item to the list in the format: "Name xQuantity - RTotalPrice"
            self.view.addItem(f"{name[:15]} x{quantity} - R{total_price:.2f}")


    def delete_item(self):
        """Delete the selected item from the list and update total."""
        selected_items = self.view.selectedItems()
        if not selected_items:
            return  # No item selected

        for item in selected_items:
            item_text = item.text()
            # Extract the name (assumes format: "Name xQuantity - RPrice")
            name = item_text.split(" x")[0]
            if name in self.items:
                del self.items[name]

        # Update display and total
        self.update_item_list()
        self.update_total()
        # self.update_tax_amount()

    def update_total(self):
        """Update the total amount."""
        self.subtotal = sum(details['price'] * details['quantity'] for details in self.items.values())
        
        self.tax = self.subtotal * self.tax_rate
        grand_total  = self.total + self.tax
        
        self.total = grand_total
        self.sub_total.setText(f"Sub total: R{self.subtotal:.2f}")
        self.tax_amount_label.setText(f"Tax (15%): R{self.tax:.2f}")
        self.grant_total_label.setText(f"Total: R{grand_total:.2f}")
        
    
        
    def update_tax_status(self, message ):
        self.tax_amount_label.setText(message)

    def update_status(self, message):
        """Update the scanner status message."""
        self.grant_total_label.setText(message)

    def clear_items(self):
        """Clear all items."""
        self.items.clear()
        self.update_item_list()
        self.update_total()

    def start_scanner(self):
        """Start the barcode scanner thread."""
        if not self.scanner_thread or not self.scanner_thread.isRunning():
            self.scanner_thread = BarcodeScanner()
            self.scanner_thread.product_scanned.connect(self.add_item)
            self.scanner_thread.scanner_status.connect(self.update_status)
            self.scanner_thread.start()

    def stop_scanner(self):
        """Stop the barcode scanner thread."""
        if self.scanner_thread and self.scanner_thread.isRunning():
            self.scanner_thread.stop()

    def process_payment(self):
        """Handles the payment process when the Pay button is clicked."""
        payment_status = f"Payment of R{self.total:.2f} processed successfully."
        print(payment_status)  # Replace with actual payment processing logic
        
        tax_statement = f"tax {self.tax:.2f}"
        print(tax_statement)
      
        self.view.addItem(payment_status)
        self.clear_items()  # Optionally clear items after payment
        self.charge_btn.setEnabled(True)

    def closeEvent(self, event):
        """Ensure the scanner is stopped when the app is closed."""
        self.stop_scanner()
        event.accept()

    
    
    def open_subpayment(self):
        self.charge_btn.setEnabled(False)
        self.subpayment_dialog = SubPaymentUi()
        self.subpayment_dialog.payment_accepted.connect(lambda: self.charge_btn.setEnabled(True))
        self.subpayment_dialog.exec()


    def open_electricity_dialog(self):
        price = float(self.current_price)  # Get the dynamically entered price
        electric_dialog = electricityDialog(price, self)  # Pass the price to the dialog
        electric_dialog.exec()
    
    def vochour_dialog(self):
        price = float(self.current_price)
        vochour_d = vochourDialog(price, self)
        vochour_d.exec()
    
    def open_funeral_dialog(self):
        price = float(self.current_price)
        dialog = FuneralCoverDialog(price ,self)
        dialog.exec()

    def open_destv_dialog(self):
        price = float(self.current_price)
        dstv_d = dstvDialog(price, self)
        dstv_d.exec()
    
    def open_atm_service_ui(self):
        service_ui = AtmServiceUi()
        service_ui.exec()
        
    def ts_lookup_ui(self):
        ts_ui = TsLookUpUi()
        ts_ui.exec()

    def settings_ui(self):
        setting_ui= SettingUi()
        setting_ui.exec()
    
    def open_option_ui(self):
        option_d = OptionUi()
        option_d.exec()
        
    def search_page_ui(self):
        search = SearchWidget()
        search.exec()
        
    def change_qaunt_ui(self):

        ui = ChangeQuantity()
        ui.exec()

