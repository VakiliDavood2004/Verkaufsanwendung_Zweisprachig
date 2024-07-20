import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class DeleteProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete item")
        self.resize(400, 150)

        form_layout = QFormLayout()
        self.product_id_input = QLineEdit()
        self.product_id_input.setPlaceholderText("Enter the product ID")

        form_layout.addRow("Product ID:", self.product_id_input)

        delete_button = QPushButton("Delete item ❌")
        delete_button.clicked.connect(self.delete_product)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(delete_button)
        self.setLayout(main_layout)

    def delete_product(self):
        product_id = self.product_id_input.text()

        if not product_id.isdigit():
            QMessageBox.warning(self, "Error", "Please enter a valid ID!")
            return
        
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        conn.commit()
        affected_rows = cursor.rowcount
        conn.close()

        if affected_rows > 0:
            QMessageBox.information(self, "Success", "The item was successfully deleted!")
            self.product_id_input.clear()
        else:
            QMessageBox.warning(self, "Error", "No item found with this ID!")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeleteProductForm()
    window.show()
    sys.exit(app.exec())
