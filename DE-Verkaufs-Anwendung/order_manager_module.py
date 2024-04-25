import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFormLayout, QLineEdit, QMessageBox

class OrderManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📋 Bestellverwaltung")
        self.resize(600, 400)

        layout = QVBoxLayout()
        
        # Bestelltabelle anzeigen
        self.table = QTableWidget()
        self.table.setColumnCount(5)  # Produktname, Menge, Kunde, Gesamtpreis, Datum
        self.table.setHorizontalHeaderLabels(["Produktname", "Menge", "Kundenname", "Gesamtpreis", "Datum"])
        self.table.itemSelectionChanged.connect(self.load_selected_order)
        layout.addWidget(self.table)

        # Bestellbearbeitungsformular
        form_layout = QFormLayout()
        self.product_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.customer_input = QLineEdit()
        self.total_price_input = QLineEdit()
        
        form_layout.addRow("Produktname", self.product_input)
        form_layout.addRow("Menge:", self.quantity_input)
        form_layout.addRow("Kundenname:", self.customer_input)
        form_layout.addRow("Gesamtpreis:", self.total_price_input)
        
        layout.addLayout(form_layout)

        # Schaltflächen 
        self.update_button = QPushButton("🔄 Bestellung bearbeiten")
        self.update_button.clicked.connect(self.update_order)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("🗑️ Bestellung löschen")
        self.delete_button.clicked.connect(self.delete_order)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
        self.load_orders()  # Bestellungen während der Ausführung anzeigen
