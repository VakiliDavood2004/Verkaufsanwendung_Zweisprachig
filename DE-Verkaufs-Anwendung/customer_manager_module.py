import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFormLayout, QLineEdit, QMessageBox

class CustomerManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kundenverwaltung 👤")
        self.resize(500, 400)

        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(3) 
        self.table.setHorizontalHeaderLabels(["Kundenname", "Telefonnummer", "Adresse"])
        self.table.itemSelectionChanged.connect(self.load_selected_customer)
        layout.addWidget(self.table)

        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.address_input = QLineEdit()

        form_layout.addRow("Kundenname:", self.name_input)
        form_layout.addRow("Telefonnummer:", self.phone_input)
        form_layout.addRow("Adresse:", self.address_input)

        layout.addLayout(form_layout)

        self.update_button = QPushButton("Kunde bearbeiten 🔄")
        self.update_button.clicked.connect(self.update_customer)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Kunde löschen 🗑️")
        self.delete_button.clicked.connect(self.delete_customer)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
        self.load_customers()  
