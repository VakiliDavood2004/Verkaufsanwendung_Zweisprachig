import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

class ProductList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Artikel anzeigen")
        self.resize(500, 400)

        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Anzahl der Spalten: Artikelname, Preis, Kategorie, Beschreibung
        self.table.setHorizontalHeaderLabels(["Artikelname", "Preis", "Kategorie", "Beschreibung"])
        
        layout.addWidget(self.table)
        
        refresh_button = QPushButton("Artikel laden")
        refresh_button.clicked.connect(self.load_products)
        layout.addWidget(refresh_button)

        self.setLayout(layout)
        self.load_products()  # Methode beim Programmstart aufrufen, um Informationen anzuzeigen

    def load_products(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, price, category, description FROM products")
        products = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(products))  # Anzahl der Zeilen festlegen

        for row, product in enumerate(products):
            for col, item in enumerate(product):
                self.table.setItem(row, col, QTableWidgetItem(str(item)))  # Jede Zelle initialisieren

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductList()
    window.show()
    sys.exit(app.exec())
