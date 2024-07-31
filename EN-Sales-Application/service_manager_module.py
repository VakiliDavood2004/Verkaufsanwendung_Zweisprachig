import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QFormLayout, QLineEdit, QMessageBox

class ServiceManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Service Management")
        self.resize(500, 400)

        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(3)  # "Name, Price, Description"
        self.table.setHorizontalHeaderLabels(["Service Name", "Price", "Description"])
        self.table.itemSelectionChanged.connect(self.load_selected_service)
        
        layout.addWidget(self.table)
        
        # Service Edit Form
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.description_input = QLineEdit()

        form_layout.addRow("Service Name:", self.name_input)
        form_layout.addRow("Price:", self.price_input)
        form_layout.addRow("Description:", self.description_input)

        layout.addLayout(form_layout)
        
        # Action Buttons
        self.update_button = QPushButton("🔄 Edit Service")
        self.update_button.clicked.connect(self.update_service)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("🗑️ Delete Service")
        self.delete_button.clicked.connect(self.delete_service)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
        self.load_services()  # Display information on program startup

    def load_services(self):
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, description FROM services")
        services = cursor.fetchall()
        conn.close()

        self.table.setRowCount(len(services))  # Set number of rows
        self.table.setColumnCount(3)

        self.service_data = {}  # Store IDs for delete and edit operations

        for row, service in enumerate(services):
            service_id, name, price, description = service
            self.service_data[row] = service_id  # Store ID for use in edit and delete operations
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
            QMessageBox.warning(self, "Error", "Please select a service!")
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

        QMessageBox.information(self, "Success!", "The service was successfully edited.")
        self.load_services()  # Update Table

    def delete_service(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a service!")
            return

        service_id = self.service_data[selected_row]

        reply = QMessageBox.question(self, "Delete Confirmation", "Are you sure you want to delete this service?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect("sales.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM services WHERE id=?", (service_id,))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success!", "The service was successfully deleted.")
            self.load_services()  # Update Table
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServiceManager()
    window.show()
    sys.exit(app.exec())
