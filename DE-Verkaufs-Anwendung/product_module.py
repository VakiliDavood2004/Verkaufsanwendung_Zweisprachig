import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox

class ProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Artikelinformationen")
        self.resize(400, 300)
        self.init_db()
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.category_input = QComboBox()  
        self.category_input.addItems(["Rohstoffe", "Industriematerialien", "Lebensmittel", "Verschiedenes"])

        self.description_input = QLineEdit()

        form_layout.addRow("Artikelname:", self.name_input)
        form_layout.addRow("Preis:", self.price_input)
        form_layout.addRow("Kategorie:", self.category_input)
        form_layout.addRow("Beschreibung:", self.description_input)

        submit_button = QPushButton("Artikel registrieren")
        submit_button.clicked.connect(self.submit_data)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)
        self.setLayout(main_layout)

    def init_db(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT
            )
        """)
        conn.commit()
        conn.close()

