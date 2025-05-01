from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QVBoxLayout, QPushButton,
    QGridLayout, QHBoxLayout,
    QCheckBox
)

from PySide6.QtCore import Qt, QThread, Signal, QSize
# import sys
# import cv2
# from pyzbar.pyzbar import decode

# PRODUCTS = {
#     "P123": {"name": "Milk 500ml", "price": 12.50},
#     "P456": {"name": "Bread Loaf", "price": 17.00},
#     "P789": {"name": "Eggs (Dozen)", "price": 30.00},
#     "6001299016608": {"name": "Tropica Mango 500ml", "price": 16.99},
# }

# class BarcodeScanner(QThread):
#     product_scanned = Signal(str, float)
#     scanner_status = Signal(str)

#     def __init__(self):
#         super().__init__()
#         self._running = True

#     def run(self):
#         self.scanner_status.emit("Starting scanner...")
#         cap = cv2.VideoCapture(0)

#         if not cap.isOpened():
#             self.scanner_status.emit("Camera not found.")
#             return

#         self.scanner_status.emit("Scanner running. Hold barcode up to camera.")

#         while self._running:
#             ret, frame = cap.read()
#             if not ret:
#                 continue

#             for barcode in decode(frame):
#                 code_data = barcode.data.decode("utf-8")
#                 if code_data in PRODUCTS:
#                     product = PRODUCTS[code_data]
#                     self.product_scanned.emit(product['name'], product['price'])

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         cap.release()
#         self.scanner_status.emit("Scanner stopped.")

#     def stop(self):
#         self._running = False
#         self.wait()

class SettingUi(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        
        self.setWindowTitle("Settings")
        self.setFixedSize(490, 370)

        setting_layout = QVBoxLayout()
        
        check_box_layout = QHBoxLayout()
        check_box_layout.setSpacing(3)
        check_box_layout.setAlignment(Qt.AlignTop| Qt.AlignJustify)
        
        label = QLabel("Scanning Device is enabled by default.")
        label.setStyleSheet("font-size: 20px;")
        check_box_layout.addWidget(label)

        scanner_check_box = QCheckBox()
        # scanner_check_box.setStyleSheet("background: rgb(0, 128, 255); border-radius: 5px;")
        scanner_check_box.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "width :30px;"
                               "height : 30px;"
                               "}")
        # scanner_check_box.clicked.connect(self.start_scanner)
        check_box_layout.addWidget(scanner_check_box)
        
        # Initialize the scanner thread
        self.scanner_thread = None

        
        self.setLayout(check_box_layout)
        
    # def start_scanner(self):
    #     """Start the barcode scanner thread."""
    #     if not self.scanner_thread or not self.scanner_thread.isRunning():
    #         self.scanner_thread = BarcodeScanner()
    #         # self.scanner_thread.product_scanned.connect(self.add_item)
    #         # self.scanner_thread.scanner_status.connect(self.update_status)
    #         self.scanner_thread.start()

    # def stop_scanner(self):
    #     """Stop the barcode scanner thread."""
    #     if self.scanner_thread and self.scanner_thread.isRunning():
    #         self.scanner_thread.stop()
            
    # def closeEvent(self, event):
    #     """Ensure the scanner is stopped when the app is closed."""
    #     self.stop_scanner()
    #     event.accept()
