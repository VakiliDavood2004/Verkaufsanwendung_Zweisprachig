import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton, QMessageBox

class InvoiceForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bestellliste 📜")
        self.resize(600, 400)
        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(2)  
        self.table.setHorizontalHeaderLabels(["Bestellnummer 🆔", "Kundenname 👤"])
        self.table.cellClicked.connect(self.show_receipt) 
        layout.addWidget(QLabel("Liste der registrierten Bestellungen 📜"))
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_orders()

    def load_orders(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, customer FROM orders")
        orders = cursor.fetchall()
        conn.close()
        self.table.setRowCount(len(orders))

        for row_idx, order in enumerate(orders):
            for col_idx, data in enumerate(order):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
    def show_receipt(self, row, _):
        order_id = self.table.item(row, 0).text()

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT product, product_price, product_quantity, customer, customer_phone, customer_address,
                   service, service_price, total_price, order_date
            FROM orders WHERE id = ?
        """, (order_id,))
        order = cursor.fetchone()
        conn.close()
