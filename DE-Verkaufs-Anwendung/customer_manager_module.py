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
    def load_customers(self):
        """ Abrufen der Kundenliste aus der Datenbank """
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
        """ Ausgewählte Kundendaten im Formular anzeigen """
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.name_input.setText(self.table.item(selected_row, 0).text())
            self.phone_input.setText(self.table.item(selected_row, 1).text())
            self.address_input.setText(self.table.item(selected_row, 2).text())

    def update_customer(self):
        """ Bearbeiten von Kundendaten in der Datenbank """
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Fehler ⚠️", "Bitte wählen Sie einen Kunden aus!")
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

        QMessageBox.information(self, "Erfolg! ✅", "Der Kunde wurde erfolgreich bearbeitet.")
        self.load_customers()
