import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QTextEdit
)
from PyQt5.QtCore import Qt

# Eine Feedback-Tabelle in der Datenbank erstellen (nur einmal erforderlich)
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    score INTEGER,
    created_at TEXT
)
""")
conn.commit()
conn.close()

class FeedbackForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kundenfeedback-Formular 💬")
        self.setFixedSize(400, 400)
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        self.label = QLabel("Kundenkommentar oder Vorschlag:")
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Zum Beispiel war die Produktqualität ausgezeichnet…")

        self.score_label = QLabel("Gesamtbewertung:")
        self.score_buttons = []
        score_layout = QHBoxLayout()
        for i in range(1, 6):
            btn = QPushButton(str(i))
            btn.setCheckable(True)
            btn.clicked.connect(self.select_score)
            self.score_buttons.append(btn)
            score_layout.addWidget(btn)

        self.submit_btn = QPushButton("Feedback absenden 📤")
        self.submit_btn.clicked.connect(self.submit_feedback)

        self.view_btn = QPushButton("Kommentare anzeigen 📋")
        self.view_btn.clicked.connect(self.toggle_feedback_view)

        self.status = QLabel("")
        self.status.setAlignment(Qt.AlignCenter)

        self.feedback_viewer = QTextEdit()
        self.feedback_viewer.setReadOnly(True)
        self.feedback_viewer.hide()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.score_label)
        layout.addLayout(score_layout)
        layout.addWidget(self.submit_btn)
        layout.addWidget(self.view_btn)
        layout.addWidget(self.status)
        layout.addWidget(self.feedback_viewer)
        self.setLayout(layout)
