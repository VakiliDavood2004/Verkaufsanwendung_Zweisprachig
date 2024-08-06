import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton

class ReportForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Order Report")
        self.resize(800, 400)
        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(10)  # Number of table columns
        self.table.setHorizontalHeaderLabels([ 
            "🆔 ID", "🛍️ Item", "💰 Item Price", "📦 Quantity", "👤 Customer", "📞 Contact", 
            "📍 Address", "🔧 Service", "💰 Service Price", "💳 Total Price", "📅 Order Date" 
        ])

        layout.addWidget(QLabel("📊 List of registered orders"))
        layout.addWidget(self.table)

        # 🔄 Table update button
        refresh_button = QPushButton("🔄 Update Report")
        refresh_button.clicked.connect(self.load_data)
        layout.addWidget(refresh_button)

        self.setLayout(layout)
        self.load_data()  # Load data when the program starts

    def load_data(self):
        """ Fetch order information from the database and update the table """
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(orders))

        for row_idx, order in enumerate(orders):
            for col_idx, data in enumerate(order):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReportForm()
    window.show()
    sys.exit(app.exec())
