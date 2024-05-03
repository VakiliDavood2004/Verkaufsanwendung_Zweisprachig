import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFormLayout, QLineEdit, QMessageBox

class ServiceManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dienstleistungsverwaltung")
        self.resize(500, 400)

        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(3)  # Name, Preis, Beschreibung
        self.table.setHorizontalHeaderLabels(["Dienstleistungsname", "Preis", "Beschreibung"])
        self.table.itemSelectionChanged.connect(self.load_selected_service)
        
        layout.addWidget(self.table)
        
        # Formular zur Bearbeitung von Dienstleistungen
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.description_input = QLineEdit()

        form_layout.addRow("Dienstleistungsname:", self.name_input)
        form_layout.addRow("Preis:", self.price_input)
        form_layout.addRow("Beschreibung:", self.description_input)

        layout.addLayout(form_layout)
        
        # Aktionsschaltflächen
        self.update_button = QPushButton("🔄Dienstleistung bearbeiten")
        self.update_button.clicked.connect(self.update_service)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("🗑️ Dienstleistung löschen")
        self.delete_button.clicked.connect(self.delete_service)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
        self.load_services()  # Informationen beim Programmstart anzeigen
