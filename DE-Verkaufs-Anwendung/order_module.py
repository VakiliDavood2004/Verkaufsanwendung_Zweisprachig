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

    def init_db(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product TEXT NOT NULL,
                product_price REAL NOT NULL,
                product_quantity INTEGER NOT NULL,
                customer TEXT NOT NULL,
                customer_phone TEXT NOT NULL,
                customer_address TEXT NOT NULL,
                service TEXT NOT NULL,
                service_price REAL NOT NULL,
                total_price REAL NOT NULL,
                order_date TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def get_products(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, price FROM products")
        data = cursor.fetchall()
        conn.close()
        return data if data else [("Keine Artikel verfügbar", "0")]

    def get_customers(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, phone, address FROM customers")
        data = cursor.fetchall()
        conn.close()
        return data if data else [("Kein Kunde verfügbar", "---", "---")]

    def get_services(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, price FROM services")
        data = cursor.fetchall()
        conn.close()
        return data if data else [("Keine Services verfügbar", "0")]

    def update_product_info(self):
        selected_index = self.product_select.currentIndex()
        selected_product = self.products[selected_index]
        self.current_product_price = float(selected_product[1])
        self.product_price.setText(f"💰 Produktpreis: {selected_product[1]} Euros")
        self.calculate_total_price()

    def update_customer_info(self):
        selected_index = self.customer_select.currentIndex()
        selected_customer = self.customers[selected_index]
        self.customer_phone.setText(f"📞 Telefonnummer: {selected_customer[1]}")
        self.customer_address.setText(f"📍 Adresse: {selected_customer[2]}")

    def update_service_info(self):
        selected_index = self.service_select.currentIndex()
        selected_service = self.services[selected_index]
        self.current_service_price = float(selected_service[1])
        self.service_price.setText(f"💰 Servicepreis: {selected_service[1]} Euro")
        self.calculate_total_price()

    def calculate_total_price(self):
        try:
            quantity = int(self.product_quantity.text() or 0)
            total = (self.current_product_price * quantity) + self.current_service_price
            self.total_price.setText(f"💳 Gesamtpreis: {total} Euro")
        except ValueError:
            self.total_price.setText("💳 Gesamtpreis: ---")

    def submit_order(self):
        try:
            if self.product_quantity.text() == "":
                QMessageBox.warning(self, "⚠️ Fehler", "Bitte geben Sie die Artikelmenge ein!")
                return

            quantity = int(self.product_quantity.text())
            total = (self.current_product_price * quantity) + self.current_service_price
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            conn = sqlite3.connect("sales.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO orders (product, product_price, product_quantity, customer,
                                    customer_phone, customer_address, service, service_price,
                                    total_price, order_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                self.product_select.currentText(),
                self.current_product_price,
                quantity,
                self.customer_select.currentText(),
                self.customer_phone.text().replace("📞 Telefonnummer: ", "").strip(),
                self.customer_address.text().replace("📍 Adresse: ", "").strip(),
                self.service_select.currentText(),
                self.current_service_price,
                total,
                order_date
            ))

            conn.commit()
            conn.close()
            QMessageBox.information(self, "✅ Erfolg!", "Ihre Bestellung wurde erfolgreich aufgegeben.")

        except sqlite3.Error as db_error:
            QMessageBox.warning(self, "⚠️ Datenbankfehler", f"Datenbankfehler:\n{db_error}")

        except Exception as e:
            QMessageBox.warning(self, "⚠️ Unerwarteter Fehler", f"Unerwarteter Fehler:\n{e}")
