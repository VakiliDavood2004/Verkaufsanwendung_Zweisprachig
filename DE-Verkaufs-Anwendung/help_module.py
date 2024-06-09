from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class HelpForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reiseleiter")
        self.resize(500, 400)

        layout = QVBoxLayout()
        
        help_text = """
        📌 * Programmführer *:

        ****
        Um das Programm korrekt zu verwenden, müssen Sie zunächst Ihre Produkte definieren, dann die 
        angebotenen Dienstleistungen eingeben und schließlich Ihre Kunden im System registrieren. 
        Wenn Sie diese Schritte abgeschlossen haben, können Sie alle Funktionen des Systems vollständig nutzen.
        ****
        
        🛒 Produktverwaltung: Artikel hinzufügen, für die Sie Verkäufe erfassen möchten. 
        🔧 Dienstleistungsverwaltung: Dienstleistungen registrieren und überprüfen, 
            die auf Produkte angeboten werden. 
        📋 Auftragsregistrierung: Neue Aufträge verwalten und erstellen. 
        🖨️ Rechnungsdruck: Rechnungen für Kunden ausstellen. 
        📊 Verkaufsberichte: Verkaufsinformationen anzeigen. 
        👤 Benutzerverwaltung: Neue Benutzer hinzufügen. 
        🏠 Kundenverwaltung: Kunden verwalten.
               
        Für weitere Informationen wenden Sie sich bitte an den Support.😊
        
        Kontaktinformationen
        🌐 Webseite: https://vakilidavood2004.ir 
        📧 E-Mail: vakilidavood2004@gmail.com 
        📱 Telegram – WhatsApp – Telefon: +98 912 005 9751 
        📱 Telegram – WhatsApp – Telefon: +98 935 723 6110 
        🔗 LinkedIn: https://www.linkedin.com/in/davood-vakili/ 
        💻 GitHub: https://github.com/VakiliDavood2004/        
        
        """
        
        label = QLabel(help_text)
        label.setWordWrap(True)
        layout.addWidget(label)

        close_button = QPushButton("schließen")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)
