from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class HelpForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guide ")
        self.resize(500, 400)

        layout = QVBoxLayout()
        
        help_text = """
        📌 * Program Guide *:

        ****
        To use the program correctly, you must first define your products, then enter the services 
        you offer, and finally register your customers in the system. By completing these steps, you
        will be able to fully benefit from the system’s features.
        ****
        
        🛒 Product Management: Add the items for which you want to record sales.
        🔧 Service Management: Register and review services offered on products.
        📋 Order Registration: Manage and create new orders.
        🖨️ Invoice Printing: Issue invoices for customers.
        📊 Sales Reports: View sales information.
        👤 User Management: Add new users.
        🏠 Customer Management: 
               
        For more information, please contact support. 😊
        
        Contact Information 
        🌐 Website: https://vakilidavood2004.ir 
        📧 Email: vakilidavood2004@gmail.com 
        📱 Telegram – WhatsApp – Phone: +98 912 005 9751 
        📱 Telegram – WhatsApp – Phone: +98 935 723 6110 
        🔗 LinkedIn: https://www.linkedin.com/in/davood-vakili/ 
        💻 GitHub: https://github.com/VakiliDavood2004/
                
        """
        
        label = QLabel(help_text)
        label.setWordWrap(True)
        layout.addWidget(label)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)
