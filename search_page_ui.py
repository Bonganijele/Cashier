from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QComboBox, QLineEdit, QListWidget, QDialog
)


class SearchWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Main vertical layout
        main_layout = QVBoxLayout(self)

        # Horizontal layout for combo boxes
        combo_layout = QHBoxLayout()

        # Category combo box
        self.category_combo = QComboBox()
        self.category_combo.addItem("All Categories")
        self.category_combo.addItems(["Groceries", "Electronics", "Clothing"])
        combo_layout.addWidget(QLabel("Category:"))
        combo_layout.addWidget(self.category_combo)

        # Department combo box
        self.department_combo = QComboBox()
        self.department_combo.addItem("All Departments")
        self.department_combo.addItems(["Front", "Back", "Online"])
        combo_layout.addWidget(QLabel("Department:"))
        combo_layout.addWidget(self.department_combo)

        # Vendor combo box
        self.vendor_combo = QComboBox()
        self.vendor_combo.addItem("All Vendors")
        self.vendor_combo.addItems(["Vendor A", "Vendor B", "Vendor C"])
        combo_layout.addWidget(QLabel("Vendor:"))
        combo_layout.addWidget(self.vendor_combo)

        # Add combo layout to main layout
        main_layout.addLayout(combo_layout)

        # Search bar
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search...")
        main_layout.addWidget(self.search_input)

        # List widget for search results
        self.results_list = QListWidget()
        main_layout.addWidget(self.results_list)

        # Optional: connect signals for dynamic search/filtering
        self.search_input.textChanged.connect(self.filter_results)
        self.category_combo.currentIndexChanged.connect(self.filter_results)
        self.department_combo.currentIndexChanged.connect(self.filter_results)
        self.vendor_combo.currentIndexChanged.connect(self.filter_results)

    def filter_results(self):
        # Placeholder logic to show filtering in effect
        self.results_list.clear()
        self.results_list.addItem(
            f"Searching: '{self.search_input.text()}' | "
            f"Category: {self.category_combo.currentText()} | "
            f"Department: {self.department_combo.currentText()} | "
            f"Vendor: {self.vendor_combo.currentText()}"
        )
