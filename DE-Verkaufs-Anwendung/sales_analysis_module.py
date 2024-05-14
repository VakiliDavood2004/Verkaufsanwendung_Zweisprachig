import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

class SalesAnalysis(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Verkaufsanalyse")
        self.resize(500, 400)
        
        layout = QVBoxLayout()
        
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)  # Nur-Anzeige-Daten, keine Bearbeitungsfunktion
        layout.addWidget(QLabel("📊 Analytischer Verkaufsbericht"))
        layout.addWidget(self.text_area)

        refresh_button = QPushButton("🔄 Bericht aktualisieren")
        refresh_button.clicked.connect(self.load_data)
        layout.addWidget(refresh_button)

        self.setLayout(layout)
        self.load_data()  # Daten beim Start laden

    def load_data(self):
        """ Verkaufsanalyse abrufen und anzeigen """
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT product, SUM(product_quantity), SUM(total_price) FROM orders GROUP BY product")
        products = cursor.fetchall()
        conn.close()

        report_text = "🏆 **Best-selling products:**\n"
        for product, quantity, total_price in products:
            report_text += f"🔹 {product}: {quantity} Einheiten , Gesamtumsatz {total_price} Euro\n"

        self.text_area.setText(report_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SalesAnalysis()
    window.show()
    sys.exit(app.exec())