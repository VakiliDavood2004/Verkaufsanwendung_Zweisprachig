import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox

class ProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Item Information")
        self.resize(400, 300)
        self.init_db()
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.category_input = QComboBox()  
        self.category_input.addItems(["Raw Materials", "Industrial Materials", "Food Products", "Miscellaneous"])

        self.description_input = QLineEdit()

        form_layout.addRow("Item Name:", self.name_input)
        form_layout.addRow("Price:", self.price_input)
        form_layout.addRow("Category:", self.category_input)
        form_layout.addRow("Description:", self.description_input)

        submit_button = QPushButton("Register item")
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

    def submit_data(self):
        name = self.name_input.text()
        price = self.price_input.text()
        category = self.category_input.currentText()
        description = self.description_input.text()

        if not name or not price:
            QMessageBox.warning(self, "Error", "Item name and price cannot be empty!")
            return

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, category, description) VALUES (?, ?, ?, ?)",
                       (name, price, category, description))
        conn.commit()
        conn.close()
        # cursor.execute("INSERT INTO products (name, price, category, description) VALUES ('Item One', 130, 'Raw Materials', 'For testing purposes')
        QMessageBox.information(self, "Success!", "The item has been successfully registered.")

        # Clear form fields after registration
        self.name_input.clear()
        self.price_input.clear()
        self.description_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductForm()
    window.show()
    sys.exit(app.exec())
