import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton

class ReportForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Bestellbericht")
        self.resize(800, 400)
        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(10)  # Anzahl der Tabellenspalten
        self.table.setHorizontalHeaderLabels([
            "🆔 ID", "🛍️ Artikel", "💰 Artikelpreis", "📦 Menge", "👤 Kunde", 
            "📞 Kontakt", "📍 Adresse", "🔧 Dienstleistung", "💰 Dienstleistungspreis", 
            "💳 Gesamtpreis", "📅 Bestelldatum" 
        ])
        layout.addWidget(QLabel("📊 Liste der registrierten Bestellungen"))
        layout.addWidget(self.table)

        # Tabellenaktualisierungsschaltfläche
        refresh_button = QPushButton("🔄 Bericht aktualisieren")
        refresh_button.clicked.connect(self.load_data)
        layout.addWidget(refresh_button)

        self.setLayout(layout)
        self.load_data()  # Daten beim Programmstart laden
    def load_data(self):
        """ Bestellinformationen aus der Datenbank abrufen und die Tabelle aktualisieren """
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(orders))
