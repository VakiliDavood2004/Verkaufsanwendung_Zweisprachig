import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class ServiceForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Service Information Entry Form")
        self.resize(400, 300)
        self.init_db()
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.description_input = QLineEdit()

        form_layout.addRow("Service name:", self.name_input)
        form_layout.addRow("Service price:", self.price_input)
        form_layout.addRow("Description:", self.description_input)

        submit_button = QPushButton("Register service")
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

    def submit_data(self):
        name = self.name_input.text()
        price = self.price_input.text()
        description = self.description_input.text()

        if not name or not price:
            QMessageBox.warning(self, "Error", "Service name and price cannot be empty!")
            return

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO services (name, price, description) VALUES (?, ?, ?)",
                       (name, price, description))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success!", "Service registered successfully.")

        self.name_input.clear()
        self.price_input.clear()
        self.description_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServiceForm()
    window.show()
    sys.exit(app.exec())
