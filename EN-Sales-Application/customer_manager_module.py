import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFormLayout, QLineEdit, QMessageBox

class CustomerManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customer management 👤")
        self.resize(500, 400)

        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(3) 
        self.table.setHorizontalHeaderLabels(["Customer Name", "Contact Number", "Address"])
        self.table.itemSelectionChanged.connect(self.load_selected_customer)
        layout.addWidget(self.table)

        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.address_input = QLineEdit()

        form_layout.addRow("Customer Name:", self.name_input)
        form_layout.addRow("Contact Number:", self.phone_input)
        form_layout.addRow("Address:", self.address_input)

        layout.addLayout(form_layout)

        self.update_button = QPushButton("Edit customer 🔄")
        self.update_button.clicked.connect(self.update_customer)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete customer 🗑️")
        self.delete_button.clicked.connect(self.delete_customer)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
        self.load_customers()  

    def load_customers(self):
        """ Retrieving the list of customers from the database """
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone, address FROM customers")
        customers = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(customers))
        self.customer_data = {} 

        for row, customer in enumerate(customers):
            customer_id, name, phone, address = customer
            self.customer_data[row] = customer_id  
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(phone))
            self.table.setItem(row, 2, QTableWidgetItem(address))

    def load_selected_customer(self):
        """ Display selected customer's information in the form """
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.name_input.setText(self.table.item(selected_row, 0).text())
            self.phone_input.setText(self.table.item(selected_row, 1).text())
            self.address_input.setText(self.table.item(selected_row, 2).text())

    def update_customer(self):
        """ Editing customer information in the database """
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error ⚠️", "please select a customer!")
            return

        customer_id = self.customer_data[selected_row]
        name = self.name_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE customers SET name=?, phone=?, address=? WHERE id=?",
                       (name, phone, address, customer_id))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success! ✅", "The customer was successfully edited.")
        self.load_customers()

    def delete_customer(self):
        """ Delete customer from the database """
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error ⚠️", "Please select a customer!")
            return

        customer_id = self.customer_data[selected_row]

        reply = QMessageBox.question(self, "Confirm deletion ⚠️", "Are you sure you want to delete this customer?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect("sales.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM customers WHERE id=?", (customer_id,))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success! ✅", "Customer was successfully deleted.")
            self.load_customers() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomerManager()
    window.show()
    sys.exit(app.exec())
