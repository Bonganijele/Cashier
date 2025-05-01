from PySide6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QVBoxLayout, QPushButton,
    QGridLayout, QHBoxLayout, QMainWindow, QWidget, QToolBar, 
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

from login.time_schedule_ui import TimeScheduleUi


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("LogIn")
        self.setFixedSize(1012, 660)

        Ui = QWidget()
        self.setCentralWidget(Ui)
        
        self.current_input = ""

        main_layout = QVBoxLayout(Ui)
        main_layout.setAlignment(Qt.AlignHCenter)        
        right_layout = QVBoxLayout()
       

        button_layout = QGridLayout()
        button_layout.setSpacing(2)
        button_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        
        toolbar = QToolBar("Toolbar")
        toolbar.setStyleSheet("background: red; font-style: Arial")
        self.addToolBar(toolbar)
        
        action_btn = QAction("Manager", self)
        action_btn.setStatusTip("Manager button")
        toolbar.addAction(action_btn)
        
        
        time_schedule = QAction("Time Schedule", self)
        time_schedule.triggered.connect(self.time_schedule_ui)
        time_schedule.setStatusTip("Time Schedule button")
        toolbar.addAction(time_schedule)
        
        help_btn = QAction("Help", self)
        help_btn.setStatusTip("Help button")
        toolbar.addAction(help_btn)
        
        exit_btn = QAction("Exit", self)
        exit_btn.triggered.connect(self.exit_program)
        exit_btn.setStatusTip("exit button")
        toolbar.addAction(exit_btn)
        
         
        
        

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
            btn.setFixedSize(140, 50)
            btn.clicked.connect(self.append_number)
            if len(pos) == 2:
                button_layout.addWidget(btn, *pos)
            else:
                button_layout.addWidget(btn, *pos)

        # Erase button
        erase_button = QPushButton("⌫")
        erase_button.setStyleSheet("background: red;")
        erase_button.setFixedSize(140, 50)
        erase_button.clicked.connect(self.erase_last_digit)
        button_layout.addWidget(erase_button, 3, 1)
        
        
        self.ok_button = QPushButton("Enter")
        self.ok_button.setMaximumSize(140, 50)
        self.ok_button.setStyleSheet("""
                                     QPushButton {
                                         padding: 10px;
                                         border-radius: 3px;
                                         font-style: arial;
                                         background-color: white;
                                         color: grey;
                                     }
                                     QPushButton:hover {
                                         
                                         background-color: lightgreen;
                                         
                                     }
                                     """)
       
        self.ok_button.setShortcut("Enter")
        self.ok_button.clicked.connect(self.authenticate_user)
        button_layout.addWidget(self.ok_button, 3, 2)

       

        label = QLabel("Cashier")
      
        label.setStyleSheet("padding: 10px; font-weight: bold; font-size: 60px; text-align: center;")
        right_layout.addWidget(label)

        self.id_label = QLineEdit()
        self.id_label.setStyleSheet("font-size: 30px;")
        self.id_label.setMinimumHeight(55)
        self.id_label.setMaximumWidth(450)
        self.id_label.setReadOnly(True)
        right_layout.addWidget(self.id_label)

        main_layout.addLayout(right_layout, stretch=1)

        dialog_btns = QHBoxLayout()
        dialog_btns.setContentsMargins(0, 0, 0, 0)
        dialog_btns.setSpacing(2.5)
        dialog_btns.setAlignment(Qt.AlignRight)

        # cancel_button = QPushButton("Cancel")
        # cancel_button.setMaximumHeight(55)
        # cancel_button.setMaximumWidth(100)
        # cancel_button.setStyleSheet("padding: 10px; background: red; border-radius: 3px;")
        # # cancel_button.clicked.connect(self.handle_cancel)
        # dialog_btns.addWidget(cancel_button)

       

        right_layout.addLayout(button_layout)
        main_layout.addLayout(dialog_btns)
        self.setLayout(main_layout)

    def append_number(self):
        number = self.sender().text()
        self.current_input += number
        self.update_list()

    def erase_last_digit(self):
        self.current_input = self.current_input[:-1]
        self.update_list()

    def update_list(self):
        self.id_label.setText(self.current_input)
    
    
    def authenticate_user(self):
        self.chasier_ui() 
    
     
    
    def exit_program(self):
        self.close()      
        
        
    def time_schedule_ui(self):
        ui = TimeScheduleUi()  
        ui.exec()
    
    def chasier_ui(self):
        from chasier_ui import MainWindow
        self.chasier_uI = MainWindow()
        self.chasier_uI.show()
        self.close()