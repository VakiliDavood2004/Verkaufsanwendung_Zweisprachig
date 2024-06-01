from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt

class ChatWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat mit KI")
        self.setFixedSize(400, 400)
        self.init_ui()

    def init_ui(self):
        # Chatbereich mit Bildlauf
        self.chat_area = QScrollArea()
        self.chat_area.setWidgetResizable(True)
        self.chat_area.setStyleSheet("background-color: #f4f7f9; border: none;")

        self.chat_content = QVBoxLayout()
        self.chat_content.setAlignment(Qt.AlignTop)

        content_widget = QFrame()
        content_widget.setLayout(self.chat_content)
        self.chat_area.setWidget(content_widget)

        # Eingabeleiste unten
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Schreiben Sie Ihre Nachricht...")
        self.input_field.setStyleSheet("""
            QLineEdit {
                font-size: 14px;
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 8px;
            }
        """)
        self.input_field.returnPressed.connect(self.send_message)

        send_button = QPushButton("🕊️")
        send_button.setFixedSize(40, 40)
        send_button.setStyleSheet("""
            QPushButton {
                background-color: #1abc9c;
                border-radius: 20px;
                font-size: 18px;
                color: white;
            }
            QPushButton:hover {
                background-color: #16a085;
            }
        """)
        send_button.clicked.connect(self.send_message)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(send_button)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_area)
        layout.addLayout(input_layout)
        self.setLayout(layout)

    def send_message(self):
        user_msg = self.input_field.text().strip()
        if not user_msg:
            return

        self.add_message(user_msg, sender="user")
        self.input_field.clear()

        bot_reply = self.generate_reply(user_msg)
        self.add_message(bot_reply, sender="bot")

    def add_message(self, text, sender):
        label = QLabel(text)
        label.setWordWrap(True)
        label.setMaximumWidth(280)

        if sender == "user":
            label.setStyleSheet("""
                background-color: #dcf8c6;
                border-radius: 10px;
                padding: 8px;
                margin: 5px;
                color: black;
            """)
            alignment = Qt.AlignRight
        else:
            label.setStyleSheet("""
                background-color: #e5e5ea;
                border-radius: 10px;
                padding: 8px;
                margin: 5px;
                color: black;
            """)
            alignment = Qt.AlignLeft

        msg_layout = QHBoxLayout()
        msg_layout.addWidget(label)
        msg_layout.setAlignment(alignment)

        wrapper = QFrame()
        wrapper.setLayout(msg_layout)
        self.chat_content.addWidget(wrapper)

    def generate_reply(self, user_msg):
        return "Hallo, ich bin ein Roboter mit künstlicher Intelligenz, der dafür entwickelt wurde, Ihre Fragen zu beantworten. Ich werde jedoch bald gestartet und kann derzeit Ihre Fragen nicht beantworten."
