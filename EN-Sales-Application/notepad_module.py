import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QTextEdit,
    QPushButton, QLineEdit, QMessageBox
)
from PyQt5.QtCore import Qt

import sqlite3
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    created_at TEXT
)
""")
conn.commit()
conn.close()

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📝 Professioneller Notizblock")
        self.setMinimumSize(600, 400)
        self.setup_ui()
        self.load_notes()

    def setup_ui(self):
        self.note_list = QListWidget()
        self.note_list.setStyleSheet("background-color: #ecf0f1; font-size: 14px;")
        self.note_list.itemClicked.connect(self.display_note)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("📝 Notiztitel")
        self.title_input.setStyleSheet("font-size: 16px; padding: 6px;")

        self.text_area = QTextEdit()
        self.text_area.setStyleSheet("font-size: 14px; background-color: #fdfdfd;")

        save_btn = QPushButton("💾 Speichern")
        save_btn.clicked.connect(self.save_note)

        delete_btn = QPushButton("🗑️ Löschen")
        delete_btn.clicked.connect(self.delete_note)

        new_btn = QPushButton("🆕 Neue Notiz")
        new_btn.clicked.connect(self.new_note)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(delete_btn)
        btn_layout.addWidget(new_btn)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.title_input)
        right_layout.addWidget(self.text_area)
        right_layout.addLayout(btn_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.note_list, 1)
        main_layout.addLayout(right_layout, 3)

        self.setLayout(main_layout)

    def load_notes(self):
        self.note_list.clear()
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, title FROM notes ORDER BY created_at DESC")
        for id_, title in cursor.fetchall():
            self.note_list.addItem(f"{id_}: {title}")
        conn.close()

    def display_note(self, item):
        note_id = int(item.text().split(":")[0])
        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        cursor.execute("SELECT title, content FROM notes WHERE id=?", (note_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            self.title_input.setText(result[0])
            self.text_area.setText(result[1])
            self.current_note_id = note_id
        else:
            QMessageBox.warning(self, "Fehler ❌", "Notiz nicht gefunden.")

    def save_note(self):
        title = self.title_input.text().strip()
        content = self.text_area.toPlainText().strip()

        if not title:
            QMessageBox.warning(self, "Warnung", "Notiztitel darf nicht leer sein!")
            return

        conn = sqlite3.connect("sales.db")
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if hasattr(self, "current_note_id"):
            cursor.execute("UPDATE notes SET title=?, content=? WHERE id=?", (title, content, self.current_note_id))
        else:
            cursor.execute("INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)", (title, content, now))
            self.current_note_id = cursor.lastrowid

        conn.commit()
        conn.close()
        self.load_notes()
        QMessageBox.information(self, "Gespeichert", "Die Notiz wurde erfolgreich gespeichert!")

    def delete_note(self):
        if hasattr(self, "current_note_id"):
            confirm = QMessageBox.question(self, "🗑️ Notiz löschen", "⚠️ Sind Sie sicher??", QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                conn = sqlite3.connect("sales.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM notes WHERE id=?", (self.current_note_id,))
                conn.commit()
                conn.close()
                self.new_note()
                self.load_notes()
        else:
            QMessageBox.warning(self, "❌ Löschen nicht möglich", "⚠️ Es wurde keine Notiz ausgewählt")

    def new_note(self):
        self.title_input.clear()
        self.text_area.clear()
        if hasattr(self, "current_note_id"):
            del self.current_note_id
