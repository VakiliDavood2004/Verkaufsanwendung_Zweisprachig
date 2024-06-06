from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class HelpForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reiseleiter")
        self.resize(500, 400)

        layout = QVBoxLayout()
        
        help_text = 
        
        label = QLabel(help_text)
        label.setWordWrap(True)
        layout.addWidget(label)

        close_button = QPushButton("schließen")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)
