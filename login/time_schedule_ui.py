
        
        
from PySide6.QtWidgets import (
   QDialog,
   QLabel,
   QLineEdit,
   QVBoxLayout,
   QPushButton,
   QGridLayout,
   QDialogButtonBox,
   QStackedWidget,
    QWidget,
    QHBoxLayout
   
)
from datetime import datetime
from PySide6.QtCore import Qt , QTimer
from PySide6.QtGui import QFont

from functools import partial


class TimeScheduleUi(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Time Schedule")
        self.setFixedSize(500, 500)
        

        atm_layout = QVBoxLayout(self)
       
        
        self.content = QStackedWidget()
        atm_layout.addWidget(self.content)
        
        
        self.pages = {}
        self.pages["password_required_page"] = self.password_required_page_ui()
        self.pages["time_schedule_page"] = self.create_uif_ui()
        self.pages["clock_in_page"] = self.clock_in_page_ui()
        
        
        
        for page in self.pages.values():
            self.content.addWidget(page)
            
        self.content.setCurrentWidget(self.pages["password_required_page"])
        
       
        
        
    def hanlde_close(self):
        self.close()
        
   
    def password_required_page_ui(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
          
        button_layout = QGridLayout()
        button_layout.setSpacing(2)
        button_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        
        
        
        
        
        label = QLabel("Enter password")
        label.setStyleSheet("padding: 1px; font-size: 20px;")
        layout.addWidget(label)
        
        edit_line = QLineEdit()
        edit_line.setReadOnly(True)
        edit_line.setMinimumHeight(40)
        edit_line.setMaximumHeight(30)
        layout.addWidget(edit_line)
        
        
        
        label_2 = QLabel("Enter cashier ID (If not admin)")
        label_2.setStyleSheet("padding: 1px; font-size: 20px;")
        layout.addWidget(label_2)
        
        edit_line_2 = QLineEdit()
        edit_line_2.setMinimumHeight(40)
        edit_line_2.setReadOnly(True)
        edit_line_2.setMaximumHeight(30)
        layout.addWidget(edit_line_2)
        
        
      
        
        buttons = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2),
            "4": (1, 0), "5": (1, 1), "6": (1, 2),
            "7": (2, 0), "8": (2, 1), "9": (2, 2),
            "0": (3, 0, 1, 2)
        }

        for text, pos in buttons.items():
            btn = QPushButton(text)
            btn.setStyleSheet("background: grey; padding:3px;")
            btn.setFixedSize(140, 50)
            # btn.clicked.connect(self.append_number)
            if len(pos) == 2:
                button_layout.addWidget(btn, *pos)
            else:
                button_layout.addWidget(btn, *pos)

        # Erase button
        erase_button = QPushButton("⌫")
        erase_button.setStyleSheet("background: red;")
        erase_button.setFixedSize(140, 50)
        # erase_button.clicked.connect(self.erase_last_digit)
        button_layout.addWidget(erase_button, 3, 1)
        
        
        self.ok_button = QPushButton("OK")
        self.ok_button.setMaximumSize(140, 50)
        self.ok_button.setStyleSheet("""
                                     QPushButton {
                                         padding: 13px;
                                         border-radius: 3px;
                                         font-style: arial;
                                         background-color: white;
                                         color: grey;
                                     }
                                     QPushButton:hover {
                                         
                                         background-color: lightgreen;
                                         
                                     }
                                     """)
        self.ok_button.clicked.connect(partial(self.switch_page, "time_schedule_page"))
        button_layout.addWidget(self.ok_button,  3, 2)
        
        
        layout.addLayout(button_layout)
        
        back_btn = QPushButton("Cancel")
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
        layout.addWidget(back_btn)
        layout.addLayout(layout)
        
        return page
    
    
    
    
    
    def clock_in_page_ui(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        label = QLabel("Please Select Job Code To Add For This Employee.")
        label.setStyleSheet("Font-size: 20px;")
        layout.addWidget(label)
        
        
        button_layout = QHBoxLayout()
        
        
        button_layout.setAlignment(Qt.AlignVCenter | Qt.AlignTop)
        
        for stock_in_btn in ["robtest2Cashier", "robtest2Stock"]:
            btn = QPushButton(stock_in_btn)
            btn.setStyleSheet("""
                              QPushButton {
                                  background-color: ghostwhite;
                                  color: black;
                                  padding: 15px;
                                  font-style: Arial;
                                 
                              }
                              QPushButton:hover {
                                  background-color: gray;
                                
                              }
                              """)
            button_layout.addWidget(btn)
        layout.addLayout(button_layout)
        
        
        ok_and_select_btn_layout = QHBoxLayout()
        ok_and_select_btn_layout.setAlignment(Qt.AlignRight)
        
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
        cancel_btn.clicked.connect(self.close_dialog)
        ok_and_select_btn_layout.addWidget(cancel_btn)
        
        ok_btn  = QPushButton("Select")
        ok_btn.setStyleSheet(
            """
            QPushButton {
                padding: 14px;
                margin: 10px;
                background: darkgreen;
                
            }
            QPushButton:hover {
                background: green;
                
            }
            
            """
        )
        ok_and_select_btn_layout.addWidget(ok_btn)
        
        layout.addLayout(ok_and_select_btn_layout)
        
        
        
        
                
        return page
    
    
    
    
    
    def create_uif_ui(self):
        ui_page = QWidget()
        ui_layout = QVBoxLayout(ui_page)
        
        
        time_and_date_layout = QHBoxLayout()
        time_and_date_layout.setAlignment(Qt.AlignJustify | Qt.AlignTop)
        
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        date_display = datetime.today().strftime("%d/%m/%Y")
        
        date_time = datetime.now()
    
        
        self.label = QLabel(self)
        self.label.setText(date_time.strftime("%I:%M:%S %p"))
        self.label.setStyleSheet("padding: 12px; font-size: 25px;")
        time_and_date_layout.addWidget(self.label)
        
       
        today_day = QLabel(f"{date_display} ")
        
        today_day.setStyleSheet("font-style: Arial; padding: 12px; font-size: 25px; margin: 6px;")
        time_and_date_layout.addWidget(today_day)
        
        
        btns_layout = QGridLayout()
        btns_layout.setAlignment(Qt.AlignVCenter)

       
        
        buttons = {
            "Clock In": (1,0),  "Leave for Break": (1,1),
            "Clock Out": (2, 0), "Back from Break": (2,1),
            
            
        }
        
        for text, pos in buttons.items():
            btn = QPushButton(text)
            if text == "Clock In":
                btn.clicked.connect(partial(self.switch_page, "clock_in_page"))
            btn.setStyleSheet("""
                              QPushButton {
                                  background-color: ghostwhite;
                                  color: black;
                                  padding: 15px;
                                  font-style: Arial;
                                 
                              }
                              QPushButton:hover {
                                  background-color: gray;
                                
                              }
                              """)
            btn.setMaximumHeight(50)
            if len(pos) == 1:
                btns_layout.addWidget(btn, *pos)
            else:
                btns_layout.addWidget(btn, *pos)
                
            
        
            
            
        
        ui_layout.addLayout(time_and_date_layout)
        ui_layout.addLayout(btns_layout)
        
        
        back_btn = QPushButton("Cancel")
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
        # back_btn.clicked.connect(partial(self.switch_page, "atm_service_ui"))
        back_btn.clicked.connect(self.close_dialog)
        ui_layout.addWidget(back_btn)
            
    
        return ui_page
    
    def close_dialog(self):
        self.close()
    
    def update_time(self):
        now = datetime.now()
        
        formatted_time = now.strftime("%H:%M:%S %p ")
        self.label.setText(formatted_time)
    
    def switch_page(self, page_name):
        if page_name in self.pages:
            self.content.setCurrentWidget(self.pages[page_name])
    
        
