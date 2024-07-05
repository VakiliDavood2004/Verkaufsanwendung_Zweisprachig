import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class User_Form(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initDB()

    def initUI(self):
        self.setWindowTitle("Username And password")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label1 = QLabel("Username:")
        self.input1 = QLineEdit()

        self.label2 = QLabel("password:")
        self.input2 = QLineEdit()
        self.input2.setEchoMode(QLineEdit.Password)

        self.submit_btn = QPushButton("Save")
        self.submit_btn.clicked.connect(self.saveData)

        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)

    def initDB(self):
        """ Create Table if not exists """
        self.conn = sqlite3.connect("sales.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user_pass (
                                id INTEGER PRIMARY KEY,
                                user_name TEXT,
                                password TEXT)''')
        self.conn.commit()

    def saveData(self):
        user_name = self.input1.text()
        password = self.input2.text()

        if user_name and password:
            self.cursor.execute("INSERT INTO user_pass (user_name, password) VALUES (?, ?)", (user_name, password))
            self.conn.commit()
            print("Data saved successfully!")

            self.input1.clear() 
            self.input2.clear()  
        else:
            print("Please enter your username and password!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = User_Form()
    window.show()
    sys.exit(app.exec_())
