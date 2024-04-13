import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

class ProductList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Artikel anzeigen")
        self.resize(500, 400)

