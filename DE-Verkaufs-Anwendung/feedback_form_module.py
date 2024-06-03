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

            QLabel {
                font-size: 14px;
                margin-top: 8px;
            }

            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-size: 14px;
                padding: 6px;
                border-radius: 6px;
            }

            QPushButton:checked {
                background-color: #27ae60;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #28b463;
            }

            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #bdc3c7;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                color: #2c3e50;
            }
        """)

    def select_score(self):
        sender = self.sender()
        for btn in self.score_buttons:
            btn.setChecked(False)
        sender.setChecked(True)

    def submit_feedback(self):
        text = self.input_text.text().strip()
        score = None
        for btn in self.score_buttons:
            if btn.isChecked():
                score = int(btn.text())

        if not text or score is None:
            QMessageBox.warning(self, "Warnung", "Bitte geben Sie Ihren Kommentar und Ihre Bewertung ein.")
            return

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (text, score, created_at) VALUES (?, ?, ?)",
                       (text, score, now))
        conn.commit()
        conn.close()

        self.status.setText(f"Feedback mit der Bewertung {score} wurde übermittelt. ✅")
        self.input_text.clear()
        for btn in self.score_buttons:
            btn.setChecked(False)
