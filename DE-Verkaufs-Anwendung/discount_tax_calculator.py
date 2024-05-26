from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout
)
from PyQt5.QtCore import Qt

class DiscountTaxCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Steuer-/Rabattrechner 🔢")
        self.setFixedSize(360, 340)
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Grundpreis (Euro)")

        self.discount_input = QLineEdit()
        self.discount_input.setPlaceholderText("Rabattprozentsatz")

        self.tax_input = QLineEdit()
        self.tax_input.setPlaceholderText("Steuerprozentsatz")

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignTop)

        self.calc_button = QPushButton("Berechnen 💰")
        self.calc_button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.price_input)
        layout.addWidget(self.discount_input)
        layout.addWidget(self.tax_input)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f7f9fc;
                font-family: Vazir, Tahoma;
            }

            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #bdc3c7;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 15px;
                padding: 10px;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #2980b9;
            }

            QLabel {
                background-color: #ffffff;
                border: 1px solid #95a5a6;
                border-radius: 6px;
                padding: 10px;
                font-size: 14px;
                margin-top: 10px;
            }
        """)

