        
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
        QListWidget,
        QComboBox,
        QCheckBox,
         
     
     
   
)
from datetime import datetime
from PySide6.QtCore import Qt , QTimer
from PySide6.QtGui import QFont

from functools import partial

from options.save_changes_ui import SaveChanges



class OptionUi(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Options")
        self.setFixedSize(890, 770)
        

        
        
        
        layout = QVBoxLayout(self)
        
        self.content = QStackedWidget()
        layout.addWidget(self.content)
        
        
        self.pages = {}
        self.pages['options_page'] = self.options_page_ui()
        self.pages["adminstrative_page"] = self.adminstrative_page_ui()
        self.pages["inventory_maintaince_page"] = self.invenoty_page_ui()
        self.pages["department_maintainance_page"] = self.department_page_ui()
        # self.pages['vendor_maintainance_page'] = self.vendor_page_ui()
        
        
        # self.pages['customer_maintainance_page'] = self.customer_page_ui()
        # self.pages['employee_maintainance_page'] = self.employee_page_ui()
        # self.pages['timeclock_maintainance_page'] = self.timeclock_page_ui()
        
        
        # self.pages['purchase_orders_page'] = self.purchase_orders_page_ui()
        # self.pages['back_orders_page'] = self.back_orders_page_ui()
        # self.pages['customer_price_page'] = self.customer_price_page_ui()
        
        
        
        for page in self.pages.values():
            self.content.addWidget(page)
            
        self.content.setCurrentWidget(self.pages['options_page'])
        
        
    
#####################################################
    # First Options page 


    def options_page_ui(self):
        page = QWidget()
        layout = QGridLayout(page)
        layout.setAlignment(Qt.AlignVCenter)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(1)

        btn_name = {
                        "Cashier 1" : (0,1), 
                    "Setup 2" : (2,1), "Tools 3": (0,2),
            "Invoice Properties 4": (3,1), "Adminstrative 5": (2,2)
        }
        
        for text, pos in btn_name.items():
            btn = QPushButton(text)
            btn.setFixedHeight(55)
            btn.setStyleSheet("""
                              QPushButton {
                                  background: darkgreen;
                                  padding: 15px;
                              }
                              QPushButton:hover {
                                  background: green;
                              }
                              """)
            if text == "Adminstrative 5":
                btn.clicked.connect(partial(self.switch_page, "adminstrative_page"))
                
            if len(pos) == 2:
                layout.addWidget(btn, *pos)
            else:
                layout.addWidget(btn, *pos)
            
       
        self.setLayout(layout)
        
      
        
        return page
        
       
        
    def adminstrative_page_ui(self):
        page =QWidget()
    
        
        l = QGridLayout(page)
        l.setAlignment(Qt.AlignVCenter )
        l.setContentsMargins(0,0,0,0)
        l.setSpacing(1)
       
        
        bts = {
            "Inventory\n Maintaince":(0,0),  "Department\n Maintainance":(0,1),  "Vendor\n Maintainance":(0,2), 
            "Customer\n Maintaince":(1,0),  "Employee\n Maintainance":(1,1),  "Time Clock\n Management":(1,2),   
            "Purchase Orders":(2,0),  "Back Orders":(2,1),  "Customer prices":(2,2),  
            "Global Price\n Changes":(3,0),  "Reporting":(3,1), "Credit Card\n Settlement": (3,2),
            
            
        }
        
        for text, pos in bts.items():
            btns = QPushButton(text)
            btns.setFixedHeight(50)
            btns.setStyleSheet("""
                               QPushButton {
                                   background: darkblue;
                               }
                               QPushButton:hover {
                                   background: blue;
                               }
                               """)
            if text == "Inventory\n Maintaince":
                btns.clicked.connect(partial(self.switch_page, "inventory_maintaince_page" ))
                
            if text == "Department\n Maintainance":
                btns.clicked.connect(partial(self.switch_page, "department_maintainance_page"))
            
            if len(pos) == 2:
                l.addWidget(btns, *pos)
            else:
                l.addWidget(btns, *pos)
                
        self.setLayout(l)
        
    
        
          
        back_btn = QPushButton("Back")
        back_btn.setStyleSheet(
            """
            QPushButton {
                padding: 14px;
                margin-top: 50px;
                background: darkred;
               
                
            }
            QPushButton:hover {
                background: red;
                
            }
            
            """
        )
        # back_btn.setMaximumWidth(110)
        
        back_btn.clicked.connect(partial(self.switch_page, 'options_page'))
        l.addWidget(back_btn)
        
    
        return page 
    
    
##################################################################
     # Inventory Page UI
   						
    def invenoty_page_ui(self):	
        
        inventory_ui = QWidget()
        main_layout = QVBoxLayout(inventory_ui)
        main_layout.setAlignment(Qt.AlignTop)
            
        
            
        label = QLabel('Inventory Maintainance.')
        label.setStyleSheet('font-size: 25px; padding: 12px;')
        main_layout.addWidget(label)
            
            
            

            # --- Main Form Inputs ---
        form_layout = QFormLayout()
            

        self.item_number_input = QLineEdit()
        self.item_number_input.setStyleSheet('padding: 8px;')
        self.item_name_input = QLineEdit()
        self.item_name_input.setStyleSheet('padding: 8px;')
        self.avg_cost_input = QLineEdit()
        self.avg_cost_input.setStyleSheet('padding: 8px;')
        self.price_input = QLineEdit()
        self.price_input.setStyleSheet('padding: 8px;')
        self.tax_input = QLineEdit()
        self.tax_input.setStyleSheet('padding: 8px;')
        self.quantity_input = QLineEdit()
        self.quantity_input.setStyleSheet('padding: 8px;')
        self.description_input = QLineEdit()
        self.description_input.setStyleSheet('padding: 8px;')
            

        form_layout.addRow("Item Number:", self.item_number_input)
        form_layout.addRow("Item Name:", self.item_name_input)
        form_layout.addRow("Average Cost:", self.avg_cost_input)

            # --- Price, Tax, Quantity in one horizontal layout ---
        price_row = QWidget()
        price_layout = QHBoxLayout(price_row)
        price_layout.setContentsMargins(0, 0, 0, 0)  # Remove padding
        price_layout.setSpacing(10)

        self.price_input.setPlaceholderText("Price")
        self.tax_input.setPlaceholderText("Tax")
        self.quantity_input.setPlaceholderText("Qty")

        price_layout.addWidget(self.price_input)
        price_layout.addWidget(self.tax_input)
        price_layout.addWidget(self.quantity_input)

        form_layout.addRow("Price / Tax / Qty:", price_row)

        form_layout.addRow("Optional Description:", self.description_input)

        main_layout.addLayout(form_layout)

            # --- Tabs Section ---
        tab_widget = QTabWidget()
        tab_widget.setContentsMargins(0,0,0,0)
            # tab_widget.setMaximumHeight()

        def create_tab_content(label_text):
            tab = QWidget()
            layout = QVBoxLayout(tab)
                
            text_edit = QTextEdit()
            text_edit.setPlaceholderText(f"Enter details for {label_text} here...")
            layout.addWidget(text_edit)
            return tab

        tab_widget.addTab(self.create_optional_info_tab(), "Optional Info")
        tab_widget.addTab(create_tab_content("Properties"), "Properties")
        tab_widget.addTab(create_tab_content("Notes"), "Notes")
        tab_widget.addTab(create_tab_content("Modifiers"), "Modifiers")
            
            
            
        tab_widget.addTab(create_tab_content("Ordering Info"), "Ordering Info")
        tab_widget.addTab(create_tab_content("Special Pricing Matrix"), "Special Pricing Matrix")
        tab_widget.addTab(create_tab_content("Sales History"), "Sales History")
        tab_widget.addTab(self.create_recipe_tab(), "Recipe")
            
            
        tabs_with_button = QWidget()
        tabs_with_button_layout = QHBoxLayout(tabs_with_button)
        tab_widget.setStyleSheet("color: green; font-size: 20px;  padding:0px; margin:0px; ")
        tabs_with_button_layout.addWidget(tab_widget)


        main_layout.addWidget(tab_widget)
        
        
        label = QLabel("Search by items number.")
        label.setStyleSheet("font-size: 13px; font-style: Arial" )
        main_layout.addWidget(label)
        
        search_input = QLineEdit()
        search_input.setMaximumHeight(34)
        # search_iput.setPlaceholderText('Search...')
        main_layout.addWidget(search_input)
        
        
        btn_layout = QGridLayout()
        btn_layout.setSpacing(1.8)
        
        bottom_btns = {
            "Add Item":(1, 0), "Save":(1, 1), "Trasnfare":(1, 2), 
            "Help":(2, 0), "Deplicate":(2, 1), "Instant PO":(2, 2), 
        }
        
        for text, pos in bottom_btns.items():
            btn = QPushButton(text)
            btn.setStyleSheet("""
                              QPushButton {
                                  padding: 10px;
                                  background: darkgreen;
                                  
                              }
                              QPushButton:hover {
                                  background: green
                              }
                              """)
            if len(pos) == 2:
                btn_layout.addWidget(btn, *pos)
            else:
                btn_layout.addWidget(btn, *pos)
            
            
            
        # exit_btn = QPushButton('Exit')
        # exit_btn.setStyleSheet(
        #         """
        #         QPushButton {
        #             padding: 14px;
        #             margin: 10px;
        #             background: darkred;
                    
        #         }
        #         QPushButton:hover {
        #             background: red;
                    
        #         }
                
        #         """
        #     )
        main_layout.addLayout(btn_layout)
            
            

        return inventory_ui					
			
        
        
    def create_recipe_tab(self):
                tab = QWidget()
                layout = QHBoxLayout(tab)  # Horizontal layout: buttons | list

                # Left-side vertical buttons
                button_layout = QVBoxLayout()
                add_button = QPushButton("Add Ingredient")
                remove_button = QPushButton("Remove Ingredient")
                button_layout.addWidget(add_button)
                button_layout.addWidget(remove_button)
                button_layout.addStretch()  # Push buttons to top

                # Right-side list widget
                ingredient_list = QListWidget()

                # Add both layouts to the main tab layout
                layout.addLayout(button_layout)
                layout.addWidget(ingredient_list)

                return tab
            
            
    
    
    def create_optional_info_tab(self):
        optional_row = QWidget()
        optional_layout = QHBoxLayout(optional_row)
        
        
        form_layout = QFormLayout()
        
        price_edit_line = QLineEdit()
        optional_layout.addWidget(price_edit_line)
        
        b_edit_line = QLineEdit()
        optional_layout.addWidget(b_edit_line)
        
        
        
        form_layout.addRow('Price', price_edit_line)
        form_layout.addRow('B', b_edit_line)
        
        optional_layout.addLayout(form_layout)
        
        return optional_row
                    
    # The Inventoty Page that contains tabs to swicth 
    # to subPage
######################################################################
            
   
   
   
   
#######################################################################
    # The Departmaent page User Interface.
    
    def department_page_ui(self):
        department_ui = QWidget()
        main_layout = QVBoxLayout(department_ui)
        main_layout.setAlignment(Qt.AlignTop)
        
        # self.setWindowTitle('Department Maintainance')
        
        label = QLabel("Department Maintainance.")
        label.setStyleSheet('font-size: 20px;')
        main_layout.addWidget(label)
        
        
        
        form_layout = QFormLayout()
        form_layout.setAlignment(Qt.AlignTop)
        
        self.combo_box = QComboBox()
        self.combo_box.addItems(['one', 'two', 'three'])
        self.combo_box.setStyleSheet("padding: 10px;")
        form_layout.addWidget(self.combo_box)
        
        self.department_id = QLineEdit()
        self.department_id.setStyleSheet("padding: 10px;")
        # self.department_id.setMaximumHeight(35)
        form_layout.addWidget(self.department_id)
        
        self.department_description = QLineEdit()
        self.department_description.setStyleSheet("padding: 10px;")
        form_layout.addWidget(self.department_description)
        
        
        
        form_layout.addRow('Catergory for department:', self.combo_box)
        form_layout.addRow('Department Id:', self.department_id )
        form_layout.addRow('Department Description:' , self.department_description)
        

        main_layout.addLayout(form_layout)

        tab_widget = QTabWidget()
        tab_widget.setContentsMargins(0,0,0,0)
       

        def create_tab_content(label_text):
                tab = QWidget()
                layout = QVBoxLayout(tab)
                
                text_edit = QTextEdit()
                text_edit.setPlaceholderText(f"Enter details for {label_text} here...")
                layout.addWidget(text_edit)
                return tab

        tab_widget.addTab(self.create_option_tab(), "Options")
        tab_widget.addTab(create_tab_content("Receipt Note"), "Receipt Note")
      
            
            
        tabs_with_button = QWidget()
        tabs_with_button_layout = QHBoxLayout(tabs_with_button)
        tab_widget.setStyleSheet("color: green; font-size: 20px;  padding:0px; margin:0px; ")
        tabs_with_button_layout.addWidget(tab_widget)


        main_layout.addWidget(tab_widget)
       
       
        bottom_btn_layout = QGridLayout()
        bottom_btn_layout.setAlignment(Qt.AlignRight)
        bottom_btn_layout.setSpacing(1)
        
        btn = {
            "Add\n Department":(1,0), "Save Changes":(1,1),  "Catergory\n Maintainance":(1,2),
            "Help":(2,0), "Deplicate":(2,1), "Delete":(2,2),
            
        }
        
        for text, pos in btn.items():
            btn = QPushButton(text)
            if text ==  "Save Changes":
                btn.clicked.connect(SaveChanges)
            btn.setMaximumHeight(55)
            btn.setStyleSheet("""
                              QPushButton {
                                  padding: 10px;
                                  background: darkgreen;
                                  
                              }
                              QPushButton:hover {
                                  background: green
                              }
                              """)
            
        
            
            if len(pos) == 2:
                bottom_btn_layout.addWidget(btn, *pos)
            else:
                bottom_btn_layout.addWidget(btn, *pos)
            
            
        main_layout.addLayout(bottom_btn_layout)
        
        
        del_and_ext_btn_layout  = QHBoxLayout()
        del_and_ext_btn_layout.setAlignment(Qt.AlignRight )
        

        for text in ['Delete', 'Exit']:
            btns = QPushButton(text)
            btns.setMaximumSize(110, 55)
            btns.setStyleSheet("""
            QPushButton {
                padding: 14px;
               
                background: darkred;
            }
            QPushButton:hover {
                background: red;
            }
        """)
            del_and_ext_btn_layout.addWidget(btns)
            
        
        main_layout.addLayout(del_and_ext_btn_layout)
        self.setLayout(main_layout)
        return department_ui
    
    
  




    def create_option_tab(self):
        option_tab = QWidget()

        option_layout = QVBoxLayout(option_tab)
        option_layout.setSpacing(5)

        # Checkboxes
        for text in [
            'Bar Tex Inclusive',
            'Include In Scale Export',
            'Require Permission For Sales.',
            'Require Special Reference Entry',
            'Print department House on Receipt.',
        ]:
            check_box = QCheckBox(text)
            check_box.setStyleSheet("color: white;")
            option_layout.addWidget(check_box)

        # Form Layout
        form_layout2 = QFormLayout()
        form_layout2.setAlignment(Qt.AlignBottom)
        form_layout2.setSpacing(10)
        form_layout2.setContentsMargins(0, 0, 0, 0)

        # Inputs with default value "0"
        square_footage = QLineEdit()
        square_footage.setFixedWidth(150)
        square_footage.setText("0")
        square_footage.setStyleSheet('color: white;')

        item_cost_percentage = QLineEdit()
        item_cost_percentage.setFixedWidth(150)
        item_cost_percentage.setText("0")
        item_cost_percentage.setStyleSheet('color: white;')

        # White text labels
        label1 = QLabel("Square Footage:")
        label1.setStyleSheet("color: white;")
        label2 = QLabel("Item Cost Percentage:")
        label2.setStyleSheet("color: white;")

        # Add rows
        form_layout2.addRow(label1, square_footage)
        form_layout2.addRow(label2, item_cost_percentage)

        # Add form layout to main layout
        option_layout.addLayout(form_layout2)

        return option_tab



    def switch_page(self, page_name):
        if page_name in self.pages:
            self.content.setCurrentWidget(self.pages[page_name])
    
        
      
        
       
        
  

        
        
        
    
    
        
        
        
       
   
   
  
    # def vendor_page_ui(self):
    #     pass
   
   
    
        
    # def customer_page_ui(self):
    #     pass
    
    
    # def employee_page_ui(self):
    #     pass
    
    
    # def timeclock_page_ui(self):
    #     pass
    
        
  
   