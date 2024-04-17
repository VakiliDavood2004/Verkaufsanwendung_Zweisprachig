import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class DeleteProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Element löschen")
        self.resize(400, 150)

        form_layout = QFormLayout()
        self.product_id_input = QLineEdit()
        self.product_id_input.setPlaceholderText("Produkt-ID eingeben")

        form_layout.addRow("Produkt-ID:", self.product_id_input)

        delete_button = QPushButton("Element löschen ❌")
        delete_button.clicked.connect(self.delete_product)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(delete_button)
        self.setLayout(main_layout)
