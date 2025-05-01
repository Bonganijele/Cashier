         
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
    QHBoxLayout, 
    QFrame,
     QTableWidget,
     QHeaderView,
         QTabWidget,
         QTextEdit,
        QFormLayout,
        QListWidget
         
     
     
   
)
from datetime import datetime
from PySide6.QtCore import Qt , QTimer
from PySide6.QtGui import QFont

from functools import partial


class InventoryMaintainceUi(QDialog):
    def __init__(self, parent = None):
          super().__init__(parent)
          
          self.setWindowTitle('l')
         
    