import sqlite3
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt

# Erstellen einer Tabelle in der Datenbank
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    done INTEGER DEFAULT 0
)
""")
conn.commit()
conn.close()

class Checklist(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kurze Checkliste 📝")
        self.setFixedSize(400, 500)
        self.setup_ui()
        self.apply_styles()
        self.load_tasks()

    def setup_ui(self):
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Neue Aufgabe hinzufügen...")
        self.input_field.returnPressed.connect(self.add_task)

        self.task_list = QListWidget()
        self.task_list.itemChanged.connect(self.update_task_status)  # Verwendung von itemChanged anstelle von itemClicked
        self.task_list.setSelectionMode(QListWidget.SingleSelection)

        delete_btn = QPushButton("Ausgewählte löschen 🗑")
        delete_btn.clicked.connect(self.delete_selected)

        clear_btn = QPushButton("Alle Aufgaben löschen 🧹")
        clear_btn.clicked.connect(self.clear_tasks)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(delete_btn)
        btn_layout.addWidget(clear_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.task_list)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #ecf0f1;
                font-family: Vazir, Tahoma;
            }

            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #bdc3c7;
                border-radius: 8px;
                padding: 8px;
                font-size: 15px;
            }

            QListWidget {
                background-color: #fdfdfd;
                border: 1px solid #bdc3c7;
                border-radius: 6px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #1abc9c;
                border-radius: 10px;
                padding: 8px 16px;
                font-size: 14px;
                color: white;
            }

            QPushButton:hover {
                background-color: #16a085;
            }
        """)

    def load_tasks(self):
        self.task_list.clear()
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, text, done FROM tasks ORDER BY id DESC")
        for id_, text, done in cursor.fetchall():
            item = QListWidgetItem(text)
            item.setData(Qt.UserRole, id_)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setCheckState(Qt.Checked if done else Qt.Unchecked)

            if done:
                item.setForeground(Qt.darkGray)
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)

            self.task_list.addItem(item)
        conn.close()

