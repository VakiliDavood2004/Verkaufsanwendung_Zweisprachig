import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

class ProductList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Display items")
        self.resize(500, 400)

        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Number of columns: Name, Price, Category, Description
        self.table.setHorizontalHeaderLabels(["Item Name", "Price", "Category", "Description"])
        
        layout.addWidget(self.table)
        
        refresh_button = QPushButton("Load items")
        refresh_button.clicked.connect(self.load_products)
        layout.addWidget(refresh_button)

        self.setLayout(layout)
        self.load_products()  # Call method to display information on program startup

    def load_products(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, price, category, description FROM products")
        products = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(products))  # Set the number of rows

        for row, product in enumerate(products):
            for col, item in enumerate(product):
                self.table.setItem(row, col, QTableWidgetItem(str(item)))  # Initialize each cell

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductList()
    window.show()
    sys.exit(app.exec())
