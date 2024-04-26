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
    def load_orders(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, product, product_quantity, customer, total_price, order_date FROM orders")
        orders = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(orders))
        self.order_data = {}  # IDs für Lösch- und Bearbeitungsoperationen speichern

        for row, order in enumerate(orders):
            order_id, product, quantity, customer, total_price, order_date = order
            self.order_data[row] = order_id
            self.table.setItem(row, 0, QTableWidgetItem(product))
            self.table.setItem(row, 1, QTableWidgetItem(str(quantity)))
            self.table.setItem(row, 2, QTableWidgetItem(customer))
            self.table.setItem(row, 3, QTableWidgetItem(str(total_price)))
            self.table.setItem(row, 4, QTableWidgetItem(order_date))

    def load_selected_order(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.product_input.setText(self.table.item(selected_row, 0).text())
            self.quantity_input.setText(self.table.item(selected_row, 1).text())
            self.customer_input.setText(self.table.item(selected_row, 2).text())
            self.total_price_input.setText(self.table.item(selected_row, 3).text())
