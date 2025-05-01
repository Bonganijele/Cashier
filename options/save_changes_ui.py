
        
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
from PySide6.QtGui import QFont, QColor

from functools import partial


class SaveChanges(QDialog):
    def __init__(self):
        super().__init__()  
        
    
        self.setWindowTitle('save changes')
        self.setFixedSize(400, 200)

        
        main_layout = QVBoxLayout()
        # bg_color = QColor('green')
        main_layout.setAlignment(Qt.AlignVCenter | Qt.AlignTop)        
        
        
        
        label = QLabel('Your department has been added Would\n you like to add another?')
        label.setStyleSheet('font-size: 18px; font-style: Arial;')
        main_layout.addWidget(label)
        
        
        button_layout = QHBoxLayout()
        
        for text in ['Yes', 'No']:
            btn = QPushButton(text)
            # btn.setMaximumHeight(100)
            btn.setStyleSheet("""
                              QPushButton {
                                 background: rgb(0, 128, 255);
                                 padding: 25px;
                              }
                              QPushButton :hover {
                                    background : blue;
                                  
                              }
                              """)
            button_layout.addWidget(btn)
            
            main_layout.addLayout(button_layout)
            self.setLayout(main_layout)
        
        
        
        self.exec()
     