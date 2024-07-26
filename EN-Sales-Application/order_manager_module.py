import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFormLayout, QLineEdit, QMessageBox

class OrderManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📋 Order Management")
        self.resize(600, 400)

        layout = QVBoxLayout()
        
        # Order Display Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)  #Product Name, Quantity, Customer, Total Price, Date
        self.table.setHorizontalHeaderLabels(["Product Name", "Quantity", "Customer Name", "Total Price", "Date"])
        self.table.itemSelectionChanged.connect(self.load_selected_order)
        layout.addWidget(self.table)

        # Order Edit Form
        form_layout = QFormLayout()
        self.product_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.customer_input = QLineEdit()
        self.total_price_input = QLineEdit()
        
        form_layout.addRow("Product Name:", self.product_input)
        form_layout.addRow("Quantity:", self.quantity_input)
        form_layout.addRow("Customer Name:", self.customer_input)
        form_layout.addRow("Total Price:", self.total_price_input)
        
        layout.addLayout(form_layout)

        # Buttons
        self.update_button = QPushButton("🔄 Edit Order")
        self.update_button.clicked.connect(self.update_order)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("🗑️ Delete Order")
        self.delete_button.clicked.connect(self.delete_order)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
        self.load_orders()  # Display orders during execution

    def load_orders(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, product, product_quantity, customer, total_price, order_date FROM orders")
        orders = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(orders))
        self.order_data = {}  # Save IDs for delete and edit operation

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

    def update_order(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "⚠️ Error", "⚠️ Please select an order!")
            return

        order_id = self.order_data[selected_row]
        product = self.product_input.text()
        quantity = self.quantity_input.text()
        customer = self.customer_input.text()
        total_price = self.total_price_input.text()

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET product=?, product_quantity=?, customer=?, total_price=? WHERE id=?",
                       (product, quantity, customer, total_price, order_id))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "✅ Success!", "✅ The order has been successfully edited")
        self.load_orders()  # Update Table

    def delete_order(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "⚠️ Error", "⚠️ Please select an order!")
            return

        order_id = self.order_data[selected_row]

        reply = QMessageBox.question(self, "⚠️ Delete Confirmation", "⚠️ Are you sure you want to delete the order?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect("sales.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM orders WHERE id=?", (order_id,))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "✅ Success!", "✅ The order has been successfully deleted")
            self.load_orders()  # Update Table

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrderManager()
    window.show()
    sys.exit(app.exec())
