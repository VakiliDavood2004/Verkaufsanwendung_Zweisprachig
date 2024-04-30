import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class ServiceForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formular zur Eingabe von Dienstleistungsinformationen")
        self.resize(400, 300)
        self.init_db()
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.description_input = QLineEdit()

        form_layout.addRow("Dienstleistungsname:", self.name_input)
        form_layout.addRow("Dienstleistungspreis:", self.price_input)
        form_layout.addRow("Beschreibung:", self.description_input)

        submit_button = QPushButton("Dienstleistung registrieren")
        submit_button.clicked.connect(self.submit_data)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)
        self.setLayout(main_layout)
    def init_db(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price TEXT NOT NULL,
                description TEXT
            )
        """)
        conn.commit()
        conn.close()

