import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLabel, QComboBox, QLineEdit, QPushButton, QMessageBox

class OrderForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bestellformular")
        self.resize(400, 500)
        self.init_db()
        self.products = self.get_products()
        self.customers = self.get_customers()
        self.services = self.get_services()

        # Numerische Variablen für Preise
        self.current_product_price = 0.0
        self.current_service_price = 0.0

        form_layout = QFormLayout()

        self.product_select = QComboBox()
        self.product_select.addItems([p[0] for p in self.products])
        self.product_select.currentIndexChanged.connect(self.update_product_info)

        self.product_price = QLabel("💰 Produktpreis: ---")
        self.product_quantity = QLineEdit()
        self.product_quantity.textChanged.connect(self.calculate_total_price)

        form_layout.addRow("🛍️Produkt auswählen:", self.product_select)
        form_layout.addRow(self.product_price)
        form_layout.addRow("📦 Anzahl der Artikel:", self.product_quantity)

        self.customer_select = QComboBox()
        self.customer_select.addItems([c[0] for c in self.customers])
        self.customer_select.currentIndexChanged.connect(self.update_customer_info)

        self.customer_phone = QLabel("📞Telefonnummer: ---")
        self.customer_address = QLabel("📍 Adresse: ---")

        form_layout.addRow("👤 Kunden auswählen:", self.customer_select)
        form_layout.addRow(self.customer_phone)
        form_layout.addRow(self.customer_address)

        self.service_select = QComboBox()
        self.service_select.addItems([s[0] for s in self.services])
        self.service_select.currentIndexChanged.connect(self.update_service_info)

        self.service_price = QLabel("💰 Servicepreis: ---")
        form_layout.addRow("🔧 Service auswählen:", self.service_select)
        form_layout.addRow(self.service_price)

        self.total_price = QLabel("💳 Gesamtpreis: ---")
        form_layout.addRow(self.total_price)

        submit_button = QPushButton("✅ Bestellung absenden")
        submit_button.clicked.connect(self.submit_order)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)
        self.setLayout(main_layout)

        self.update_product_info()
        self.update_customer_info()
        self.update_service_info()
