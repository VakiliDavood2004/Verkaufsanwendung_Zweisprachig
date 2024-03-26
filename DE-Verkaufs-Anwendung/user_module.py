import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class User_Form(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initDB()

