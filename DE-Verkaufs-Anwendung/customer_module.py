import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class CustomerForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kunden registrieren")
        self.resize(400, 250)
        self.init_db()
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.address_input = QLineEdit()

        form_layout.addRow("Kundenname:", self.name_input)
        form_layout.addRow("Telefonnummer:", self.phone_input)
        form_layout.addRow("Adresse:", self.address_input)

        submit_button = QPushButton("Kunden registrieren")
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
