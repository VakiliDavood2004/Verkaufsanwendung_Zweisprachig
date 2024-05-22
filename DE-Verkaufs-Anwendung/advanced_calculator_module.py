from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
import math

# Zulässige Funktionen für die Verwendung in sicheren Berechnungen
allowed_names = {
    name: obj for name, obj in math.__dict__.items() if not name.startswith("__")
}
allowed_names.update({
    "sqrt": math.sqrt,
    "log": math.log,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "abs": abs,
    "pow": pow
})

def safe_eval(expr):
    try:
        expr = expr.replace("^", "**").replace("√", "sqrt")
        return str(eval(expr, {"__builtins__": None}, allowed_names))
    except:
        return "Fehler!"

class AdvancedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Professioneller Taschenrechner")
        self.setFixedSize(370, 520)
        self.create_ui()

    def create_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
            }

            QLineEdit {
                background-color: #34495e;
                border: 1px solid #95a5a6;
                font-size: 22px;
                padding: 10px;
                color: white;
                border-radius: 6px;
            }

            QPushButton {
                background-color: #1abc9c;
                border-radius: 10px;
                font-size: 18px;
                color: black;
            }

            QPushButton:hover {
                background-color: #16a085;
            }
        """)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        grid = QGridLayout()
        buttons = [
            ('√', 0, 0), ('log', 0, 1), ('sin', 0, 2), ('cos', 0, 3), ('tan', 0, 4),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('(', 4, 2), (')', 4, 3),
            ('C', 5, 0), ('^', 5, 1), ('=', 5, 2, 1, 2)
        ]

        for item in buttons:
            if len(item) == 3:
                text, row, col = item
                rowspan, colspan = 1, 1
            else:
                text, row, col, rowspan, colspan = item

            button = QPushButton(text)
            button.setFixedSize(60, 60)
            button.clicked.connect(lambda checked, t=text: self.on_click(t))
            grid.addWidget(button, row, col, rowspan, colspan)

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid)
        self.setLayout(layout)
    def on_click(self, text):
        if text == 'C':
            self.display.clear()
        elif text == '=':
            result = safe_eval(self.display.text())
            self.display.setText(result)
        else:
            current = self.display.text()
            if text in ['Sinus', 'Kosinus', 'Tangens', 'Logarithmus', 'Quadratwurzel']:
                current += f"{text}("
            else:
                current += text
            self.display.setText(current)
