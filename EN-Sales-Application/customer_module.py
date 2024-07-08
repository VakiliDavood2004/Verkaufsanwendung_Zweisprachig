import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class CustomerForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register customer")
        self.resize(400, 250)
        self.init_db()
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.address_input = QLineEdit()

        form_layout.addRow("Customer Name:", self.name_input)
        form_layout.addRow("Contact Number:", self.phone_input)
        form_layout.addRow("Address:", self.address_input)

        submit_button = QPushButton("Register customer")
        submit_button.clicked.connect(self.submit_data)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)
        self.setLayout(main_layout)

    def init_db(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT
            )
        """)
        conn.commit()
        conn.close()

    def submit_data(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()

        if not name or not phone:
            QMessageBox.warning(self, "Error", "Customer name and contact number cannot be empty!")
            return

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, phone, address) VALUES (?, ?, ?)",
                       (name, phone, address))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success!", "Customer was successfully registered.")

        # Clear form fields
        self.name_input.clear()
        self.phone_input.clear()
        self.address_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomerForm()
    window.show()
    sys.exit(app.exec())
