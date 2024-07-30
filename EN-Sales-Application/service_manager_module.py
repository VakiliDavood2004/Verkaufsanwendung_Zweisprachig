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

    def load_services(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, description FROM services")
        services = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(services))  # Anzahl der Zeilen festlegen
        self.table.setColumnCount(3)

        self.service_data = {}  # IDs für Lösch- und Bearbeitungsoperationen speichern

        for row, service in enumerate(services):
            service_id, name, price, description = service
            self.service_data[row] = service_id  # ID zur Verwendung bei Bearbeitungs- und Löschoperationen speichern
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(price)))
            self.table.setItem(row, 2, QTableWidgetItem(description))

    def load_selected_service(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.name_input.setText(self.table.item(selected_row, 0).text())
            self.price_input.setText(self.table.item(selected_row, 1).text())
            self.description_input.setText(self.table.item(selected_row, 2).text())

    def update_service(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Fehler", "Bitte wählen Sie eine Dienstleistung aus!")
            return

        service_id = self.service_data[selected_row]
        name = self.name_input.text()
        price = self.price_input.text()
        description = self.description_input.text()

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE services SET name=?, price=?, description=? WHERE id=?",
                       (name, price, description, service_id))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Erfolg!", "Die Dienstleistung wurde erfolgreich bearbeitet.")
        self.load_services()  # Tabelle aktualisieren

    def delete_service(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a service!")
            return

        service_id = self.service_data[selected_row]

        reply = QMessageBox.question(self, "Löschbestätigung", "Sind Sie sicher, dass Sie diese Dienstleistung löschen möchten?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect("sales.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM services WHERE id=?", (service_id,))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Erfolg!", "Die Dienstleistung wurde erfolgreich gelöscht.")
            self.load_services()  # Tabelle aktualisieren
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServiceManager()
    window.show()
    sys.exit(app.exec())
